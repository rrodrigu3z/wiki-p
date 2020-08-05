from wikipediaapi import Wikipedia, ExtractFormat
from bs4 import BeautifulSoup

class WikiP:
    def __init__(self, title, lang="en"):
        api = self._wiki_api(lang)
        self.page = api.page(title)

    def extract_paragraphs(self):
        soup = BeautifulSoup(self.page.text, "html.parser")
        return [p.text for p in soup.find_all("p")]

    def _wiki_api(self, lang):
        return Wikipedia(
            language=lang,
            extract_format=ExtractFormat.HTML)
