# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import logging
from typing import Dict
import json

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class TheNewsLens(BaseMediaNewsCrawler):
    """Web Crawler for TheNewsLens News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # use 3-rd element (0-indexed)
        script_info_str = soup.find_all("script", type="application/ld+json")[3].string
        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_STR:\n {script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        whyneedknow = soup.find("header", class_="WhyNeedKnow").find("p").text
        content = soup.find("article", itemprop="articleBody").text
        for script in soup.find("article", itemprop="articleBody").find_all("script"):
            if script.text in content:
                content = content.replace(script.text, "")
        content = whyneedknow + "\n" + content
        logger.debug(f"CONTENT:\n {content}")
        return content
