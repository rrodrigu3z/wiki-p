"""Lambda function for extract paragraphs from a Wikipedia page"""

import json
from wiki_p import WikiP


def paragraphs(event, context): # pylint: disable=unused-argument
    """Handles HTTP request and returns paragraphs"""
    parser = WikiP(event["title"])
    body = {"data": parser.extract_paragraphs()}

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
