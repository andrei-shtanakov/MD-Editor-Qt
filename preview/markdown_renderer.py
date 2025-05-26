"""
Конвертация Markdown в HTML (заготовка для будущего развития)
"""
try:
    import markdown
    MARKDOWN_AVAILABLE = True
except ImportError:
    MARKDOWN_AVAILABLE = False

class MarkdownRenderer:
    def __init__(self):
        if MARKDOWN_AVAILABLE:
            self.md = markdown.Markdown(extensions=['extra', 'codehilite'])
        else:
            self.md = None
            
    def render(self, markdown_text):
        """Конвертация markdown в HTML"""
        if self.md:
            return self.md.convert(markdown_text)
        else:
            # Простая заглушка если markdown не установлен
            return f"<pre>{markdown_text}</pre>"

