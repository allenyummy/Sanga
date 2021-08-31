# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Data structure

import json
import logging
from dataclasses import asdict, dataclass, field
from typing import List, Union

logger = logging.getLogger(__name__)


@dataclass
class NewsStruct:
    """News Data Structure"""

    title: str = field(
        default=None,
        metadata={"help": "News title."},
    )
    content: str = field(
        default=None,
        metadata={"help": "News content."},
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={"help": "News keywords."},
    )
    category: Union[str, List[str]] = field(
        default=None,
        metadata={"help": "News category."},
    )
    media: str = field(
        default=None,
        metadata={"help": "Media which releases news."},
    )
    datetime: str = field(
        default=None,
        metadata={"help": "Datetime in which news is released."},
    )
    link: str = field(
        default=None,
        metadata={"help": "News link."},
    )

    def __eq__(self, other) -> bool:
        return self.link == other.link

    def __repr__(self):
        return (
            "\n"
            f"[TITLE   ]: {self.title}\n"
            f"[CONTENT ]: {self.content}\n"
            f"[KEYWORDS]: {self.keywords}\n"
            f"[CATEGORY]: {self.category}\n"
            f"[MEDIA   ]: {self.media}\n"
            f"[DATETIME]: {self.datetime}\n"
            f"[LINK    ]: {self.link}\n"
        )

    def __2json__(self):
        return json.dumps(
            asdict(self),
            ensure_ascii=False,
            indent=4,
        )

    def __2dict__(self):
        return json.loads(self.__2json__())
