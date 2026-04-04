# JSON Prompt Schemas

JSON prompts are the preferred format for precise iteration. Each field can be independently modified. The `## Prompt` section of a prompt file contains a JSON object — `generate.py` auto-detects it when the content starts with `{`.

## Common Fields

Every JSON prompt should include these fields:

- `scene_type` — High-level category (see templates below)
- `composition` — Spatial arrangement, viewing angle, framing
- `camera` — Angle, focal length, depth of field
- `lighting` — Type, mood, time of day, shadow quality
- `constraints` — What to avoid (no people, no text, no gradients, etc.)

## Choosing a Schema

| If the image is... | Use scene_type | Key fields |
|--------------------|---------------|------------|
| A physical model on a table | `physical_architectural_model` | `model_elements`, `materials` |
| A building exterior photograph | `exterior_architectural_photograph` | `building`, `landscape` |
| An interior space | `interior_architectural_render` | `room`, `objects`, `surfaces` |
| A site plan or diagram | `architectural_diagram` | `zones`, `paths`, `annotations` |
| A hand drawing or sketch | `architectural_drawing` | `medium`, `technique`, `subject` |

These are starting points. Invent fields that fit the specific image — the schema is flexible.

## Template 1: Physical Architectural Model

```json
{
  "scene_type": "physical_architectural_model",
  "composition": {
    "arrangement": "single building on rectangular site base",
    "viewing_angle": "three-quarter view from above",
    "surface": "clean white studio surface"
  },
  "camera": {
    "angle": "elevated three-quarter, ~40 degrees from above",
    "depth_of_field": "deep, entire model in focus"
  },
  "model_elements": [
    {
      "element": "main building volume",
      "material": "white museum board, clean-cut edges",
      "details": "three stories, L-shaped plan, flat roof with rooftop terrace"
    },
    {
      "element": "site base",
      "material": "grey chipboard, raw edges visible",
      "details": "rectangular platform showing street edge and courtyard"
    },
    {
      "element": "landscaping",
      "material": "dried moss and fine sand",
      "details": "courtyard garden, row of trees along street frontage"
    }
  ],
  "materials": {
    "primary": "white museum board, matte, precise cuts",
    "base": "grey chipboard with visible layers",
    "vegetation": "dried natural materials — moss, twigs, cork"
  },
  "lighting": {
    "type": "soft studio lighting",
    "shadows": "subtle cast shadows on white surface"
  },
  "constraints": ["no people or figures", "no text or labels", "handmade model aesthetic, not a 3D render"]
}
```

## Template 2: Exterior Architectural Photograph

```json
{
  "scene_type": "exterior_architectural_photograph",
  "composition": {
    "framing": "three-quarter view from street level",
    "focal_point": "building entrance"
  },
  "camera": {
    "angle": "eye-level, slight upward tilt",
    "focal_length": "35mm equivalent",
    "depth_of_field": "deep, all elements sharp"
  },
  "building": {
    "style": "contemporary residential, 3 floors",
    "facade": "white render with timber cladding accents",
    "windows": "floor-to-ceiling, thin black frames",
    "ground_floor": "recessed entrance with concrete canopy"
  },
  "landscape": {
    "foreground": "cobblestone path, ornamental grasses",
    "trees": "mature deciduous, dappled shade",
    "sky": "soft overcast, warm undertones"
  },
  "lighting": {
    "time_of_day": "late afternoon golden hour",
    "quality": "warm directional from left, long shadows"
  }
}
```

## Template 3: Interior Architectural Render

```json
{
  "scene_type": "interior_architectural_render",
  "room": {
    "type": "open-plan living area",
    "style": "warm minimalist / Japandi",
    "dimensions_feel": "spacious, 4m ceiling height"
  },
  "objects": [
    {
      "name": "lounge chair",
      "color": "cream ivory",
      "material": "textured bouclé fabric",
      "position": "center-left, beneath floor lamp"
    },
    {
      "name": "coffee table",
      "color": "light beige with grey mottling",
      "material": "travertine stone",
      "position": "foreground right, on rug"
    }
  ],
  "surfaces": {
    "floor": "light oak herringbone parquet",
    "walls": "warm white plaster with subtle texture",
    "ceiling": "smooth matte white"
  },
  "lighting": {
    "natural": "large window, left side, diffuse daylight",
    "artificial": "floor lamp with linen shade, warm 2700K",
    "mood": "calm, warm, inviting"
  },
  "camera": {
    "angle": "eye-level, seated perspective",
    "focal_length": "24mm wide",
    "depth_of_field": "shallow, foreground table soft"
  }
}
```

## Template 4: Architectural Diagram / Site Plan

```json
{
  "scene_type": "architectural_diagram",
  "diagram_type": "site plan / figure-ground",
  "composition": {
    "view": "top-down orthographic",
    "scale": "neighborhood block, ~200m across",
    "orientation": "north up"
  },
  "zones": [
    {
      "name": "residential",
      "representation": "solid warm beige fill",
      "pattern": "fine cross-hatch for private gardens"
    },
    {
      "name": "public space",
      "representation": "solid sage green fill",
      "pattern": "stipple for planted areas"
    }
  ],
  "paths": [
    {
      "type": "pedestrian",
      "representation": "thin dashed line",
      "width_feel": "narrow, intimate"
    }
  ],
  "annotations": {
    "style": "minimal, thin sans-serif labels",
    "north_arrow": true,
    "scale_bar": true
  },
  "rendering_style": "clean line drawing with flat color fills, no 3D effects"
}
```

## Template 5: Architectural Drawing / Sketch

```json
{
  "scene_type": "architectural_drawing",
  "medium": "ink and watercolor on textured paper",
  "technique": "loose hand-drawn lines with controlled watercolor washes",
  "subject": {
    "type": "building section",
    "content": "three-story residential with exposed structure",
    "key_elements": ["timber frame visible", "double-height living space", "roof garden"]
  },
  "composition": {
    "framing": "full section cut, slight perspective",
    "paper_visible": true,
    "margins": "generous white border"
  },
  "color_palette": {
    "structure": "warm sepia ink lines",
    "fills": "pale ochre and grey watercolor washes",
    "accents": "touches of green for vegetation"
  },
  "detail_level": "selective — structure and spatial volumes detailed, furniture simplified to gestures",
  "constraints": ["hand-drawn aesthetic, not digital", "visible paper texture", "no photorealistic rendering"]
}
```

## Writing Custom JSON Prompts

- Start from the closest template, then adapt
- Add type-specific fields as needed: `tiles` for miniature models, `facade` for exteriors, `objects` for interiors
- Use descriptive string values — Gemini interprets prose descriptions well
- `constraints` array is critical — explicitly state what to avoid
- Keep the JSON flat where possible — deeply nested structures can confuse generation
