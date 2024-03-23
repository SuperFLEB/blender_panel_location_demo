from bpy.props import EnumProperty
from bpy.types import AddonPreferences, bpy_struct

from ..lib import pkginfo
from ..panel import view3d as view3d_panel, node_editor as node_editor_panel

if "_LOADED" in locals():
    import importlib

    for mod in (pkginfo, view3d_panel, node_editor_panel):
        importlib.reload(mod)
_LOADED = True

package_name = pkginfo.package_name()


def get_location(self: "PrefsPanel"):
    return self.get("value", 0)


def set_location(self: "PrefsPanel", value: str):
    changed = self.get("value", 0) != value
    self["value"] = value
    if changed:
        # Normally you would only update the relevant panel here, but this demo has two panels so update them both.
        view3d_panel.update_panel_category()
        node_editor_panel.update_panel_category()


class PrefsPanel(AddonPreferences):
    bl_idname = package_name

    view3d_panel_location: EnumProperty(
        name="3D View panel location",
        description="Where should the panel be located in the 3D view?",
        items=[
            ("Panel Demo", 'In a "Panel Demo" tab', "Put the panel in its own tab"),
            ("Item", 'In the "Item" tab', "Put the panel after other items in the Item tab"),
            ("Edit", 'In the "Edit" tab', "Put the panel after other items in the Edit tab"),
        ],
        get=get_location,
        set=set_location
    )

    node_editor_panel_location: EnumProperty(
        name="Node Editor panel location",
        description="Where should the panel be located in the Node Editor?",
        items=[
            ("Panel Demo", 'In a "Panel Demo" tab', "Put the panel in its own tab"),
            ("Node", 'In the "Node" tab', "Put the panel after other items in the Node tab"),
            ("View", 'In the "View" tab', "Put the panel after other items in the View tab"),
        ],
        get=get_location,
        set=set_location
    )

    def draw(self, context: bpy_struct) -> None:
        layout = self.layout
        layout.prop(self, "view3d_panel_location")
        layout.prop(self, "node_editor_panel_location")


REGISTER_CLASSES = [PrefsPanel]
