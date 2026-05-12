# Minamo Keymap

A Blender add-on that provides custom keymap configurations for viewport navigation. This add-on customizes mouse controls for 3D View, 2D View, and Image Editor to improve workflow efficiency.

## Features

- **3D Viewport Navigation**: Custom mouse controls for rotating, panning, and zooming in 3D View
- **2D View Navigation**: Custom mouse controls for panning and zooming in 2D View
- **Image Editor Navigation**: Custom mouse controls for panning and zooming in Image Editor
- **Edit Mode Selection Mode Switching**: Quick selection mode switching using Alt + mouse drag in Edit Mode

## Keymap Configuration

### 3D View

- **Rotate View**: `Ctrl + Left Mouse Button`
- **Pan View**: `Ctrl + Middle Mouse Button`
- **Zoom View**: `Ctrl + Right Mouse Button`

### 2D View

- **Pan View**: `Ctrl + Left Mouse Button` or `Ctrl + Middle Mouse Button`
- **Zoom View**: `Ctrl + Right Mouse Button`

### Image Editor

- **Pan View**: `Ctrl + Left Mouse Button` or `Ctrl + Middle Mouse Button`
- **Zoom View**: `Ctrl + Right Mouse Button`

### Mesh (Edit Mode)

- **Vertex Selection Mode**: `Alt + Left Mouse Drag (West/Left)`
- **Edge Selection Mode**: `Alt + Left Mouse Drag (South/Down)`
- **Face Selection Mode**: `Alt + Left Mouse Drag (East/Right)`

## Installation

### Method 1: Remote Repository (Recommended)

1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://blender.kract.studio/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "Minamo Keymap" from the repository

### Method 2: Drag and Drop (Blender 4.2+)

1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation

1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Minamo Keymap" add-on

## Usage

After installation, the custom keymap will be automatically active:

- In **3D Viewport**: Use `Ctrl + mouse buttons` to rotate, pan, and zoom
- In **2D View**: Use `Ctrl + mouse buttons` to pan and zoom
- In **Image Editor**: Use `Ctrl + mouse buttons` to pan and zoom
- In **Edit Mode**: Use `Alt + Left Mouse Drag` in different directions to switch selection modes:
  - Drag left → Vertex selection mode
  - Drag down → Edge selection mode
  - Drag right → Face selection mode

## Compatibility

- **Blender Version**: 4.2.0 or later
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **Input Methods**: Standard mouse with left, middle, and right buttons

## License

This project is licensed under the GPL 3.0 or later license.
