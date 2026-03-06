#!/usr/bin/env python3
"""
GHX to LLM Format Parser

Parses Grasshopper GHX (XML) files and outputs an LLM-readable format
suitable for documentation and RAG context.

Output format:
## GROUP NAME
{id} ComponentType"NickName"[InputName:source.n{M} → OutputName:id.n]

Where:
- {M} = modifier (F/G/S/R)
- Custom names in quotes
- Wire refs as id.n

ID NUMBERING STRATEGY:
  IDs are assigned by a global topological sort across ALL components,
  using XY canvas position (X first, then Y) as tiebreaker within the
  same dependency level. This means:
  - Source components (panels, sliders, toggles) always get low IDs
  - Wire refs always point to lower-numbered components
  - IDs reflect data-flow order, not group membership or render order
  - Works identically for grouped and ungrouped definitions

  Rendering order (what appears in the output file) remains spatial
  (groups sorted by canvas position, components within groups sorted
  by column then Y). Only the {id} numbers reflect topology.
"""

import argparse
import io
import sys
import xml.etree.ElementTree as ET

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# Rhino ObjectType bitmask → human-readable names
RHINO_OBJECT_TYPES: dict[int, str] = {
    1: "Point",
    2: "PointSet",
    4: "Curve",
    8: "Surface",
    16: "Brep",
    32: "Mesh",
    512: "Light",
    4096: "Annotation",
    8192: "InstanceReference",
    65536: "Hatch",
    131072: "Morph",
    262144: "SubD",
    524288: "BrepLoop",
    2097152: "Extrusion",
}


def resolve_type_filter(value: int) -> str:
    """Decompose a Rhino ObjectType bitmask into readable names."""
    if value <= 0:
        return "*"
    parts = []
    for bit, name in sorted(RHINO_OBJECT_TYPES.items()):
        if value & bit:
            parts.append(name)
    return "+".join(parts) if parts else str(value)


@dataclass
class InputParam:
    name: str
    instance_guid: str
    sources: list[str] = field(default_factory=list)
    modifiers: set[str] = field(default_factory=set)


@dataclass
class OutputParam:
    name: str
    instance_guid: str
    index: int
    modifiers: set[str] = field(default_factory=set)


@dataclass
class Component:
    instance_guid: str
    type_name: str
    nick_name: str
    inputs: list[InputParam] = field(default_factory=list)
    outputs: list[OutputParam] = field(default_factory=list)
    value: Optional[str] = None
    x: float = 0.0
    y: float = 0.0


@dataclass
class Group:
    instance_guid: str
    nick_name: str
    member_guids: list[str] = field(default_factory=list)


def get_item_value(parent: ET.Element, name: str, default: str = "") -> str:
    """Extract value from an item element by name."""
    for item in parent.findall("item"):
        if item.get("name") == name:
            return item.text or default
    return default


def get_item_values(parent: ET.Element, name: str) -> list[str]:
    """Extract all values for items with the same name (e.g., Source, ID)."""
    values = []
    for item in parent.findall("item"):
        if item.get("name") == name:
            if item.text:
                values.append(item.text)
    return values


def extract_modifiers(items: ET.Element) -> set[str]:
    """Extract data tree modifiers from param items."""
    mods = set()
    if get_item_value(items, "SimplifyData") == "true":
        mods.add("S")
    if get_item_value(items, "GraftData") == "true":
        mods.add("G")
    if get_item_value(items, "ReverseData") == "true":
        mods.add("R")
    if get_item_value(items, "FlattenData") == "true" or get_item_value(items, "FlattenInputs") == "true":
        mods.add("F")

    # Also check Mapping value (1=Flatten, 2=Graft)
    mapping = get_item_value(items, "Mapping")
    if mapping == "1":
        mods.add("F")
    elif mapping == "2":
        mods.add("G")

    return mods


