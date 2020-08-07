import pytest
import json
from handler import paragraphs


@pytest.fixture
def parapgraps_mock(monkeypatch):
    def paragraphs(self):
        return [{"paragraph": "Hello"}, {"paragraph": "World"}]
    monkeypatch.setattr("wiki_p.WikiP.extract_paragraphs", paragraphs)


@pytest.fixture
def body():
    return {"title": "Hello_world"}


class TestHandler:
    def test_response_code(self, body, parapgraps_mock):
        response = paragraphs(body, {})
        assert response["statusCode"] == 200

    def test_response_body(self, body, parapgraps_mock):
        response = paragraphs(body, {})
        items = [{"paragraph": "Hello"}, {"paragraph": "World"}]
        assert response["body"] == json.dumps({"data": items})

    def test_cors_headers(self, body, parapgraps_mock):
        response = paragraphs(body, {})
        assert response["headers"] == {"Access-Control-Allow-Origin": "*"}
