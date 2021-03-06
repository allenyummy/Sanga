# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import ettoday
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
    name="ETtoday新聞雲_1",
    link="https://www.ettoday.net/news/20210720/2035771.htm",
    expected_output=NewsStruct(
        title="東元股東會前夕再出招　黃育仁旗下兩公司光菱、東友明停牌",
        content="\n▲菱光董座黃育仁。（圖／記者陳心怡攝）\n記者陳心怡／台北報導\n光菱 (8032) 與東友 (5438) 今 (20) 日傍晚同步公告，因有重大事項待公布，經櫃買中心同意明 (21) 日暫停交易。由於兩家公司大股東均為菱光，也是東元集團會長黃茂雄兒子黃育仁主導的公司，兩家公司是否進行換股、策略合作，引發外界關注，同時也被視為可能是黃育仁的反撲。\n東元電機（1504）股東會23日登場前，東元黃家黃茂雄、黃育仁父子之爭越演越烈。黃育仁旗下的3家公司，包括上市的菱光科技，上櫃的東友科技和光菱電子，黃茂雄先前結合創投達勝伍成立鈺叡，要收購菱光過半股權；7月初，黃茂雄主導成立的安富國際投宣布要以6.14億元，公開收購東友30%股權。\n不過黃育仁近期頻出招，更讓兩家公司明天同時停牌，外界預料黃育仁可能再出招，確保在兩家公司的掌控能力，對抗東元勢力。",
        keywords=["東元", "黃育仁", "黃茂雄"],
        category="財經",
        media="ETtoday新聞雲",
        datetime="2021-07-20T20:21:00+08:00",
        link="https://www.ettoday.net/news/20210720/2035771.htm",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="ETtoday財經雲_1",
    link="https://finance.ettoday.net/news/1929335",
    expected_output=NewsStruct(
        title="外資上周賣超938億元　聯電、台積電淪提款機",
        content="\n▲聯電、台積電上週成為外資提款機。（圖／路透社）\n記者陳心怡／台北報導\n根據證交所公布上周外資買賣超狀況，上周外資賣超938.45億元，今年以來累計賣超為1,931億元，外資總持有股票市值為22兆2,981.33億元新台幣，占全體上市股票市值的45.88%，較2月19日的23兆4,521.50億元新台幣，減少11,540.17億元。\n就個股比較部分，外資外資賣超前三名則為聯電（2303）16萬5910張，台積電（2330）8萬8182張，新光金（2888）5萬3488張。\n賣超四到十名分別為，佳格（1227）3萬4063張、長榮航（2618）3萬3858張、和碩（4938）2萬8592張、兆豐金（2886）2萬5131張、鴻海（2317）2萬4052張、精英（2331）1萬8523張、旺宏（2337）1萬8322張。\n另外，外資買超前三名分別是華航（2610）、友達（2409）、華邦電（2344），華航買超6萬7486張，友達買超5萬5519張，華邦電則是買超5萬4734張。\n買超四到十名分別為，中信金（2891）4萬1761張、陽明（2609）2萬9584張、遠東新（1402）2萬2187張、榮成（1909）1萬7634張、永豐金（2890）1萬5470張、華南金（2880）1萬2961張、台塑（1301）1萬2933張。",
        keywords=[],
        category="財經",
        media="ETtoday財經雲",
        datetime="2021-03-02T15:52:00+08:00",
        link="https://finance.ettoday.net/news/1929335",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return ettoday.ETtoday()


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
