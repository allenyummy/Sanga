# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict

from bs4 import BeautifulSoup

# from src.config import MEDIA_URL
from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class CNYES(BaseMediaNewsCrawler):
    """Web Crawler for CNYES News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_title(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> str:

        title = soup.find(itemprop="headline").text
        logger.debug(f"TITLE: {title}")
        return title

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content = soup.find(class_="_2E8y").text
        logger.debug(f"CONTENT:\n {content}\n")
        return content
