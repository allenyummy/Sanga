# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, Union

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class ERACOM(BaseMediaNewsCrawler):
    """Web Crawler for ERACOM News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_datetime(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        datetime = soup.find("span", class_="time").text
        logger.debug(f"DATETIME: {datetime}")
        return datetime

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("div", class_="article-main").text
        logger.debug(f"CONTENT:\n {content}")
        return content
