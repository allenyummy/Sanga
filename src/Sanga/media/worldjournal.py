# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class WorldJournal(BaseMediaNewsCrawler):
    """Web Crawler for WorldJournal News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        paragrah = soup.find("div", class_="article-content__paragraph")

        content_list = list()
        for content_cand in paragrah.find_all("p"):
            if content_cand.text in ["上一則", "下一則"]:
                continue
            content_list.append(content_cand)

        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
