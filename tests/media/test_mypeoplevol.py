# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import mypeoplevol
from Sanga.struct import NewsStruct

logger = logging.getLogger(__name__)


TEST_DATA = namedtuple(
    typename="TEST_DATA",
    field_names=[
        "name",
        "link",
        "expected_output",
    ],
)

TEST_DATA_1 = TEST_DATA(
    name="民眾新聞網_1",
    link="https://www.mypeoplevol.com/Article/3493",
    expected_output=NewsStruct(
        title="民眾網 - 聯電調漲晶圓代工價 預計平均調漲10%以上",
        content=" 【民眾網綜合報導】 近日半導體市場消息傳出，聯電(2303)將在Q4再度調漲晶圓代工價格，平均調漲幅度約在10%上下，對於聯電Q4營收而言是個絕佳利多的好消息，產能滿載又逐季調高價格，可望使聯電今年獲利再創新高。 供應鏈傳出，聯電近期向客戶發出調升晶圓代工價格通知，11月平均帳價10%，部分製程漲15%。在漲價效益的催動下，法人看好聯電營收、毛利率以及稅後純益都有望持續創高。 對於漲價消息，聯電於昨(16)日回應表示，不評論市場傳聞。而昨日聯電收盤股價下跌0.5元，收在57.1元，外資大買超過1.8萬張終止連續兩日的賣超。 聯電目前接單持續滿載，7月營收達183.66億元，較6月再增加5.9%，連續3個月營收創歷史新高。公司也看好第3季營收再創新高。 聯電日前於法說會表示，Q3需求仍然強勁，包括8吋及12吋晶圓代工整體供給吃緊情況將會持續，產能利用率將維持100%。 聯電預期整體Q3晶圓出貨量將增加1%至2%，產品平均售價將上升6個百分點，毛利率將上升至35%。以此推估，聯電Q3營收將季增約7%至8%，將續創單季營收歷史新高。 另外，聯電預估今年調漲價格幅度大約在13%。日前於法說會上表示將上修今年全年平均銷售價格(ASP)預估幅度，由年增10%調高到10%至13%，訂單能見度也已看到明年底，受惠成熟製程產能供不應求，價格持續調漲，帶動聯電上修ASP增幅。  圖片來源：聯華電子股份有限公司 更多新聞：大陸5G基建、漲價題材燒 銅箔基板三雄毛利向上 ",
        keywords=None,
        category=None,
        media="民眾新聞網",
        datetime="2021-08-17T11:31:51Z",
        link="https://www.mypeoplevol.com/Article/3493",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="民眾新聞網_2",
    link="https://www.mypeoplevol.com/Article/3485",
    expected_output=NewsStruct(
        title="民眾網 - 宅經濟退燒？Chromebook筆電大砍單 產業前景堪憂",
        content=" 【民眾網綜合報導】 因疫情而起的宅經濟題材而受惠的Chromebook筆電銷售潮，近日傳出許多國際品牌大廠包含聯想、惠普、戴爾等對零組件供應商大砍單，砍單幅度高達兩成，總量超過1,000萬台。法人表示擔心這將是銷售大爆發告終的可能跡象，將牽動台灣Chromebook相關供應鏈的出貨情形，可能受影響的名單有創惟(6104)、義隆(2458)、聯詠(3034)、友達(2409)、群創(3481)。 Chromebook是搭載Google作業系統的輕量級筆電，以學生為主要客群。由於疫情帶來遠距教學潮，Chromebook成為學生在家上課必備的配件而大熱賣。 研調機構IDC表示，Chromebook去年出貨量大增至3,250萬台，較2019年的1,670萬台幾乎翻倍成長，寫下Google從2011年開始向聯想、惠普、戴爾、宏碁(2353)和華碩(2357)等PC業者授權以來的最快成長幅度。 然而，在疫情蔓延近二年之後，多數學生已添購在家上課的硬體，導致Chromebook銷售熱潮退去。  圖片來源：惠普官方網站 更多新聞：新唐晶圓代工價漲15% 早盤強勢填息 ",
        keywords=None,
        category=None,
        media="民眾新聞網",
        datetime="2021-08-17T10:33:29Z",
        link="https://www.mypeoplevol.com/Article/3485",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return mypeoplevol.MyPeopleVol()


@pytest.mark.parametrize(
    argnames="name, link, expected_output",
    argvalues=[tuple(t) for t in TEST_DATA_LIST],
    ids=[
        f"{t.name}, {t.link[:50]+'...' if len(t.link) > 50 else t.link}"
        for t in TEST_DATA_LIST
    ],
)
def test_get_info(
    newsCrawler,
    name,
    link,
    expected_output,
):
    output = newsCrawler.getInfo(link=link)
    assert NewsStruct.__2dict__(output) == NewsStruct.__2dict__(expected_output)
