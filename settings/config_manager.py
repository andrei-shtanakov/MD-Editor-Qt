"""
Менеджер настроек (заготовка для будущего развития)
"""
from PyQt6.QtCore import QSettings

class ConfigManager:
    def __init__(self):
        self.settings = QSettings("MarkdownEditor", "Config")
        
    def save_setting(self, key, value):
        self.settings.setValue(key, value)
        
    def load_setting(self, key, default_value=None):
        return self.settings.value(key, default_value)

