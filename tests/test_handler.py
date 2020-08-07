import pytest
import json
from handler import paragraphs


@pytest.fixture
def parapgraps_mock(monkeypatch):
    def paragraphs(self):
        return [{"paragraph": "Hello"}, {"paragraph": "World"}]
    monkeypatch.setattr("wiki_p.WikiP.extract_paragraphs", paragraphs)


@pytest.fixture
def event():
    return {"body": json.dumps({"title": "Hello_world"})}


class TestHandler:
    def test_response_code(self, event, parapgraps_mock):
        response = paragraphs(event, {})
        assert response["statusCode"] == 200

    def test_response_body(self, event, parapgraps_mock):
        response = paragraphs(event, {})
        items = [{"paragraph": "Hello"}, {"paragraph": "World"}]
        assert response["body"] == json.dumps({"data": items})

    def test_cors_headers(self, event, parapgraps_mock):
        response = paragraphs(event, {})
        assert response["headers"] == {"Access-Control-Allow-Origin": "*"}
