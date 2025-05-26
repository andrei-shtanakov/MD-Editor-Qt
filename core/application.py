"""
Главный класс приложения
"""
from PyQt6.QtWidgets import QApplication
from core.main_window import MainWindow
from core.state_manager import StateManager

class MarkdownEditorApp:
    def __init__(self, app):
        self.app = app
        self.state_manager = StateManager()
        self.main_window = MainWindow(self.state_manager)
    
    def show(self):
        self.main_window.show()
    
    def get_main_window(self):
        return self.main_window

