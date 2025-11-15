# Utilities Toolkit

A powerful Blender add-on that provides essential object manipulation utilities, starting with the "Drop It" feature that allows you to quickly drop objects to the ground or surface.

## Features

### Drop It

Drop selected objects to the ground or any surface below them with advanced options:

- **Drop by Lowest Vertex or Origin**: Choose how objects are positioned
- **Surface Alignment**: Automatically align objects to surface normals
- **Collision Detection**: Control whether selected objects collide with each other
- **Parenting Support**: Maintain or modify parent-child relationships during drop
- **Random Transformations**: Add random rotation and location variations
- **Z-Offset**: Fine-tune vertical positioning after drop
- **Multi-Object Support**: Process multiple objects simultaneously

## Installation

### Method 1: Remote Repository (Recommended)

1. Go to `Edit > Preferences > Extensions`
2. Click the dropdown arrow next to "Repositories"
3. Click "Add Remote Repository"
4. Enter the repository URL: `https://blender.kract.jp/api/v1/extensions/`
5. Click "Add Repository"
6. Browse and install "Utilities Toolkit" from the repository

### Method 2: Drag and Drop (Blender 4.2+)

1. Download the add-on as a ZIP file
2. Simply drag and drop the ZIP file into Blender
3. The add-on will be automatically installed and enabled

### Method 3: Traditional Installation

1. Download the add-on files
2. Go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the ZIP file
4. Enable the "Utilities Toolkit" add-on

## Usage

### Drop It

#### Quick Access

- **V Key**: Press `V` in 3D Viewport (Object Mode) to open the Drop It operator
- **Context Menu**: Right-click on object → "Drop It" (or press `W` → "Drop It")

#### Drop Options

**Drop By:**
- **Lowest Vertex**: Drops object based on its lowest vertex point
- **Origin**: Drops object based on its origin point

**Collision in Selection:**
- When enabled, selected objects can collide with each other during drop
- When disabled, selected objects ignore each other for collision detection

**Random Transformations:**
- **Rotation**: Random Z-axis rotation between -Z and +Z degrees
- **Location**: Random XY displacement within specified radius

**Offset Z Location:**
- Fine-tune vertical position after drop
- Positive values move up, negative values move down

**Parenting Settings:**
- **Affect Parenting**: Enable to modify parent-child relationships
- **Affect Only Parents**: Drop only parent objects, leaving children in place
- **Affect Selected Children**: Process selected child objects independently

**Surface Alignment:**
- **Align To Surface**: Automatically rotate object to match surface normal
- **No Align**: Keep object's current rotation

## Workflow Examples

### Basic Object Placement

1. Select object(s) in Object Mode
2. Press `V` to open Drop It
3. Choose "Lowest Vertex" or "Origin"
4. Click "Drop It" to execute

### Scattering Objects

1. Select multiple objects
2. Press `V`
3. Set "Random Location" radius
4. Set "Random Rotation" angle
5. Enable "Collision in Selection" if needed
6. Execute to scatter objects naturally

### Surface Alignment

1. Select object
2. Press `V`
3. Enable "Align To Surface"
4. Choose drop method
5. Object will align to surface normal upon drop

### Parenting Workflow

1. Select parent and children
2. Press `V`
3. Enable "Parenting Settings"
4. Choose whether to affect only parents or selected children
5. Objects maintain relationships during drop

## Technical Details

### Ray Casting

- Uses Blender's ray casting system to detect surfaces
- Casts rays downward from object's lowest points
- Supports distance up to 1000 units
- Automatically handles Blender version differences (2.91+)

### Performance

- Optimized for multiple objects
- Efficient vertex processing using NumPy
- Automatic visibility management during processing
- Calculation time reported in console

### Compatibility

- **Blender Version**: 4.2.0 or later
- **Object Types**: Mesh and Empty objects
- **Viewport**: Works in 3D Viewport only
- **Mode**: Object Mode required

## Keyboard Shortcuts

| Shortcut | Function                    | Location              |
| -------- | --------------------------- | --------------------- |
| `V`      | Drop It operator            | 3D Viewport (Object Mode) |
| `W` → Drop It | Context menu access | Right-click menu |

## Tips for Maximum Efficiency

1. **Quick Placement**: Use `V` key for instant access
2. **Multi-Object**: Select multiple objects and drop them all at once
3. **Surface Alignment**: Enable for natural object placement on slopes
4. **Random Variation**: Use random transforms for organic scattering
5. **Z-Offset**: Fine-tune positioning after initial drop
6. **Collision Control**: Disable "Collision in Selection" for faster processing

## Troubleshooting

- **Operator not appearing**: Ensure you're in Object Mode and 3D Viewport
- **Objects not dropping**: Check if objects are above a surface (ray cast distance: 1000 units)
- **Rotation issues**: Disable "Align To Surface" if unwanted rotation occurs
- **Parenting problems**: Use "Parenting Settings" to control parent-child behavior
- **Performance**: For many objects, disable "Collision in Selection" for faster processing

## Future Enhancements

The Utilities Toolkit is designed for expansion:

- Additional utility operators
- Custom drop presets
- Advanced collision options
- Animation support
- Batch processing tools

## Support

For issues, feature requests, or questions, please create an issue in the project repository.

## License

This project is licensed under the GPL 3.0 or later license.

