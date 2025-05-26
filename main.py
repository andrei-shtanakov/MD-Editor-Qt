"""
Markdown Editor - Точка входа в приложение
"""
import sys
from PyQt6.QtWidgets import QApplication
from core.application import MarkdownEditorApp

def main():
    app = QApplication(sys.argv)
    editor_app = MarkdownEditorApp(app)
    editor_app.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
