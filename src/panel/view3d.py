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


class VIEW3D_PT_NPanel(Panel):
    bl_idname = 'VIEW3D_PT_n_panel'
    bl_category = 'Panel Demo'
    bl_label = '3D View Panel Demo'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        self.layout.label(text='3D view panel')
        box = self.layout.box()
        box.scale_y = 0.5
        box.label(text='This is a demo panel from the')
        box.label(text='Panel Location Demo addon')


def set_panel_category_from_prefs() -> None:
    """Set the panel's category (tab) from the n_panel_location preference"""
    try:
        location = bpy.context.preferences.addons[package_name].preferences.view3d_panel_location
        VIEW3D_PT_NPanel.bl_category = location
    except AttributeError:
        # This means the preferences aren't set up, so just pass and use the default
        pass


def update_panel_category() -> None:
    """Set the panel's category (tab) from the n_panel_location preference and unregister/reregister the panel"""
    unregister_class(VIEW3D_PT_NPanel)
    set_panel_category_from_prefs()
    register_class(VIEW3D_PT_NPanel)


REGISTER_CLASSES = [VIEW3D_PT_NPanel]
