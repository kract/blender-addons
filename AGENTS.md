# Agent Guidelines

## .idea Directory Usage Policy

**Important**: Files within the `.idea/` directory may be used as implementation references, but must never be mentioned or documented in any repository files.

### Rules

1. **Implementation Reference**: You may use files from the `.idea/` directory as implementation references when developing features.

2. **Strict Documentation Prohibition**: It is strictly forbidden to mention, reference, or document that any implementation was based on or inspired by files from the `.idea/` directory in:

   - README files (`.md`)
   - Documentation files (`.md`, `.txt`, etc.)
   - Source code comments
   - Configuration files (`.toml`, `.json`, `.yaml`, etc.)
   - Any other files in the repository

3. **No Public References**: Do not include any statements such as:

   - "This implementation is based on `.idea/` files"
   - "Inspired by `.idea/` directory"
   - Any similar acknowledgments or attributions

4. **Code Implementation**: When implementing features that were referenced from `.idea/` files:
   - Implement the functionality directly
   - Write clean, original code
   - Do not include comments referencing the source
   - Document features without mentioning their origin

### Rationale

The `.idea/` directory contains IDE-specific configuration files that are:

- Not part of the project's source code
- Environment-specific and not portable
- Already excluded via `.gitignore`
- Should remain completely separate from the project documentation and codebase
- Internal implementation references only, not for public documentation

### Enforcement

When working with this repository:

- You may reference `.idea/` files for implementation guidance
- If you encounter documentation that mentions `.idea/` files, remove those references immediately
- When documenting features, describe them as if they were implemented from scratch
- Never acknowledge `.idea/` files as a source of inspiration or reference in any public-facing documentation

## Version Management

**Important**: All version updates must follow [Semantic Versioning 2.0.0](https://semver.org/) specifications.

### Rules

1. **After Feature Addition**: When adding new functionality in a backward compatible manner, increment the **MINOR** version (e.g., 1.1.0 → 1.2.0).

2. **After Bug Fix**: When fixing bugs that do not affect the API, increment the **PATCH** version (e.g., 1.1.0 → 1.1.1).

3. **After Breaking Changes**: When making incompatible API changes, increment the **MAJOR** version (e.g., 1.1.0 → 2.0.0).

4. **Version Format**: Follow the format `MAJOR.MINOR.PATCH` (e.g., `1, 2, 0` in Python tuple format for `bl_info`).

### Implementation

- Update the `version` field in `bl_info` dictionary in the addon's `__init__.py` file
- Ensure version numbers are non-negative integers without leading zeros
- Reset lower version numbers when incrementing higher ones (e.g., when incrementing MINOR, reset PATCH to 0)

### Reference

For detailed specifications, refer to: https://semver.org/

## Blender Manifest ID Rules

**Important**: The `id` field in `blender_manifest.toml` must follow strict identifier rules.

### Rules

1. **Allowed Characters**: The `id` field can only contain:
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Underscore (`_`) as the only allowed special character for word separation

2. **Prohibited Characters**: The following characters are **NOT allowed** in the `id` field:
   - Hyphen (`-`)
   - Space
   - Any other special characters

3. **Naming Convention**: 
   - Use lowercase letters only
   - **When word separation is needed, use underscores (`_`) instead of hyphens (`-`)**
   - Single-word IDs don't require underscores
   - Examples of valid IDs:
     - `viewpie` ✓ (single word, no separator needed)
     - `keymap_toolkit` ✓ (multiple words, underscore used)
     - `svg_importer_plus` ✓ (multiple words, underscore used)
   - Examples of invalid IDs:
     - `keymap-toolkit` ✗ (hyphen not allowed, use underscore)
     - `keymap toolkit` ✗ (space not allowed)
     - `KeymapToolkit` ✗ (uppercase not allowed)

4. **Directory Name vs ID**: 
   - Directory names can use hyphens (e.g., `keymap-toolkit/`, `svg-importer-plus/`)
   - When the `id` in `blender_manifest.toml` needs word separation, **convert hyphens to underscores** (e.g., `keymap-toolkit/` → `id = "keymap_toolkit"`)
   - Single-word directory names don't need conversion (e.g., `viewpie/` → `id = "viewpie"`)

### Implementation

- When creating a new addon, if the directory name uses hyphens, convert them to underscores in the `id` field
- Single-word names can be used as-is without underscores
- This is required because Blender's extension system validates the `id` as a valid identifier, and hyphens are not allowed in identifiers

### Error Prevention

- Using hyphens in the `id` field will cause the error: `key "id" invalid: Not a valid identifier`
- This error occurs during package generation when Blender validates the manifest
- **Remember**: Use underscores (`_`) for word separation, not hyphens (`-`)
