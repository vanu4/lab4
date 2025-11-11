import pytest
from app import TextUtils

class TestTextUtils:
    def setup_method(self):
        self.utils = TextUtils()

    @pytest.mark.parametrize("text,expected", [
        ("Привет мир", 2),
        ("   Один    два три  ", 3),
        ("", 0)
    ])
    def test_count_words(self, text, expected):
        assert self.utils.count_words(text) == expected

    def test_reverse_text(self):
        assert self.utils.reverse_text("abc") == "cba"
        assert self.utils.reverse_text("12345") == "54321"

    def test_is_palindrome(self):
        assert self.utils.is_palindrome("топот") is True
        assert self.utils.is_palindrome("Казак") is True
        assert self.utils.is_palindrome("Привет") is False

    def test_to_upper(self):
        assert self.utils.to_upper("test") == "TEST"
        assert self.utils.to_upper("TeSt") == "TEST"

    def test_remove_spaces(self):
        assert self.utils.remove_spaces("a b c") == "abc"
        assert self.utils.remove_spaces("   hello world   ") == "helloworld"
