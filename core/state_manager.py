"""
Управление состоянием приложения
"""
from PyQt6.QtCore import QObject, pyqtSignal

class StateManager(QObject):
    # Сигналы для уведомления об изменениях состояния
    file_opened = pyqtSignal(str)  # путь к файлу
    file_saved = pyqtSignal(str)   # путь к файлу
    text_changed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.is_modified = False
        
    def set_current_file(self, file_path):
        self.current_file = file_path
        self.file_opened.emit(file_path)
        
    def set_modified(self, modified):
        self.is_modified = modified
        if modified:
            self.text_changed.emit()
            
    def get_current_file(self):
        return self.current_file
        
    def is_file_modified(self):
        return self.is_modified

