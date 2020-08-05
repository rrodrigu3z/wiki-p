import json
from wiki_p import WikiP


def paragraphs(event, context):
    parser = WikiP(event["title"])
    body = {"data": parser.extract_paragraphs()}

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
