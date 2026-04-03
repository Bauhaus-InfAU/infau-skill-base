"""
monet — Architecture-focused image generation harness.

Usage:
    python generate.py <project_dir> [prompt_ids...]     # generate images
    python generate.py <project_dir> --list              # list prompts & versions

Examples:
    python generate.py /path/to/thesis-topics                  # all prompts
    python generate.py /path/to/thesis-topics participation    # one prompt
    python generate.py /path/to/thesis-topics --list           # show what's available

API key is read from .env (GOOGLE_API_KEY or GEMINI_API_KEY).
"""

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image as PILImage

# --- Constants ---
DEFAULT_MODEL = "gemini-3.1-flash-image-preview"
DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_IMAGE_SIZE = "2K"


def is_json_prompt(text):
    """Check if prompt text is a JSON scene description."""
    stripped = text.strip()
    return stripped.startswith("{") and stripped.endswith("}")


def resolve_project_dir(path_str):
    """Validate that the given path is a project directory with prompts/."""
    project_dir = Path(path_str).resolve()
    if not project_dir.is_dir():
        print(f"Error: Project directory not found: {project_dir}")
        sys.exit(1)
    prompts_dir = project_dir / "prompts"
    if not prompts_dir.is_dir():
        print(f"Error: No prompts/ directory in {project_dir}")
        sys.exit(1)
    return project_dir


