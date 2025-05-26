"""
Основное окно приложения
"""
from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, 
                            QMenuBar, QStatusBar, QMessageBox, QFileDialog)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QAction, QKeySequence
from editor.text_editor import MarkdownTextEditor
from file_manager.file_operations import FileManager

class MainWindow(QMainWindow):
    def __init__(self, state_manager):
        super().__init__()
        self.state_manager = state_manager
        self.file_manager = FileManager()
        self.current_file_path = None
        
        self.init_ui()
        self.setup_menu()
        self.setup_shortcuts()
        self.setup_connections()
        
    def init_ui(self):
        self.setWindowTitle("Markdown Editor")
        self.setGeometry(100, 100, 1000, 700)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Основной layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Текстовый редактор
        self.text_editor = MarkdownTextEditor()
        layout.addWidget(self.text_editor)
        
        # Строка состояния
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Готов")
        
    def setup_menu(self):
        menubar = self.menuBar()
        
        # Меню Файл
        file_menu = menubar.addMenu("Файл")
        
        # Новый файл
        new_action = QAction("Новый", self)
        new_action.setShortcut(QKeySequence.StandardKey.New)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        # Открыть файл
        open_action = QAction("Открыть", self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        # Сохранить файл
        save_action = QAction("Сохранить", self)
        save_action.setShortcut(QKeySequence.StandardKey.Save)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        # Сохранить как
        save_as_action = QAction("Сохранить как...", self)
        save_as_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        # Выход
        exit_action = QAction("Выход", self)
        exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Меню Правка
        edit_menu = menubar.addMenu("Правка")
        
        undo_action = QAction("Отменить", self)
        undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        undo_action.triggered.connect(self.text_editor.undo)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction("Повторить", self)
        redo_action.setShortcut(QKeySequence.StandardKey.Redo)
        redo_action.triggered.connect(self.text_editor.redo)
        edit_menu.addAction(redo_action)
        
    def setup_shortcuts(self):
        pass  # Дополнительные горячие клавиши можно добавить здесь
        
    def setup_connections(self):
        # Подключение сигналов
        self.text_editor.textChanged.connect(self.on_text_changed)
        
    def new_file(self):
        if self.check_unsaved_changes():
            self.text_editor.clear()
            self.current_file_path = None
            self.update_window_title()
            self.status_bar.showMessage("Новый файл создан")
            
    def open_file(self):
        if self.check_unsaved_changes():
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Открыть файл",
                "",
                "Markdown files (*.md *.markdown);;All files (*.*)"
            )
            
            if file_path:
                try:
                    content = self.file_manager.load_file(file_path)
                    self.text_editor.setPlainText(content)
                    self.current_file_path = file_path
                    self.update_window_title()
                    self.status_bar.showMessage(f"Файл открыт: {file_path}")
                except Exception as e:
                    QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл: {str(e)}")
                    
    def save_file(self):
        if self.current_file_path:
            try:
                content = self.text_editor.toPlainText()
                self.file_manager.save_file(self.current_file_path, content)
                self.text_editor.document().setModified(False)
                self.status_bar.showMessage(f"Файл сохранен: {self.current_file_path}")
                self.update_window_title()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")
        else:
            self.save_file_as()
            
    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить файл как",
            "",
            "Markdown files (*.md);;All files (*.*)"
        )
        
        if file_path:
            try:
                content = self.text_editor.toPlainText()
                self.file_manager.save_file(file_path, content)
                self.current_file_path = file_path
                self.text_editor.document().setModified(False)
                self.update_window_title()
                self.status_bar.showMessage(f"Файл сохранен: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {str(e)}")
                
    def check_unsaved_changes(self):
        if self.text_editor.document().isModified():
            reply = QMessageBox.question(
                self,
                "Несохраненные изменения",
                "Файл был изменен. Сохранить изменения?",
                QMessageBox.StandardButton.Save | 
                QMessageBox.StandardButton.Discard | 
                QMessageBox.StandardButton.Cancel
            )
            
            if reply == QMessageBox.StandardButton.Save:
                self.save_file()
                return True
            elif reply == QMessageBox.StandardButton.Discard:
                return True
            else:
                return False
        return True
        
    def on_text_changed(self):
        self.update_window_title()
        
    def update_window_title(self):
        title = "Markdown Editor"
        if self.current_file_path:
            title += f" - {self.current_file_path}"
        if self.text_editor.document().isModified():
            title += " *"
        self.setWindowTitle(title)
        
    def closeEvent(self, event):
        if self.check_unsaved_changes():
            event.accept()
        else:
            event.ignore()

