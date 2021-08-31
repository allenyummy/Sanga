# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class CTV(BaseMediaNewsCrawler):
    """Web Crawler for CTV News"""

    def getInfo(self, link: str) -> NewsStruct:
        raise NotImplementedError

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        raise NotImplementedError
