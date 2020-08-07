"""Wikipedia paragraph parser classes."""

from wikipediaapi import Wikipedia, ExtractFormat
from bs4 import BeautifulSoup


class WikiP:
    """Implements Wikipedia paragraph parser / extraction"""

    def __init__(self, title, lang="en"):
        api = self._wiki_api(lang)
        self.page = api.page(title)

    @property
    def is_valid(self):
        """Returns True if `page` exists, otherwise returns False"""
        return self.page.exists()

    def extract_paragraphs(self):
        """Extract paragraphs from the page

        Returns:
            list: collection of paragraphs

            Example output::

                [
                    {"paragraph": "this is a paragraph"},
                    {"paragraph": "this is another paragraph"}
                ]

        """
        soup = BeautifulSoup(self.page.text, "html.parser")
        paragraphs = [self._format_p(p.text) for p in soup.find_all("p")]
        return list(filter(lambda p: p["paragraph"], paragraphs))

    @staticmethod
    def _format_p(text):
        return {"paragraph": text.strip()}

    @staticmethod
    def _wiki_api(lang):
        return Wikipedia(
            language=lang,
            extract_format=ExtractFormat.HTML)
