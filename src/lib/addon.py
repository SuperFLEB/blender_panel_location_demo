from types import ModuleType
from typing import Callable, Type

import bpy

"""
This library contains helper functions useful in setup and management of Blender addons.
It is required by the __init__.py, so don't remove it unless you fix dependencies.
"""


def _collate_registerable(registerable_modules: list[ModuleType], attribute: str) -> list[Type] | list[Callable]:
    # Classes grouped by module
    mod_items = [getattr(mod, attribute) for mod in registerable_modules if hasattr(mod, attribute)]
    # Flatten (comprehension) and deduplicate (list(dict.fromkeys()))
    return list(dict.fromkeys([c for mc in mod_items for c in mc]))


def warn_unregisterable(registerable_modules: list[ModuleType]) -> None:
    def can_register(mod: ModuleType) -> bool:
        return hasattr(mod, "REGISTER_CLASSES") or hasattr(mod, "REGISTER_FUNCTIONS") or hasattr(mod,
                                                                                                 "UNREGISTER_FUNCTIONS")

    unregisterable = [mod for mod in registerable_modules if not can_register(mod)]
    if unregisterable:
        print("Panel Location Demo: Some modules had nothing to register:")
        print("\n".join([f" - {mod}" for mod in unregisterable]))


def register_classes(registerable_modules: list[ModuleType], register: bool = True) -> None:
    """
    Register or unregister classes specified in modules' REGISTER_CLASSES attributes
    :param registerable_modules: List of modules to register or unregister
    :param register: Whether to register (True) or unregister (False)
    """

    classes = _collate_registerable(registerable_modules, "REGISTER_CLASSES")
    # Reverse order when unregistering
    classes = classes if register else classes[::-1]

    for cls in classes:
        # Always unregister. If we're registering, this ensures clean-up after a prior registration failure.
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            if not register:
                print("(!) Panel Location Demo failed to unregister class:", cls)

        if register:
            bpy.utils.register_class(cls)
            if hasattr(cls, 'post_register') and callable(cls.post_register):
                cls.post_register()
            print("Panel Location Demo registered class:", cls)
        else:
            if hasattr(cls, 'post_unregister') and callable(cls.post_unregister):
                cls.post_unregister()
            print("Panel Location Demo unregistered class:", cls)


def unregister_classes(registerable_modules: list[ModuleType]) -> None:
    """
    Unregister classes specified in modules' REGISTER_CLASSES attributes
    (an alias for register_classes(registerable_modules, False))
    :param registerable_modules:
    :return:
    """
    register_classes(registerable_modules, False)
