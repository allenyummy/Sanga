# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import tvbs
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
    name="TVBS_1",
    link="https://news.tvbs.com.tw/money/1566997",
    expected_output=NewsStruct(
        title="台塑集團拍板加薪3.83%　再發1萬元慰勉金│TVBS新聞網",
        content="\n\n\n台塑集團今天舉行年度調薪會議，總裁王文淵拍板今年加薪幅3.83%，並加碼發出新台幣1萬元慰勉金；若以去年台塑基層員工平均薪資5萬4800元來看，每月薪水增加2100元。台塑集團年度調薪今天定案，台塑集團總裁王文淵拍板員工加薪3.83%，同時發出1萬元慰勉金，本次加薪會回溯至7月1日生效。\n\n\n\n\n\n\n\n&nbsp工會代表指出，若以台塑集團基層員工去年平均薪資約5萬4800元來看，每月薪水增加2100元，若算上加碼的紅包，整體加薪幅度達5.33%。工會代表轉述，王文淵會中提到，美中貿易紛爭未解，石化景氣易受到經濟、地緣政治影響，且未來通貨膨脹恐日益嚴峻，加上Delta變種病毒蔓延全球，後市仍須密切關注疫情狀況，對下半年審慎看待。工會原先爭取加薪4.5%、相當每月增加逾2400元，實質薪幅度略低於工會期待。不過，工會代表指出，王文淵認為今年度加薪應以去年業績為依據，且總管理處原擬發放6000元慰勉金，王文淵另外加碼4000元、至1萬元。工會表示，能夠體恤公司辛勞，盼下半年不要再受疫情影響，獲利、營收能創佳績，屆時工會將為員工爭取更佳年終獎金。（中央社）",
        keywords=["台塑", "加薪", "基層員工", "薪水", "台塑集團"],
        category="理財房地產",
        media="TVBS",
        datetime="2021/08/17 14:20",
        link="https://news.tvbs.com.tw/money/1566997",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="TVBS_2",
    link="https://news.tvbs.com.tw/politics/1567072",
    expected_output=NewsStruct(
        title="軍公教待遇明年是否調整？　政院：綜合考量後決定│TVBS新聞網",
        content="\n\n\n行政院官員今天表示，關於明年軍公教待遇是否調整，行政院將經綜合考量後，待定案再對外說明。「軍公教員工待遇審議委員會」每年都會就政府財政狀況、消費者物價指數變動情形、平均每人國民所得、經濟成長率及民間企業薪資水準等指標進行討論，並向行政院提出政策建議。\n\n\n\n\n\n\n\n&nbsp行政院人事行政總處人事長施能傑今天對中央社記者表示，軍公教員工待遇審議委員會已依程序開會完成，並將意見簽給行政院做決定。據了解，軍公教員工待遇審議委員會的討論意見，主要是就整體疫情考量做出建議。政院官員則表示，行政院將經綜合考量後再做出最後決定，定案後一併對外說明。根據行政院人事行政總處資料顯示，軍公教在民國88年以前幾乎年年加薪，但其後只有在90年、94年、100年、107年調薪，幅度皆為3%。全國教師工會總聯合會（全教總）今天質疑，行政院人事總處13日「偷偷摸摸」召開薪資委員會，決議明年軍公教不調薪，會中完全沒有基層代表，只能照行政院的說法去做結論。全教總表示，軍公教調薪「是權利，不是施捨；是尊嚴，不是工具」。呼籲政府參考經濟成長率、民間企業薪資成長、物價指數、重要民生物資指數等數據，不要拿其他無關的事由推卸責任。（中央社）\n\n\n\n\n\n\n\n&nbsp",
        keywords=["軍公教", "行政院", "人事總處", "疫情", "調薪"],
        category="要聞",
        media="TVBS",
        datetime="2021/08/17 15:45",
        link="https://news.tvbs.com.tw/politics/1567072",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return tvbs.TVBS()


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
