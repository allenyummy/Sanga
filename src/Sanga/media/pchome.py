# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, Union

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class PChome(BaseMediaNewsCrawler):
    """Web Crawler for NowNews News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_category(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        category = soup.find("div", class_="breadcrumb_wrap").find_all("a")
        category = [c.text for c in category]
        logger.debug(f"CATEGORY: {category}")
        return category

    @staticmethod
    def _get_datetime(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        datetime = soup.find("time").get("datetime")
        logger.debug(f"DATETIME: {datetime}")
        return datetime

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", calss="article_text").text
        logger.debug(f"CONTENT:\n {content}")
        return content
