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


class UDN(BaseMediaNewsCrawler):
    """Web Crawler for UDN News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # list of dictionary
        script_info_str = soup.find("script", type="application/ld+json").string

        # use first element (0-indexed)
        script_info_dict = json.loads(script_info_str)[0]
        logger.debug(f"SCRIPT_INFO_STR:\n {script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n {script_info_dict}")
        return script_info_dict

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find("section", class_="article-content__editor").find_all(
            "p"
        )
        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
