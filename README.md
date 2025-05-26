# Markdown Editor

A simple and functional Markdown file editor built with Python and PyQt6.

## MVP Features

- ✅ Main window with text editor
- ✅ Markdown syntax highlighting
- ✅ File opening and saving
- ✅ Basic editing operations (undo/redo)
- ✅ Unsaved changes detection on close

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

## Project Structure

The project is organized modularly for easy functionality extension:

- `core/` - Application core (main window, state management)
- `editor/` - Text editor and syntax highlighting
- `file_manager/` - File operations
- `preview/` - Preview module (stub for future development)
- `ui/` - Interface elements (stubs for future development)
- `settings/` - Settings and configuration (stubs for future development)

## Keyboard Shortcuts

- `Ctrl+N` - New file
- `Ctrl+O` - Open file
- `Ctrl+S` - Save file
- `Ctrl+Shift+S` - Save as
- `Ctrl+Z` - Undo
- `Ctrl+Y` - Redo
- `Ctrl+Q` - Exit

## Syntax Highlighting

Supports highlighting of main Markdown elements:
- Headers (H1-H6)
- Bold and italic text
- Inline code and code blocks
- Links
- Lists (bulleted and numbered)
- Quotes

## Development Roadmap

- HTML preview panel
- Toolbar with formatting buttons
- File browser
- Theme system
- Auto-save
- Export to various formats
