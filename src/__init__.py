from .lib import addon
from .panel import node_editor
from .panel import preferences as preferences_panel
from .panel import view3d

if "_LOADED" in locals():
    import importlib

    for mod in (
            addon, preferences_panel, view3d, node_editor):  # list all imports here
        importlib.reload(mod)
_LOADED = True

package_name = __package__

bl_info = {
    "name": "Panel Location Demo",
    "description": "Demonstrates an addon preferences setting to put an N-Panel in a specified tab",
    "author": "FLEB (a.k.a. SuperFLEB)",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "location": "View3D, Node Editor",
    "warning": "This is a demo that does nothing except show a couple N-panels. See the README for information.",  # used for warning icon and text in addons panel
    "doc_url": "https://github.com/SuperFLEB/blender_panel_location_demo",
    "tracker_url": "https://github.com/SuperFLEB/blender_panel_location_demo/issues",
    "support": "COMMUNITY",
    "category": "User Interface",
}

# Registerable modules have a REGISTER_CLASSES list that lists all registerable classes in the module
registerable_modules = [
    # preferences_panel is not included in this list because it needs to be registered separately for the panel-position
    view3d,
    node_editor,
]


def register() -> None:
    # Register the prefs panel first so we can set the n-panel's "bl_category" before the n-panel gets registered
    addon.register_classes([preferences_panel])
    view3d.set_panel_category_from_prefs()
    node_editor.set_panel_category_from_prefs()

    # Register everything else. If you were registering menus, etc. from the addon template base,
    # those would go here too.
    addon.warn_unregisterable(registerable_modules)
    addon.register_classes(registerable_modules)


def unregister() -> None:
    addon.unregister_classes(registerable_modules)
    # Unregister the prefs panel
    addon.unregister_classes([preferences_panel])


if __name__ == "__main__":
    register()
