# Example Prompts

## JSON Prompt Example

From thesis-topics project — a structured scene description for a miniature model composition.

**File:** `prompts/participation.md`

```markdown
# Image Prompt — Topic 01: What If Participation Meant Designing, Not Just Choosing?

## Concept
The image should capture the core shift: from passive wish-listing to active designing. Multiple stakeholders around a shared urban model, each shaping the space from their perspective, discovering that their choices affect others. The mood is collaborative tension — people engaged, not fighting, but visibly wrestling with trade-offs.

## Prompt

{
  "scene_type": "miniature_architectural_model",
  "composition": {
    "arrangement": "four square tiles in 2x2 grid, one larger center tile on raised plinth",
    "viewing_angle": "isometric from above, looking diagonally",
    "surface": "clean white background, no table"
  },
  "camera": {
    "angle": "isometric overhead, approximately 45 degrees",
    "depth_of_field": "deep, all tiles sharp"
  },
  "tiles": [
    {
      "position": "top-left (tile 1)",
      "elevation": "flat on surface",
      "content": "same urban street segment redesigned with wide terracotta bike lane, miniature trees lining both sides",
      "primary_material": "terracotta with visible pores",
      "details": "same buildings as other tiles, different street treatment"
    },
    {
      "position": "top-right (tile 2)",
      "elevation": "flat on surface",
      "content": "same street segment with wide car lanes, parking spots, tiny model cars",
      "primary_material": "grey concrete",
      "details": "same buildings, car-dominated street design"
    },
    {
      "position": "bottom-left (tile 3)",
      "elevation": "flat on surface",
      "content": "same street segment with large open playground, miniature benches, swing set, green lawn",
      "primary_material": "terracotta with green accents",
      "details": "same buildings, family-oriented street design"
    },
    {
      "position": "bottom-right (tile 4)",
      "elevation": "flat on surface",
      "content": "same street segment with outdoor cafe terraces, small market stalls, pedestrian space",
      "primary_material": "terracotta with warm tones",
      "details": "same buildings, social/commercial street design"
    },
    {
      "position": "center",
      "elevation": "raised on thick concrete pedestal/plinth, above surrounding tiles",
      "content": "chaotic failed compromise — bike lane crashing into parking lot, playground wedged against highway, raw clay blocks piled haphazardly, streets leading nowhere",
      "primary_material": "mixed terracotta and grey, disorganized",
      "details": "broken, dysfunctional compared to the four coherent outer visions"
    }
  ],
  "materials": {
    "designed_elements": "cast terracotta, warm matte, visible pores and imperfections",
    "systemic_elements": "grey concrete, cool matte",
    "quality": "raw, tactile, handmade — cast concrete and terracotta feel"
  },
  "lighting": {
    "type": "soft studio lighting",
    "shadows": "subtle natural cast shadows on white surface"
  },
  "constraints": [
    "no people, no figures",
    "no text, no labels, no UI elements",
    "no table or surrounding environment",
    "same buildings on every outer tile, only street design differs"
  ]
}
```

**Key patterns:**
- Custom `tiles` array field — invented for this specific scene type
- Each tile has position, elevation, content, material, and details
- Constraints list explicitly states what to avoid
- `## Concept` explains intent; `## Prompt` has the generation payload

---

## Narrative Prompt Example

From thesis-topics project — a prose description for the same visual system.

**File:** `prompts/boundaries.md`

```markdown
# Image Prompt — Topic 05: Playing Across Boundaries

## Concept
The image should make invisible urban boundaries visible — and show people crossing them through play. A city map where neighborhood silos are revealed by spatial analysis, with game trails cutting across barriers. The mood is playful discovery — people moving through unfamiliar territory guided by a game, encountering each other across divides.

## Prompt

Isometric view from above, looking diagonally. A large concrete tile on a clean white surface showing a neighborhood model split in two by a deep physical gap — a carved-out channel representing a railway or highway barrier. The left side has dense, old, tightly packed terracotta buildings. The right side has newer, spaced-out grey concrete blocks with open areas. The two halves look like they belong to different cities. Across the gap, thin terracotta bridges and winding paths connect the two sides — small, playful, almost hidden connections that cross the barrier. Tiny concrete figures are placed on these bridges, mid-crossing. The gap itself is deep and stark, making the barrier tangible and physical. Raw, tactile, handmade quality — cast concrete and terracotta with visible pores and imperfections. Clean white background. No text, no labels, no UI elements.
```

**Key patterns:**
- Photographic/cinematic language (camera angles, materials, lighting)
- Atmosphere cues ("playful discovery", "the barrier tangible and physical")
- Specific material and texture descriptions
- Constraints woven into the prose ("No text, no labels, no UI elements")
