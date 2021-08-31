# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class MirrorMedia(BaseMediaNewsCrawler):
    """Web Crawler for MirrorMedia News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find_all("p", class_="g-story-paragraph")
        content = "\n".join([s.text for s in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
