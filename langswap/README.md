# LangSwap

Quickly switch between multiple languages with a single key press in Blender.

## Features

- **Multiple Language Support**: Switch between up to 5 languages dynamically
- **Easy Configuration**: Add or remove languages from the preferences panel
- **Quick Toggle**: Use the default `END` key (customizable) to cycle through languages
- **Translation Settings**: Control which UI elements are translated (Tooltips, Interface, Reports, New Data)
- **Intuitive UI**: Visual language list with add/remove buttons

## Installation

1. Download or clone this repository
2. In Blender, go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the `langswap` folder or zip file
4. Enable the addon by checking the box next to "LangSwap"

## Usage

### Initial Setup

1. Open Blender Preferences (`Edit > Preferences`)
2. Navigate to `Add-ons > System > LangSwap`
3. If no languages are configured, click "Initialize Default Languages" to add English and Japanese
4. Alternatively, use the "+" button to add languages manually
5. Configure translation settings (Tooltips, Interface, Reports, New Data)

### Switching Languages

- Press `END` key (default) to cycle through configured languages
- The current language is displayed at the top of the preferences panel
- Languages cycle in order: Language 1 → Language 2 → Language 3 → ... → Language 1

### Customizing Keymap

1. Go to `Edit > Preferences > Keymap`
2. Search for "Switch Language" under `Window`
3. Change the key assignment as needed

### Managing Languages

- **Add Language**: Click the "+" button in the preferences panel
- **Remove Language**: Select a language in the list and click the "-" button
- **Maximum**: Up to 5 languages can be configured

## Requirements

- Blender 4.2.0 or later

## License

GPL-3.0-or-later
