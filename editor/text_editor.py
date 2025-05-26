"""
Основной текстовый редактор с подсветкой синтаксиса
"""
from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from editor.markdown_highlighter import MarkdownHighlighter

class MarkdownTextEditor(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_editor()
        self.setup_highlighter()
        
    def setup_editor(self):
        # Настройка шрифта
        font = QFont("Consolas", 12)
        if not font.exactMatch():
            font = QFont("Courier New", 12)
        self.setFont(font)
        
        # Настройка отступов и табов
        self.setTabStopDistance(40)
        
        # Включение переноса слов
        self.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        
    def setup_highlighter(self):
        self.highlighter = MarkdownHighlighter(self.document())
