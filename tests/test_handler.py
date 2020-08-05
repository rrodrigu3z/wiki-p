import pytest
import wiki_p
import json
from handler import paragraphs


class TestHandler:
    def test_response(self, mocker):
        items = ["Hello", "World"]

        def paragraphs_mock(self):
            return items

        mocker.patch("wiki_p.WikiP.extract_paragraphs", paragraphs_mock)
        response = paragraphs({"title": "Hello_world"}, {})

        assert response["statusCode"] == 200
        assert response["body"] == json.dumps({"data": items})