def extract_slider_value(container: ET.Element) -> Optional[str]:
    """Extract slider current value."""
    for chunk in container.findall(".//chunk"):
        items = chunk.find("items")
        if items is not None:
            value = get_item_value(items, "Value")
            if value:
                try:
                    val = float(value)
                    if val == int(val):
                        return str(int(val))
                    return f"{val:.3f}".rstrip('0').rstrip('.')
                except ValueError:
                    return value
    return None


def parse_ghx(file_path: str) -> tuple[dict[str, Component], dict[str, tuple[str, int]], list[Group]]:
    """
    Parse a GHX file and build lookup structures.

    Returns:
        components: dict mapping InstanceGuid -> Component
        outputs:    dict mapping output InstanceGuid -> (component_guid, output_index)
        groups:     list of Group objects
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    components: dict[str, Component] = {}
    outputs: dict[str, tuple[str, int]] = {}
    groups: list[Group] = []

    for chunk in root.iter("chunk"):
        if chunk.get("name") == "DefinitionObjects":
            chunks_elem = chunk.find("chunks")
            if chunks_elem is None:
                continue

            for obj_chunk in chunks_elem.findall("chunk[@name='Object']"):
                items = obj_chunk.find("items")
                if items is None:
                    continue

                type_name = get_item_value(items, "Name")
                container = obj_chunk.find(".//chunk[@name='Container']")
                if container is None:
                    continue

                container_items = container.find("items")
                if container_items is None:
                    continue

                instance_guid = get_item_value(container_items, "InstanceGuid")
                nick_name = get_item_value(container_items, "NickName")

                # Handle Groups
                if type_name == "Group":
                    member_guids = get_item_values(container_items, "ID")
                    groups.append(Group(
                        instance_guid=instance_guid,
                        nick_name=nick_name,
                        member_guids=member_guids
                    ))
                    continue

                comp = Component(
                    instance_guid=instance_guid,
                    type_name=type_name,
                    nick_name=nick_name
                )

                # Extract X,Y position from Attributes/Pivot or Bounds
                attributes = container.find(".//chunk[@name='Attributes']")
                if attributes is not None:
                    attr_items = attributes.find("items")
                    if attr_items is not None:
                        pivot = attr_items.find(".//item[@name='Pivot']")
                        if pivot is not None:
                            px = pivot.find("X")
                            py = pivot.find("Y")
                            if px is not None and px.text:
                                comp.x = float(px.text)
                            if py is not None and py.text:
                                comp.y = float(py.text)
                        else:
                            bounds = attr_items.find(".//item[@name='Bounds']")
                            if bounds is not None:
                                bx = bounds.find("X")
                                by = bounds.find("Y")
                                if bx is not None and bx.text:
                                    comp.x = float(bx.text)
                                if by is not None and by.text:
                                    comp.y = float(by.text)

                # Special component handling
                if type_name == "Panel":
                    user_text = get_item_value(container_items, "UserText")
                    if user_text:
                        comp.value = user_text
                    sources = get_item_values(container_items, "Source")
                    if sources:
                        comp.inputs.append(InputParam(
                            name="Panel", instance_guid=instance_guid,
                            sources=sources, modifiers=extract_modifiers(container_items)
                        ))
                    outputs[instance_guid] = (instance_guid, 1)
                    comp.outputs.append(OutputParam(name="Panel", instance_guid=instance_guid, index=1))

                elif type_name == "Number Slider":
                    comp.value = extract_slider_value(container)
                    outputs[instance_guid] = (instance_guid, 1)
                    comp.outputs.append(OutputParam(name="Slider", instance_guid=instance_guid, index=1))

                elif type_name == "Boolean Toggle":
                    toggle_val = get_item_value(container_items, "ToggleValue")
                    comp.value = "True" if toggle_val == "true" else "False"
                    outputs[instance_guid] = (instance_guid, 1)
                    comp.outputs.append(OutputParam(name="Toggle", instance_guid=instance_guid, index=1))

                elif type_name == "Data":
                    sources = get_item_values(container_items, "Source")
                    if sources:
                        comp.inputs.append(InputParam(
                            name="Data", instance_guid=instance_guid,
                            sources=sources, modifiers=extract_modifiers(container_items)
                        ))
                    outputs[instance_guid] = (instance_guid, 1)
                    comp.outputs.append(OutputParam(name="Data", instance_guid=instance_guid, index=1))

                elif type_name == "Scribble":
                    comp.value = get_item_value(container_items, "Text") or None

                elif type_name == "Number":
                    sources = get_item_values(container_items, "Source")
                    if sources:
                        comp.inputs.append(InputParam(
                            name="Number", instance_guid=instance_guid,
                            sources=sources, modifiers=extract_modifiers(container_items)
                        ))
                    outputs[instance_guid] = (instance_guid, 1)
                    comp.outputs.append(OutputParam(name="Number", instance_guid=instance_guid, index=1))

                elif type_name == "Colour Swatch":
                    swatch_color = container_items.find(".//item[@name='SwatchColor']")
                    if swatch_color is not None:
                        argb = swatch_color.find("ARGB")
                        if argb is not None and argb.text:
                            parts = argb.text.split(";")
                            if len(parts) == 4:
                                r, g, b = int(parts[1]), int(parts[2]), int(parts[3])
                                comp.value = f"[{r},{g},{b}]"
                    outputs[instance_guid] = (instance_guid, 1)
                    comp.outputs.append(OutputParam(name="Swatch", instance_guid=instance_guid, index=1))

                elif type_name == "Geometry Pipeline":
                    layer_filter = get_item_value(container_items, "LayerFilter", "*")
                    name_filter = get_item_value(container_items, "NameFilter", "*")
                    type_filter_raw = get_item_value(container_items, "TypeFilter", "0")
                    try:
                        type_filter = resolve_type_filter(int(type_filter_raw))
                    except ValueError:
                        type_filter = "*"
                    comp.value = f'Layer:"{layer_filter}",Name:"{name_filter}",Type:{type_filter}'
                    outputs[instance_guid] = (instance_guid, 1)
                    comp.outputs.append(OutputParam(
                        name="Pipeline", instance_guid=instance_guid, index=1
                    ))

                # Generic param_input chunks
                for param_chunk in container.findall(".//chunk[@name='param_input']"):
                    param_items = param_chunk.find("items")
                    if param_items is None:
                        continue
                    comp.inputs.append(InputParam(
                        name=get_item_value(param_items, "Name"),
                        instance_guid=get_item_value(param_items, "InstanceGuid"),
                        sources=get_item_values(param_items, "Source"),
                        modifiers=extract_modifiers(param_items)
                    ))

                # Generic param_output chunks
                for idx, param_chunk in enumerate(container.findall(".//chunk[@name='param_output']")):
                    param_items = param_chunk.find("items")
                    if param_items is None:
                        continue
                    param_name = get_item_value(param_items, "Name")
                    param_guid = get_item_value(param_items, "InstanceGuid")
                    output = OutputParam(
                        name=param_name,
                        instance_guid=param_guid,
                        index=idx + 1,
                        modifiers=extract_modifiers(param_items)
                    )
                    comp.outputs.append(output)
                    outputs[param_guid] = (instance_guid, idx + 1)

                # ParameterData (Merge, Entwine, etc.)
                param_data = container.find(".//chunk[@name='ParameterData']")
                if param_data is not None:
                    for param_chunk in param_data.findall(".//chunk[@name='InputParam']"):
                        param_items = param_chunk.find("items")
                        if param_items is None:
                            continue
                        param_name = get_item_value(param_items, "NickName") or get_item_value(param_items, "Name")
                        comp.inputs.append(InputParam(
                            name=param_name,
                            instance_guid=get_item_value(param_items, "InstanceGuid"),
                            sources=get_item_values(param_items, "Source"),
                            modifiers=extract_modifiers(param_items)
                        ))

                    for param_chunk in param_data.findall(".//chunk[@name='OutputParam']"):
                        param_items = param_chunk.find("items")
                        if param_items is None:
                            continue
                        param_name = get_item_value(param_items, "NickName") or get_item_value(param_items, "Name")
                        param_guid = get_item_value(param_items, "InstanceGuid")
                        output = OutputParam(
                            name=param_name,
                            instance_guid=param_guid,
                            index=len(comp.outputs) + 1,
                            modifiers=extract_modifiers(param_items)
                        )
                        comp.outputs.append(output)
                        outputs[param_guid] = (instance_guid, output.index)

                # Fallback: standalone persistent parameters (Curve, Point, Brep,
                # Mesh, Surface, etc.) have no param chunks  -  their InstanceGuid
                # IS the output, and Source items provide inputs.
                if not comp.outputs and type_name != "Scribble":
                    has_param_chunks = (
                        container.findall(".//chunk[@name='param_input']")
                        or container.findall(".//chunk[@name='param_output']")
                        or container.find(".//chunk[@name='ParameterData']") is not None
                    )
                    if not has_param_chunks:
                        sources = get_item_values(container_items, "Source")
                        if sources:
                            comp.inputs.append(InputParam(
                                name=type_name, instance_guid=instance_guid,
                                sources=sources, modifiers=extract_modifiers(container_items)
                            ))
                        outputs[instance_guid] = (instance_guid, 1)
                        comp.outputs.append(OutputParam(
                            name=type_name, instance_guid=instance_guid, index=1
                        ))

                components[instance_guid] = comp

    return components, outputs, groups


def build_global_id_map(
    components: dict[str, Component],
    outputs: dict[str, tuple[str, int]]
) -> dict[str, int]:
    """
    Assign IDs using a spatial-first ordering that still respects topology.

    Strategy:
      1. Sort ALL components by canvas position (X primary, Y secondary).
         This gives a natural left-to-right, top-to-bottom reading order.
      2. Walk that spatial order and check each component's dependencies.
         If any dependency hasn't been assigned an ID yet, defer the
         component until its dependencies are resolved.
      3. Repeat deferred components until all are placed.

    This means:
    - IDs closely follow canvas position (spatially readable)
    - id(source) < id(consumer) is guaranteed for every wire
    - Inline constants (Unit Z etc.) get IDs near their canvas position,
      which is near their consumers  -  naturally correct
    - Panels/sliders at left edge get low IDs  -  naturally correct
    - Large ID gaps only occur when long cross-canvas wires exist,
      which accurately reflects the script's actual structure
    """
    all_guids = list(components.keys())
    guid_set = set(all_guids)

    # Build dependency map: dependencies[guid] = set of guids it depends on
    dependencies: dict[str, set[str]] = {guid: set() for guid in all_guids}
    for guid in all_guids:
        for inp in components[guid].inputs:
            for source_guid in inp.sources:
                if source_guid in outputs:
                    src_comp, _ = outputs[source_guid]
                    if src_comp in guid_set and src_comp != guid:
                        dependencies[guid].add(src_comp)

    def xy_key(guid: str) -> tuple[float, float]:
        c = components.get(guid)
        return (c.x, c.y) if c else (999999.0, 999999.0)

    # Step 1: sort all components spatially
    spatial_order = sorted(all_guids, key=xy_key)

    # Step 2: walk spatial order, deferring any component whose
    # dependencies haven't been assigned yet
    assigned: set[str] = set()
    topo_order: list[str] = []

    pending = list(spatial_order)
    max_passes = len(all_guids) + 1  # guard against cycles

    for _ in range(max_passes):
        if not pending:
            break
        still_pending = []
        made_progress = False
        for guid in pending:
            if dependencies[guid].issubset(assigned):
                topo_order.append(guid)
                assigned.add(guid)
                made_progress = True
            else:
                still_pending.append(guid)
        pending = still_pending
        if not made_progress:
            # Cycle or unresolvable  -  just assign remaining in spatial order
            topo_order.extend(pending)
            break

    return {guid: idx for idx, guid in enumerate(topo_order, start=1)}


def format_component(
    comp: Component,
    comp_id: int,
    id_map: dict[str, int],
    outputs: dict[str, tuple[str, int]]
) -> str:
    """Format a single component as a text line."""

    def resolve(source_guid: str, modifiers: set[str]) -> str:
        if source_guid in outputs:
            src_comp_guid, out_idx = outputs[source_guid]
            src_id = id_map.get(src_comp_guid, "?")
            ref = f"{src_id}.{out_idx}"
            if modifiers:
                ref += "".join(sorted(modifiers))
            return ref
        return "?"

    # --- Special types with values ---
    if comp.value is not None:
        if comp.type_name == "Panel":
            nick = f'"{comp.nick_name}"' if comp.nick_name else ""
            inp_refs = [
                resolve(src, inp.modifiers)
                for inp in comp.inputs for src in inp.sources
            ]
            if inp_refs:
                return f'{{{comp_id}}} Panel{nick}[{",".join(inp_refs)}→{comp_id}.1]=({comp_id}.1)'
            val = comp.value[:50] + "..." if len(comp.value) > 50 else comp.value
            return f'{{{comp_id}}} Panel{nick}[→{comp_id}.1]=({val.replace(chr(10), chr(92)+"n")})'

        if comp.type_name == "Number Slider":
            return f'{{{comp_id}}} Slider[→{comp_id}.1]=({comp.value})'

        if comp.type_name == "Boolean Toggle":
            return f'{{{comp_id}}} Toggle[→{comp_id}.1]=({comp.value})'

        if comp.type_name == "Scribble":
            text = comp.value[:40] + "..." if len(comp.value) > 40 else comp.value
            return f'{{{comp_id}}} Scribble"{text.replace(chr(10), " ")}"'

        if comp.type_name == "Colour Swatch":
            return f'{{{comp_id}}} Swatch[→{comp_id}.1]=({comp.value})'

        if comp.type_name == "Geometry Pipeline":
            return f'{{{comp_id}}} Geometry Pipeline[→{comp_id}.1]({comp.value})'

    # --- Data relay (simplified) ---
    if comp.type_name == "Data" and len(comp.inputs) == 1 and len(comp.outputs) == 1:
        nick = f'"{comp.nick_name}"' if comp.nick_name else ""
        inp = comp.inputs[0]
        ref = resolve(inp.sources[0], inp.modifiers) if inp.sources else "x"
        return f'{{{comp_id}}} Data{nick}[{ref}→{comp_id}.1]'

    # --- Number primitive (simplified) ---
    if comp.type_name == "Number" and len(comp.outputs) == 1:
        if comp.inputs and comp.inputs[0].sources:
            inp = comp.inputs[0]
            ref = resolve(inp.sources[0], inp.modifiers)
            return f'{{{comp_id}}} Number[{ref}→{comp_id}.1]'
        return f'{{{comp_id}}} Number[→{comp_id}.1]'

    # --- General component ---
    if comp.nick_name and comp.nick_name != comp.type_name:
        header = f'{{{comp_id}}} {comp.type_name}"{comp.nick_name}"'
    else:
        header = f'{{{comp_id}}} {comp.type_name}'

    input_parts = []
    for inp in comp.inputs:
        if inp.sources:
            refs = [resolve(src, inp.modifiers) for src in inp.sources]
            if len(refs) == 1:
                input_parts.append(f"{inp.name}:{refs[0]}")
            else:
                input_parts.append(f"{inp.name}:[{','.join(refs)}]")

    def format_output(out: OutputParam) -> str:
        ref = f"{out.name}:{comp_id}.{out.index}"
        if out.modifiers:
            ref += "".join(sorted(out.modifiers))
        return ref

    output_parts = [format_output(out) for out in comp.outputs]

    inp_str = ",".join(input_parts)
    out_str = ",".join(output_parts)

    if inp_str and out_str:
        return f"{header}[{inp_str} → {out_str}]"
    elif inp_str:
        return f"{header}[{inp_str}→]"
    elif out_str:
        return f"{header}[→{out_str}]"
    return header


def generate_output(
    components: dict[str, Component],
    outputs: dict[str, tuple[str, int]],
    groups: list[Group],
    filename: str = ""
) -> str:
    """Generate the compact LLM-readable text output."""
    lines = []

    # =========================================================================
    # 1. Build global topological ID map (group-agnostic)
    # =========================================================================
    global_id_map = build_global_id_map(components, outputs)

    # =========================================================================
    # 2. Build group hierarchy
    # =========================================================================
    group_by_guid: dict[str, Group] = {g.instance_guid: g for g in groups}

    def get_all_component_members(
        group: Group,
        visited_groups: set[str] | None = None,
        visited_comps: set[str] | None = None
    ) -> list[str]:
        if visited_groups is None:
            visited_groups = set()
        if visited_comps is None:
            visited_comps = set()
        if group.instance_guid in visited_groups:
            return []
        visited_groups.add(group.instance_guid)
        members = []
        for m in group.member_guids:
            if m in components and m not in visited_comps:
                members.append(m)
                visited_comps.add(m)
            elif m in group_by_guid:
                members.extend(get_all_component_members(group_by_guid[m], visited_groups, visited_comps))
        return members

    # Explicit nesting: group GUID appears in another group's member list
    parent_to_children: dict[str, list[Group]] = {}
    for group in groups:
        for m in group.member_guids:
            if m in group_by_guid:
                parent_to_children.setdefault(group.instance_guid, []).append(group_by_guid[m])

    # Implicit nesting: Group B's components ⊂ Group A's components  →  B is subgroup of A
    group_component_sets: dict[str, set[str]] = {
        g.instance_guid: {m for m in g.member_guids if m in components}
        for g in groups
    }
    nested_group_guids: set[str] = set()

    for child in groups:
        child_comps = group_component_sets.get(child.instance_guid, set())
        if not child_comps:
            continue
        best_parent: Group | None = None
        best_size = float('inf')
        for parent in groups:
            if parent.instance_guid == child.instance_guid:
                continue
            parent_comps = group_component_sets.get(parent.instance_guid, set())
            if child_comps.issubset(parent_comps) and len(parent_comps) > len(child_comps):
                if len(parent_comps) < best_size:
                    best_parent, best_size = parent, len(parent_comps)
        if best_parent is not None:
            existing = parent_to_children.get(best_parent.instance_guid, [])
            if child not in existing:
                parent_to_children.setdefault(best_parent.instance_guid, []).append(child)
            nested_group_guids.add(child.instance_guid)

    # Explicitly nested groups (by member list)
    for group in groups:
        for m in group.member_guids:
            if m in group_by_guid:
                nested_group_guids.add(m)

    def get_direct_members(group: Group) -> list[str]:
        """Components directly in this group, excluding those belonging to subgroups."""
        nested: set[str] = set()
        for child in parent_to_children.get(group.instance_guid, []):
            nested.update(get_all_component_members(child))
        return [m for m in group.member_guids if m in components and m not in nested]

    # =========================================================================
    # 3. Identify ungrouped components; associate with nearest group
    # =========================================================================
    grouped_guids: set[str] = set()
    guid_to_group: dict[str, Group] = {}
    for group in groups:
        for m in get_all_component_members(group):
            grouped_guids.add(m)
            guid_to_group[m] = group

    ungrouped_guids = [g for g in components if g not in grouped_guids]

    ungrouped_to_group: dict[str, Group] = {}
    for ug in ungrouped_guids:
        comp = components.get(ug)
        if not comp:
            continue
        for inp in comp.inputs:
            for src in inp.sources:
                if src in outputs:
                    src_comp, _ = outputs[src]
                    if src_comp in guid_to_group:
                        ungrouped_to_group.setdefault(ug, guid_to_group[src_comp])
        for other_guid, other_comp in components.items():
            if other_guid == ug:
                continue
            for inp in other_comp.inputs:
                for src in inp.sources:
                    if src in outputs:
                        src_comp, _ = outputs[src]
                        if src_comp == ug and other_guid in guid_to_group:
                            ungrouped_to_group.setdefault(ug, guid_to_group[other_guid])

    # Propagate through ungrouped chains
    changed = True
    while changed:
        changed = False
        for ug in ungrouped_guids:
            if ug in ungrouped_to_group:
                continue
            comp = components.get(ug)
            if not comp:
                continue
            for other in ungrouped_guids:
                if other == ug or other not in ungrouped_to_group:
                    continue
                other_comp = components.get(other)
                if not other_comp:
                    continue
                for inp in other_comp.inputs:
                    for src in inp.sources:
                        if src in outputs:
                            src_comp, _ = outputs[src]
                            if src_comp == ug:
                                ungrouped_to_group[ug] = ungrouped_to_group[other]
                                changed = True
                                break
                    if ug in ungrouped_to_group:
                        break
                if ug in ungrouped_to_group:
                    break

    # =========================================================================
    # 4. Sort top-level groups spatially for rendering
    # =========================================================================
    COLUMN_WIDTH = 800

    group_positions: list[tuple[float, float, Group]] = []
    for group in groups:
        if group.instance_guid in nested_group_guids:
            continue
        members = get_all_component_members(group)
        if members:
            positions = [(components[g].x, components[g].y) for g in members if g in components]
            if positions:
                min_y = min(p[1] for p in positions)
                min_x = min(p[0] for p in positions if p[1] == min_y)
                group_positions.append((min_x, min_y, group))
                continue
        group_positions.append((999999.0, 999999.0, group))

    if group_positions:
        sorted_by_x = sorted(group_positions, key=lambda t: t[0])
        col_bounds: list[float] = [sorted_by_x[0][0]]
        for i in range(1, len(sorted_by_x)):
            if sorted_by_x[i][0] - col_bounds[-1] > COLUMN_WIDTH:
                col_bounds.append(sorted_by_x[i][0])

        x_to_col: dict[int, int] = {}
        for x, y, g in group_positions:
            best = 0
            for ci, boundary in enumerate(col_bounds):
                if x >= boundary - COLUMN_WIDTH / 2:
                    best = ci
            x_to_col[id(g)] = best

        group_positions.sort(key=lambda t: (x_to_col.get(id(t[2]), 0), t[1], t[0]))

    # =========================================================================
    # 5. Spatial sort helpers for rendering order within groups
    # =========================================================================
    COMPONENT_COLUMN_WIDTH = 100

    def sort_spatially(comp_guids: list[str]) -> list[str]:
        """Sort components by canvas column (X), then Y within column."""
        positions = [(components[g].x, components[g].y, g) for g in comp_guids if g in components]
        if not positions:
            return comp_guids

        sorted_by_x = sorted(positions, key=lambda t: t[0])
        col_bounds2: list[float] = [sorted_by_x[0][0]]
        for i in range(1, len(sorted_by_x)):
            if sorted_by_x[i][0] - col_bounds2[-1] > COMPONENT_COLUMN_WIDTH:
                col_bounds2.append(sorted_by_x[i][0])

        comp_to_col: dict[str, int] = {}
        for x, y, g in positions:
            best = 0
            for ci, boundary in enumerate(col_bounds2):
                if x >= boundary - COMPONENT_COLUMN_WIDTH / 2:
                    best = ci
            comp_to_col[g] = best

        return sorted(
            comp_guids,
            key=lambda g: (
                comp_to_col.get(g, 0),
                components[g].y if g in components else 999999.0,
                components[g].x if g in components else 999999.0
            )
        )

    def subgroup_position(subgroup: Group) -> tuple[float, float]:
        sub_comps = get_all_component_members(subgroup)
        if sub_comps:
            pos = [(components[g].x, components[g].y) for g in sub_comps if g in components]
            if pos:
                min_y = min(p[1] for p in pos)
                min_x = min(p[0] for p in pos if p[1] == min_y)
                return (min_y, min_x)
        return (999999.0, 999999.0)

    # =========================================================================
    # 6. Render
    # =========================================================================
    output_components: set[str] = set()
    group_num = 0

    def render_block(comp_guids: list[str], indent: str = "") -> None:
        for guid in sort_spatially(comp_guids):
            comp = components.get(guid)
            if comp and guid not in output_components:
                output_components.add(guid)
                comp_id = global_id_map[guid]
                lines.append(f"{indent}{format_component(comp, comp_id, global_id_map, outputs)}")

    for _min_x, _min_y, group in group_positions:
        all_members = get_all_component_members(group)
        if not all_members:
            continue
        if all(c in output_components for c in all_members):
            continue

        group_num += 1
        group_name = (group.nick_name.strip() or "UNNAMED").upper()
        lines.append(f"## GROUP {group_num}: {group_name}")
        lines.append("```")

        # Direct members first
        render_block(get_direct_members(group))

        # Nested subgroups
        subgroup_counter = 0
        for subgroup in sorted(parent_to_children.get(group.instance_guid, []), key=subgroup_position):
            sub_comps = [c for c in get_all_component_members(subgroup) if c not in output_components]
            if not sub_comps:
                continue
            subgroup_counter += 1
            sub_name = (subgroup.nick_name.strip() or "UNNAMED").upper()
            lines.append(f"### SUBGROUP {group_num}.{subgroup_counter}: {sub_name}")
            render_block(sub_comps)

        lines.append("```")

        # Ungrouped components associated with this group (sorted by topo ID)
        here = sorted(
            [g for g in ungrouped_guids if g not in output_components and ungrouped_to_group.get(g) == group],
            key=lambda g: global_id_map.get(g, 999999)
        )
        for guid in here:
            comp = components.get(guid)
            if comp:
                output_components.add(guid)
                lines.append(format_component(comp, global_id_map[guid], global_id_map, outputs))

        lines.append("")

    # Remaining ungrouped with no group association (edge case: fully ungrouped definitions)
    remaining = sorted(
        [g for g in ungrouped_guids if g not in output_components],
        key=lambda g: global_id_map.get(g, 999999)
    )
    if remaining:
        for guid in remaining:
            comp = components.get(guid)
            if comp:
                lines.append(format_component(comp, global_id_map[guid], global_id_map, outputs) + "  ")
        lines.append("")

    # =========================================================================
    # 7. Header (appended at top)
    # =========================================================================
    header_lines = [
        f"# Grasshopper Definition: {filename}" if filename else "# Grasshopper Definition",
        "",
        "## How to Read This File",
        "- **Structure**: `## GROUP` = workflow section, `### SUBGROUP` = nested group within parent",
        "- **Component**: `{id} Type\"Name\"[inputs→outputs]` where id is unique reference number",
        "- **Wiring**: `source_id.output_num` (e.g., `5.1` = component 5, output 1)",
        "- **Data flow**: Follow wire references to trace connections between components",
        "- **Modifiers**: F=Flatten, G=Graft, S=Simplify, R=Reverse (appended to wire refs)",
        "- **ID order**: IDs reflect topological data-flow order  -  lower ID = earlier in pipeline",
        "",
        "## Stats",
        f"Components: {len(components)} | Groups: {group_num}",
        "",
    ]

    return "\n".join(header_lines + lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Convert Grasshopper GHX files to LLM-readable format"
    )
    parser.add_argument("input", help="Input GHX file path")
    parser.add_argument("-o", "--output", help="Output file path (default: <input>_ghx-to-llm.md)")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of file")

    args = parser.parse_args()
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    if input_path.suffix.lower() != ".ghx":
        print(f"Warning: File does not have .ghx extension: {input_path}", file=sys.stderr)

    try:
        components, outputs, groups = parse_ghx(str(input_path))
        result = generate_output(components, outputs, groups, filename=input_path.name)

        if args.stdout:
            print(result)
        else:
            output_path = Path(args.output) if args.output else \
                input_path.parent / (input_path.stem + "_ghx-to-llm.md")
            output_path.write_text(result, encoding="utf-8")
            print(f"Output written to: {output_path}")
            print(f"Components: {len(components)}, Groups: {len(groups)}")

    except ET.ParseError as e:
        print(f"Error: Failed to parse XML: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
