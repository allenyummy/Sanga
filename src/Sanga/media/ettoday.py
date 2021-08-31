# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class ETtoday(BaseMediaNewsCrawler):
    """Web Crawler for ETtoday News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find("div", class_="story").find_all("p")
        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}\n")
        return content
