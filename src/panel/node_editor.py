import bpy
from bpy.types import Panel
from bpy.utils import register_class, unregister_class

from ..lib import pkginfo

if "_LOADED" in locals():
    import importlib

    for mod in (pkginfo,):  # list all imports here
        importlib.reload(mod)
_LOADED = True

package_name = pkginfo.package_name()


class NODE_PT_demo(Panel):
    bl_idname = 'NODE_PT_demo'
    bl_category = 'Panel Demo'
    bl_label = 'Node Editor Panel'
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        self.layout.label(text='Node Editor panel')
        box = self.layout.box()
        box.scale_y = 0.5
        box.label(text='This is a demo panel from the')
        box.label(text='Panel Location Demo addon')


def set_panel_category_from_prefs() -> None:
    """Set the panel's category (tab) from the n_panel_location preference"""
    try:
        location = bpy.context.preferences.addons[package_name].preferences.node_editor_panel_location
        NODE_PT_demo.bl_category = location
    except AttributeError:
        # This means the preferences aren't set up, so just pass and use the default
        pass


def update_panel_category() -> None:
    """Set the panel's category (tab) from the n_panel_location preference and unregister/reregister the panel"""
    unregister_class(NODE_PT_demo)
    set_panel_category_from_prefs()
    register_class(NODE_PT_demo)


REGISTER_CLASSES = [NODE_PT_demo]
