# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Get news

import json
import logging
from typing import Dict, List, Union

from bs4 import BeautifulSoup

from .base import BaseMediaNewsCrawler
from ..struct import NewsStruct

logger = logging.getLogger(__name__)


class CTEE(BaseMediaNewsCrawler):
    """Web Crawler for CTEE News"""

    def getInfo(self, link: str) -> NewsStruct:
        return super().getInfo(link)

    @staticmethod
    def _get_script_info(
        soup: BeautifulSoup,
    ) -> Dict[str, str]:

        # use 4-th element (0-indexed)
        script_info_str = soup.find_all("script", type="application/ld+json")[3].string
        script_info_dict = json.loads(script_info_str)
        logger.debug(f"SCRIPT_INFO_STR:\n" f"{script_info_str}")
        logger.debug(f"SCRIPT_INFO_DICT:\n" f"{script_info_dict}")

        # keywords not in script_info_dict but in soup.
        # I don't get them. I just let them go because it's a special case.
        # Maybe after a while, I'll figure out how to resolve it in an elegant way.
        return script_info_dict

    @staticmethod
    def _get_keywords(
        script_info: Dict[str, str],
        soup: BeautifulSoup,
    ) -> Union[List[str], None]:

        keywords_list = soup.find_all("a", rel="tag")
        keywords = [k.text for k in keywords_list]
        logger.debug(f"KEYWORDS: {keywords}")
        return keywords

    @staticmethod
    def _get_content(
        soup: BeautifulSoup,
    ) -> str:

        content_list = soup.find(
            "div", class_="entry-content clearfix single-post-content"
        ).find_all("p")
        content = "\n".join([c.text for c in content_list])
        logger.debug(f"CONTENT:\n {content}")
        return content
