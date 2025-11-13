# Keymap Toolkit

A utility add-on that centralizes Blender keymap tweaks in one place. The first release includes the Alt + Left Mouse drag gestures extracted from the `.idea/.py` keymap so you can quickly switch between vertex, edge, and face selection modes without hunting through menus.

## Features

- **Alt + LMB drag gestures** in Edit Mode:
  - Drag **West** → Vertex Select
  - Drag **South** → Edge Select
  - Drag **East** → Face Select
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
1. Enter Edit Mode on any mesh object.
2. Hold `Alt` and drag with the **Left Mouse Button**:
   - Drag West to switch to Vertex Select.
   - Drag South to switch to Edge Select.
   - Drag East to switch to Face Select.
3. Release the mouse to confirm the selection mode change.

That's it—enjoy rapid select mode switching without extra UI clutter. As new custom keymaps are added, they'll appear in this toolkit automatically when you update the add-on.
