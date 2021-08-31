# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class NowNews(BaseMediaNewsCrawler):
    """Web Crawler for NowNews News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("article", itemprop="articleBody").text
        related = soup.find("ul", class_="related").text
        idx = content.find(related)
        content = content[:idx]
        logger.debug(f"CONTENT:\n {content}")
        return content
