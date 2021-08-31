# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class TVBS(BaseMediaNewsCrawler):
    """Web Crawler for TVBS News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", itemprop="articleBody").text

        for script in soup.find("div", itemprop="articleBody").find_all("script"):
            if script.text in content:
                content = content.replace(script.text, "")

        # Ad changes over time in the same page.
        # It'll cause error during tests.
        # So I have to remove it from content
        ad = soup.find("div", class_="guangxuan").find("strong").text
        idx = content.find(ad)
        content = content[:idx]
        logger.debug(f"CONTENT:\n {content}")
        return content
