import pytest
import json
from handler import paragraphs


@pytest.fixture
def parapgraps_mock(monkeypatch):
    def paragraphs(self):
        return [{"paragraph": "Hello"}, {"paragraph": "World"}]
    monkeypatch.setattr("wiki_p.WikiP.extract_paragraphs", paragraphs)


class TestHandler:
    def test_response_code(self, parapgraps_mock):
        response = paragraphs({"title": "Hello_world"}, {})
        assert response["statusCode"] == 200

    def test_response_body(self, parapgraps_mock):
        response = paragraphs({"title": "Hello_world"}, {})
        items = [{"paragraph": "Hello"}, {"paragraph": "World"}]
        assert response["body"] == json.dumps({"data": items})
