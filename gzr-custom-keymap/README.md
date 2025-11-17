# GZR Custom Keymap

A Blender add-on that provides custom keymaps for improved workflow efficiency.

## Features

- **Custom 3D View Navigation**:
  - `Alt + Left Click` → Rotate view
  - `Alt + Middle Click` → Pan view
  - `Alt + Right Click` → Zoom view

- **Preference Panel**: Access and customize keymaps through Add-on Preferences
- **Keymap Management**: View and modify all custom keymaps in the preferences panel

## Installation

### Method 1: Remote Repository (Recommended)

1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://blender.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "GZR Custom Keymap" from the repository

### Method 2: Drag and Drop (Blender 4.2+)

1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation

1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "GZR Custom Keymap" add-on

## Usage

### Default Keymaps

Once installed and enabled, the following keymaps are active:

**3D Viewport Navigation:**
- `Alt + Left Mouse Button` → Rotate view
- `Alt + Middle Mouse Button` → Pan view
- `Alt + Right Mouse Button` → Zoom view

### Customizing Keymaps

1. Go to `Edit > Preferences > Add-ons`
2. Find "GZR Custom Keymap" in the list
3. Click on the add-on name to expand preferences
4. Select the "Keymap" tab
5. View and modify keymaps as needed
6. Changes take effect immediately

## Keyboard Shortcuts Summary

| Shortcut              | Function      | Context    |
| --------------------- | ------------- | ---------- |
| `Alt + Left Click`    | Rotate view   | 3D Viewport |
| `Alt + Middle Click`  | Pan view      | 3D Viewport |
| `Alt + Right Click`   | Zoom view     | 3D Viewport |

## Technical Details

### Compatibility

- **Blender Version**: 4.2.0 or later
- **Viewport**: Works in 3D viewport
- **Keymap System**: Uses Blender's addon keymap system for easy customization

### Keymap Management

The add-on uses Blender's standard keymap system, allowing you to:
- View all registered keymaps in preferences
- Modify key bindings directly from preferences
- Reset to defaults if needed

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.

