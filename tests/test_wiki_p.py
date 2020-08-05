import pytest
from wiki_p import WikiP


class MockPage:
    def __init__(self, title):
        self.title = title
        self.text = "<p>Hello</p> <p>World</p>"


class TestHandler:
    def test_extract_paragraphs(self, mocker):
        def page_mock(self, title):
            return MockPage(title)

        mocker.patch("wikipediaapi.Wikipedia.page", page_mock)
        parser = WikiP("Hello")
        paragraphs = parser.extract_paragraphs()

        assert parser.page.title == "Hello"
        assert paragraphs == ["Hello", "World"]