def discover_prompts(project_dir):
    """Scan prompts/ for *.md files containing '## Prompt'; skip _-prefixed files."""
    prompts_dir = project_dir / "prompts"
    result = {}
    for md_file in sorted(prompts_dir.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        text = md_file.read_text(encoding="utf-8")
        if "## Prompt" in text:
            result[md_file.stem] = md_file
    return result


def strip_code_fence(text):
    """Strip markdown code fences (```json ... ``` or ``` ... ```) if present."""
    import re
    match = re.match(r"^```\w*\s*\n(.*)\n```\s*$", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text


def extract_prompt(filepath):
    """Return text after '## Prompt' marker (fallback: after first blank line)."""
    text = filepath.read_text(encoding="utf-8")
    marker = "## Prompt"
    if marker in text:
        prompt = text.split(marker, 1)[1].strip()
        return strip_code_fence(prompt)
    return text.split("\n\n", 1)[-1].strip()


def load_design_concept(project_dir):
    """Read context/_design_concept.md if it exists, return content or None."""
    concept_path = project_dir / "context" / "_design_concept.md"
    if concept_path.exists():
        return concept_path.read_text(encoding="utf-8").strip()
    return None


def find_style_references(project_dir):
    """List .png/.jpg/.jpeg files in references/styles/, sorted."""
    styles_dir = project_dir / "references" / "styles"
    if not styles_dir.is_dir():
        return []
    extensions = {".png", ".jpg", ".jpeg"}
    return sorted(f for f in styles_dir.iterdir() if f.suffix.lower() in extensions)


def find_starter_images(project_dir):
    """List .png/.jpg/.jpeg files in starters/, sorted."""
    starters_dir = project_dir / "starters"
    if not starters_dir.is_dir():
        return []
    extensions = {".png", ".jpg", ".jpeg"}
    return sorted(f for f in starters_dir.iterdir() if f.suffix.lower() in extensions)


def generate_image(
    client,
    prompt_text,
    results_dir,
    prompt_id,
    style_references,
    starter_image,
    design_concept,
    model,
    aspect_ratio,
    image_size,
):
    """Build Gemini payload, call API, save versioned output to results/."""
    results_dir.mkdir(parents=True, exist_ok=True)

    # Find next available version number
    version = 1
    while (results_dir / f"{prompt_id}_v{version}.png").exists():
        version += 1
    output_path = results_dir / f"{prompt_id}_v{version}.png"

    # Build content payload
    has_styles = bool(style_references)
    has_starter = starter_image is not None
    has_concept = design_concept is not None
    json_prompt = is_json_prompt(prompt_text)

    style_instruction = (
        "Use the visual style of the reference image(s) above "
        "(materials, lighting, color palette, level of abstraction).\n\n"
    )
    concept_text = f"Follow this visual style guide:\n\n{design_concept}\n\n" if has_concept else ""

    if json_prompt:
        if has_starter:
            generate_instruction = "Transform the base image according to the following JSON scene description:\n\n"
        else:
            generate_instruction = "Generate an image based on the following JSON scene description:\n\n"
    else:
        if has_starter:
            generate_instruction = "Transform the base image above into this description:\n\n"
        else:
            generate_instruction = "Generate a new image with this description:\n\n"

    prompt_payload = concept_text + generate_instruction + prompt_text

    if has_styles:
        style_imgs = [PILImage.open(str(ref)) for ref in style_references]
        if has_starter:
            starter_img = PILImage.open(str(starter_image))
            contents = [
                *style_imgs,
                starter_img,
                style_instruction + prompt_payload,
            ]
        else:
            contents = [
                *style_imgs,
                style_instruction + prompt_payload,
            ]
    elif has_starter:
        starter_img = PILImage.open(str(starter_image))
        contents = [
            starter_img,
            prompt_payload,
        ]
    elif has_concept:
        contents = prompt_payload
    else:
        contents = prompt_text

    print(f"  Generating {prompt_id}...")
    print(f"  Prompt: {prompt_text[:100]}...")

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(str(output_path))
            print(f"  Saved: {output_path}")
            return

    print(f"  [WARNING] No image returned for {prompt_id}")
    for part in response.parts:
        if part.text is not None:
            print(f"  Model response: {part.text[:200]}")


def count_images_in(directory):
    """Count image files in a directory."""
    if not directory.is_dir():
        return 0
    extensions = {".png", ".jpg", ".jpeg"}
    return sum(1 for f in directory.iterdir() if f.suffix.lower() in extensions)


def list_prompts(project_dir):
    """Print discovered prompts with existing version counts and project stats."""
    prompts = discover_prompts(project_dir)
    results_dir = project_dir / "results"

    if not prompts:
        print("No prompts found.")
        return

    # Count project resources
    style_count = count_images_in(project_dir / "references" / "styles")
    type_count = count_images_in(project_dir / "references" / "types")
    starter_count = count_images_in(project_dir / "starters")
    context_dir = project_dir / "context"
    context_count = sum(1 for f in context_dir.glob("*.md")) if context_dir.is_dir() else 0

    print(f"Project: {project_dir.name}")
    print(f"Prompts: {len(prompts)}")
    print(f"Style references: {style_count}")
    print(f"Type references: {type_count}")
    print(f"Starters: {starter_count}")
    print(f"Context files: {context_count}")
    print()

    for prompt_id, filepath in prompts.items():
        # Count existing versions
        version_count = 0
        if results_dir.is_dir():
            version_count = len(list(results_dir.glob(f"{prompt_id}_v*.png")))
        status = f"{version_count} version(s)" if version_count else "no versions"
        print(f"  {prompt_id:30s} {status}")


def main():
    load_dotenv()

    import os

    parser = argparse.ArgumentParser(
        description="monet — Architecture-focused image generation harness"
    )
    parser.add_argument("project_dir", help="Path to project directory (must contain prompts/)")
    parser.add_argument(
        "prompt_ids", nargs="*", help="Specific prompt IDs to generate (default: all)"
    )
    parser.add_argument(
        "--list", action="store_true", help="List discovered prompts and version counts"
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL, help=f"Model to use (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--aspect-ratio",
        default=DEFAULT_ASPECT_RATIO,
        help=f"Aspect ratio (default: {DEFAULT_ASPECT_RATIO})",
    )
    parser.add_argument(
        "--image-size",
        default=DEFAULT_IMAGE_SIZE,
        help=f"Image size (default: {DEFAULT_IMAGE_SIZE})",
    )
    parser.add_argument(
        "--style",
        help="Use a specific style reference filename from references/styles/",
    )
    parser.add_argument(
        "--starter",
        help="Use a specific starter image filename from starters/",
    )
    parser.add_argument(
        "--no-concept",
        action="store_true",
        help="Skip prepending design concept to prompts",
    )

    args = parser.parse_args()

    # Resolve project
    project_dir = resolve_project_dir(args.project_dir)

    # List mode
    if args.list:
        list_prompts(project_dir)
        return

    # Validate API key
    api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: Set GOOGLE_API_KEY or GEMINI_API_KEY environment variable.")
        print("Get a key at: https://aistudio.google.com/apikey")
        sys.exit(1)

    # Discover prompts
    prompts = discover_prompts(project_dir)
    if not prompts:
        print(f"No prompts found in {project_dir / 'prompts'}")
        sys.exit(1)

    # Filter to requested prompt IDs
    if args.prompt_ids:
        unknown = [pid for pid in args.prompt_ids if pid not in prompts]
        if unknown:
            print(f"Unknown prompt(s): {', '.join(unknown)}")
            print(f"Available: {', '.join(prompts.keys())}")
            sys.exit(1)
        prompt_ids = args.prompt_ids
    else:
        prompt_ids = list(prompts.keys())

    # Load design concept
    design_concept = None
    if not args.no_concept:
        design_concept = load_design_concept(project_dir)

    # Select style references
    style_references = []
    if args.style:
        style_path = project_dir / "references" / "styles" / args.style
        if not style_path.exists():
            print(f"Error: Style reference not found: {style_path}")
            sys.exit(1)
        style_references = [style_path]
    else:
        style_references = find_style_references(project_dir)

    # Select starter image
    starter_image = None
    if args.starter:
        starter_path = project_dir / "starters" / args.starter
        if not starter_path.exists():
            print(f"Error: Starter image not found: {starter_path}")
            sys.exit(1)
        starter_image = starter_path
    else:
        starters = find_starter_images(project_dir)
        if starters:
            starter_image = starters[0]

    # Print config
    print(f"Project: {project_dir.name}")
    print(f"Model: {args.model}")
    print(f"Aspect ratio: {args.aspect_ratio}")
    print(f"Image size: {args.image_size}")
    if style_references:
        print(f"Style references: {len(style_references)} image(s)")
    if starter_image:
        print(f"Starter: {starter_image.name}")
    if design_concept:
        print(f"Design concept: loaded")
    print(f"Prompts: {', '.join(prompt_ids)}")
    print()

    # Create client once
    client = genai.Client()
    results_dir = project_dir / "results"

    for prompt_id in prompt_ids:
        prompt_text = extract_prompt(prompts[prompt_id])
        generate_image(
            client=client,
            prompt_text=prompt_text,
            results_dir=results_dir,
            prompt_id=prompt_id,
            style_references=style_references,
            starter_image=starter_image,
            design_concept=design_concept,
            model=args.model,
            aspect_ratio=args.aspect_ratio,
            image_size=args.image_size,
        )
        print()

    print("Done.")


if __name__ == "__main__":
    main()
