import pytest
from wiki_p import WikiP


class PageMock:
    def __init__(self, title):
        self.title = title
        self.text = "<p>Hello</p> <p>World</p>"

    @staticmethod
    def exists():
        return True


@pytest.fixture
def page_mock(monkeypatch):
    def page(self, title):
        return PageMock(title)
    monkeypatch.setattr("wikipediaapi.Wikipedia.page", page)


class TestWikiP:
    def test_title(self, page_mock):
        parser = WikiP("Hello")
        assert parser.page.title == "Hello"

    def test_is_valid(self, page_mock):
        parser = WikiP("Hello")
        assert parser.is_valid == True

    def test_extract_paragraphs(self, page_mock):
        parser = WikiP("Hello")
        paragraphs = parser.extract_paragraphs()
        expected = [
            {"paragraph": "Hello"},
            {"paragraph": "World"}
        ]
        assert paragraphs == expected
