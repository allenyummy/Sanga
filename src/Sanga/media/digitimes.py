# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class DigiTimes(BaseMediaNewsCrawler):
    """Web Crawler for DigiTimes News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find_all("p", class_="main_p")
        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
