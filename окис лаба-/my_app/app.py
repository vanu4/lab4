class TextUtils:
    def count_words(self, text):
        """Возвращает количество слов в строке"""
        words = text.strip().split()
        return len(words)

    def reverse_text(self, text):
        """Переворачивает строку"""
        return text[::-1]

    def is_palindrome(self, text):
        """Проверяет, является ли строка палиндромом"""
        cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]

    def to_upper(self, text):
        """Преобразует все символы в верхний регистр"""
        return text.upper()

    def remove_spaces(self, text):
        """Удаляет все пробелы из строки"""
        return text.replace(' ', '')
