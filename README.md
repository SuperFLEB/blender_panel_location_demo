# Panel Location Demo

https://github.com/SuperFLEB/blender_panel_location_demo

This is a demonstration addon that shows how to make an addon preference that puts an addons N-panel(s) into specified
tabs. It adds N-panels in both the Node Editor and 3D view, and the location of those panels can be set in Preferences.

It's based on the [Blender Addon Template](https://github.com/SuperFLEB/blender_addon_template), although this one is
stripped down to remove things like menus, operators, etc., that are not relevant to the demo.

## Notable code

### The Preferences panel

The preferences panel [src/panel/preferences](src/panel/preferences) contains the preference(s) to set the panel tabs.
In this case, there are two panels, but you will likely only have one, making things a bit simpler.

### The panels

The panels, [src/panel/node_editor.py](src/panel/node_editor.py) and [src/panel/view3d.py](src/panel/view3d.py), have
new `set_panel_category_from_prefs()` and `update_panel_category()` functions that update the proper category. In this
demo, the code is duplicated in each, but it could certainly be consolidated in an actual production case where there
are multiple panels.

### __init__.py

In order to get the preferences for the panel locations, the preference panel needs to be registered first, which is why
it's registered and deregistered separately. After that, `update_panel_category()` can be run to set the panel category
to the preference value, and the rest of the classes, including the panels, can be registered.

## To install the demo

This is mostly meant to be a reference, but if you'd like to install it you can install the ZIP file from the release,
use the build_release.py script to build a ZIP file that you can install into Blender, or symlink the `src` directory
into your Blender addons directory.
