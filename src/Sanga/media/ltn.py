# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class LTN(BaseMediaNewsCrawler):
    """Web Crawler for LTN News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content_list = list()
        for c in soup.find("div", class_="text").find_all("p"):
            if c.has_attr("class"):
                continue
            content_list.append(c)

        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}\n")
        return content
