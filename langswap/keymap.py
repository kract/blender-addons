# -*- coding: utf-8 -*-
import bpy

# Keymap management
addon_keymaps = []


def register_keymaps():
    """Register addon keymaps"""
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name="Window", space_type="EMPTY")
        kmi = km.keymap_items.new(
            "langswap.switch_language",
            "END",
            "PRESS"
        )
        addon_keymaps.append((km, kmi))


def unregister_keymaps():
    """Unregister addon keymaps"""
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except (KeyError, ReferenceError):
            pass  # Keymap item already removed
    addon_keymaps.clear()

