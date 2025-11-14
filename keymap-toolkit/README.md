# Keymap Toolkit

A utility add-on that centralizes Blender keymap tweaks in one place. The first release includes Alt + Left Mouse drag gestures so you can quickly switch between vertex, edge, and face selection modes without hunting through menus.

## Features

- **Alt + LMB drag gestures** in Edit Mode:
  - Drag **West** → Vertex Select
  - Drag **South** → Edge Select
  - Drag **East** → Face Select
- **Z key shading toggle**:
  - Press `Z` to cycle through shading modes: Wireframe → Solid → Material Preview → Rendered → Wireframe
- **Axis constraints**:
  - `Ctrl+X` → Constrain to X axis (for translate, rotate, scale)
  - `Ctrl+Y` → Constrain to Y axis (for translate, rotate, scale)
  - `Ctrl+Z` → Constrain to Z axis (for translate, rotate, scale)
- Built with future expansion in mind so additional custom keymaps can live in a single add-on.
- Keeps your default keymap untouched—enable or disable the tweaks in one place.

## Installation

### Method 1: Remote Repository (Recommended)
1. Open `Edit > Preferences > Extensions`.
2. Expand the "Repositories" dropdown and click **Add Remote Repository**.
3. Enter `https://blender.kract.jp/api/v1/extensions/` and click **Add Repository**.
4. Find and install **Keymap Toolkit** from the repository list.

### Method 2: Drag and Drop (Blender 4.2+)
1. Download the add-on ZIP.
2. Drag and drop the ZIP into Blender.
3. The add-on installs and enables automatically.

### Method 3: Traditional Installation
1. Download the add-on ZIP.
2. Go to `Edit > Preferences > Add-ons`.
3. Click **Install...**, choose the ZIP, and enable **Keymap Toolkit**.

## Usage

### Select Mode Gestures
1. Enter Edit Mode on any mesh object.
2. Hold `Alt` and drag with the **Left Mouse Button**:
   - Drag West to switch to Vertex Select.
   - Drag South to switch to Edge Select.
   - Drag East to switch to Face Select.
3. Release the mouse to confirm the selection mode change.

### Z Key Shading Toggle
- Press `Z` in the 3D Viewport to cycle through shading modes:
  - Wireframe → Solid → Material Preview → Rendered → Wireframe

### Axis Constraints
- During transform operations (move, rotate, scale), press:
  - `Ctrl+X` to constrain movement to X axis
  - `Ctrl+Y` to constrain movement to Y axis
  - `Ctrl+Z` to constrain movement to Z axis
- Works with translate (`G`), rotate (`R`), and scale (`S`) operations.

That's it—enjoy rapid workflow improvements without extra UI clutter. As new custom keymaps are added, they'll appear in this toolkit automatically when you update the add-on.
