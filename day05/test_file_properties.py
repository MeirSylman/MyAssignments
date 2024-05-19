import pytest
from count_2 import characters_count, lines_count, words_count


def test_characters_count():
    content = "Hello World\nThis is a test file."
    assert characters_count(content) == 32


def test_lines_count():
    content = "Hello World\nThis is a test file."
    assert lines_count(content) == 2


def test_words_count():
    content = "Hello World\nThis is a test file."
    assert words_count(content) == 7



