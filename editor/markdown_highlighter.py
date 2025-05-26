"""
Подсветка синтаксиса Markdown
"""
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter

class MarkdownHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []
        self.setup_rules()
        
    def setup_rules(self):
        # Заголовки
        header_format = QTextCharFormat()
        header_format.setForeground(QColor("#2E86C1"))  # Синий
        header_format.setFontWeight(QFont.Weight.Bold)
        
        # H1-H6
        for i in range(1, 7):
            pattern = QRegularExpression(f"^#{{{i}}}\\s+.*")
            self.highlighting_rules.append((pattern, header_format))
            
        # Жирный текст
        bold_format = QTextCharFormat()
        bold_format.setFontWeight(QFont.Weight.Bold)
        bold_format.setForeground(QColor("#D35400"))  # Оранжевый
        bold_pattern = QRegularExpression(r"\*\*([^*]+)\*\*")
        self.highlighting_rules.append((bold_pattern, bold_format))
        
        # Курсив
        italic_format = QTextCharFormat()
        italic_format.setFontItalic(True)
        italic_format.setForeground(QColor("#8E44AD"))  # Фиолетовый
        italic_pattern = QRegularExpression(r"\*([^*]+)\*")
        self.highlighting_rules.append((italic_pattern, italic_format))
        
        # Код (инлайн)
        inline_code_format = QTextCharFormat()
        inline_code_format.setForeground(QColor("#E74C3C"))  # Красный
        inline_code_format.setBackground(QColor("#F8F9FA"))  # Светло-серый фон
        inline_code_format.setFontFamily("Consolas")
        inline_code_pattern = QRegularExpression(r"`([^`]+)`")
        self.highlighting_rules.append((inline_code_pattern, inline_code_format))
        
        # Блоки кода
        code_block_format = QTextCharFormat()
        code_block_format.setForeground(QColor("#E74C3C"))
        code_block_format.setBackground(QColor("#F8F9FA"))
        code_block_format.setFontFamily("Consolas")
        code_block_pattern = QRegularExpression(r"^```.*")
        self.highlighting_rules.append((code_block_pattern, code_block_format))
        
        # Ссылки
        link_format = QTextCharFormat()
        link_format.setForeground(QColor("#3498DB"))  # Голубой
        link_format.setUnderlineStyle(QTextCharFormat.UnderlineStyle.SingleUnderline)
        link_pattern = QRegularExpression(r"\[([^\]]+)\]\(([^)]+)\)")
        self.highlighting_rules.append((link_pattern, link_format))
        
        # Списки
        list_format = QTextCharFormat()
        list_format.setForeground(QColor("#27AE60"))  # Зеленый
        list_format.setFontWeight(QFont.Weight.Bold)
        list_pattern = QRegularExpression(r"^[\s]*[-*+]\s+")
        self.highlighting_rules.append((list_pattern, list_format))
        
        # Нумерованные списки
        numbered_list_pattern = QRegularExpression(r"^[\s]*\d+\.\s+")
        self.highlighting_rules.append((numbered_list_pattern, list_format))
        
        # Цитаты
        quote_format = QTextCharFormat()
        quote_format.setForeground(QColor("#7F8C8D"))  # Серый
        quote_format.setFontItalic(True)
        quote_pattern = QRegularExpression(r"^>\s+.*")
        self.highlighting_rules.append((quote_pattern, quote_format))
        
    def highlightBlock(self, text):
        # Применяем все правила подсветки
        for pattern, format_obj in self.highlighting_rules:
            iterator = pattern.globalMatch(text)
            while iterator.hasNext():
                match = iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format_obj)


