# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict, Union

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class BCC(BaseMediaNewsCrawler):
    """Web Crawler for BCC News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_datetime(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[str, None]:

        datetime = None
        if soup.find("div", class_="tt27"):
            datetime = soup.find("div", class_="tt27").text

        logger.debug(
            f"DATETIME: {datetime}"
            f"{'. Found it because soup has `<div class=tt27>`.' if datetime else ''}"
        )

        return datetime

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find("spand", id="sizectl").text
        logger.debug(f"CONTENT:\n {content}")
        return content
