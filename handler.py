"""Lambda function for extract paragraphs from a Wikipedia page"""

import json
from wiki_p import WikiP


def paragraphs(event, context):  # pylint: disable=unused-argument
    """Handles HTTP request and returns paragraphs"""
    body = json.loads(event["body"])
    parser = WikiP(body["title"])
    body = {"data": parser.extract_paragraphs()}
    headers = {"Access-Control-Allow-Origin": "*"}

    return {
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps(body)
    }
