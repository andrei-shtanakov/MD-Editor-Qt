"""
Автодополнение (заготовка для будущего развития)
"""
from PyQt6.QtWidgets import QCompleter
from PyQt6.QtCore import QStringListModel

class MarkdownCompleter(QCompleter):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Заготовка для будущего функционала автодополнения
        pass
