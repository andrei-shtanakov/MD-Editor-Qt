"""
Операции с файлами
"""
import os
from pathlib import Path

class FileManager:
    def __init__(self):
        self.supported_extensions = ['.md', '.markdown', '.txt']
        
    def load_file(self, file_path):
        """Загрузка содержимого файла"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # Попытка загрузки с другой кодировкой
            with open(file_path, 'r', encoding='cp1251') as file:
                return file.read()
                
    def save_file(self, file_path, content):
        """Сохранение содержимого в файл"""
        # Создаем директорию если она не существует
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
    def is_supported_file(self, file_path):
        """Проверка поддерживаемого расширения файла"""
        return Path(file_path).suffix.lower() in self.supported_extensions
        
    def get_file_info(self, file_path):
        """Получение информации о файле"""
        if not os.path.exists(file_path):
            return None
            
        stat = os.stat(file_path)
        return {
            'size': stat.st_size,
            'modified': stat.st_mtime,
            'created': stat.st_ctime
        }


