# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import yahoo
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
    name="Yahoo奇摩股市_1",
    link="https://tw.stock.yahoo.com/news/%E7%86%B1%E9%96%80%E6%97%8F%E7%BE%A4-%E5%A7%94%E5%A4%96%E8%A8%82%E5%96%AE%E6%97%BA-%E5%89%B5%E6%84%8F%E5%8A%9B%E6%97%BA%E6%A5%AD%E7%B8%BE%E8%A3%9C-234511435.html",
    expected_output=NewsStruct(
        title="《熱門族群》委外訂單旺 創意力旺業績補",
        content="【時報-台北電】新冠肺炎疫情加速全球數位轉型，資料中心及網路巨擘為了因應爆發成長的雲端及邊緣運算強勁需求，砸下鉅資投入開發5G高速網路、人工智慧（AI）、高效能運算（HPC）等客製化運算晶片。業者為了突破IC設計經驗不足困境，同時為了追上先進製程推進速度，今年開始擴大採用已獲矽驗證的第三方矽智財（IP），包括創意（3443）、智原（3035）、M31（6643）、力旺（3529）、晶心科（6533）等直接受惠，今年IP業務接單均創新高。包括微軟、亞馬遜AWS、Google、阿里巴巴、百度、騰訊等資料中心及網路巨擘，過去3年陸續公布開發自行研發的客製化特殊應用晶片（ASIC）計畫，然而去年下半年到今年中，晶片開發計畫已明顯停擺，業界指出主要原因網路大廠的IC設計經驗明顯不足，新晶片由開案到完成設計定案（tape-out）時程超過2年，明顯追不上先進製程推進速度。為加快客製化AI／HPC運算晶片開發，同時因應5G企業專網及開放式無線接取網路（O-RAN）的聯網架構轉換，資料中心及網路大廠開始釋出大量客製化ASIC委託設計（NRE）案件，如亞馬遜AWS的AI推論運算ASIC、Google新一代機器學習TPU等都完成NRE開案，並將採先進7奈米或5奈米製程投片，搭配台積電CoWoS等先進封裝技術。後疫情時代的數位轉型加速，網路大廠為了縮短5G、AI／HPC等客製化晶片開發時程，開始擴大採用已通過矽驗證的第三方IP，包括創意、智原、M31、力旺、晶心科等IP供應商直接受惠。由於客製化ASIC價格普遍來說都會比通用型運算晶片高出3～5倍，IP權利金普遍是以晶片或晶圓價格的一定比例收取，也讓業者今年IP相關收入屢創新高。此外，美中貿易衝突延續，中國大陸半導體產業鏈自製自銷晶片比重預料將長期穩定上升，然而在美國的圍堵政策下，中國網路大廠對於開發客製化ASIC更是砸錢毫不手軟，最關鍵的IP過去都向美國供應商取得授權，去年以來則大量採用台灣IP供應商方案。包括創意、M31、力旺、晶心科等都受惠於轉單效應發酵，第三季之後授權金及權利金將大幅認列，營收成長動能強勁，下半年旺季可期。（新聞來源：工商時報─記者涂志豪／台北報導）",
        keywords=["晶心科", "新冠肺炎疫情", "晶片"],
        category=None,
        media="Yahoo奇摩股市",
        datetime="2021-07-22T23:45:11.000Z",
        link="https://tw.stock.yahoo.com/news/%E7%86%B1%E9%96%80%E6%97%8F%E7%BE%A4-%E5%A7%94%E5%A4%96%E8%A8%82%E5%96%AE%E6%97%BA-%E5%89%B5%E6%84%8F%E5%8A%9B%E6%97%BA%E6%A5%AD%E7%B8%BE%E8%A3%9C-234511435.html",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="Yahoo奇摩新聞_1",
    link="https://tw.news.yahoo.com/%E5%85%AC%E5%8F%B8%E6%B2%BB%E7%90%86100%E6%8C%87%E6%95%B8-%E6%88%90%E5%88%86%E8%82%A1%E6%96%B0%E5%A2%9E32%E6%AA%94-115754553.html",
    expected_output=NewsStruct(
        title="公司治理100指數 成分股新增32檔",
        content="臺灣指數公司公布「公司治理100指數」成分股本年度定期審核結果，新納入的成分股計有嘉泥（1103）、伸興（1558）、岱宇（1598）、正隆（1904）、上銀（2049）、鴻海（2317）、旺宏（2337）、華邦電（2344）、宏碁（2353）、瑞昱（2379）、廣達（2382）、友達（2409）、超豐（2441）、陽明（2609）、聯邦銀（2838）、國票金（2889）、欣興（3037）、晶技（3042）、大量（3167）、景碩（3189）、創意（3443）、上緯投控（3708）、泰鼎-KY（4927）、崇越（5434）、工信（5521）、盛群（6202）、晶碩（6491）、和潤企業（6592）、緯穎（6669）、南電（8046）、至上（8112）、達方（8163）等32檔股票，這項審核結果將於7月19日生效。「公司治理100指數」於每年7月辦理定審，須經流動性檢驗、公司治理評鑑篩選、三項財務指標(每股淨值不低於面額、稅後淨利排名及營收成長率排名)等過程。「公司治理100指數」，係以在臺灣證券交易所掛牌的上市公司（含國內上市公司及外國企業第一上市公司，不含TDR），先刪除最近1年期間，日平均交易金額最小20%的股票；再將採樣母體內符合流動性檢驗標準的股票，選取符合「最近1年公司治理評鑑結果前20%」及「最近1年底的每股淨值不得低於面額」的股票，之後分別以「最近一年稅後淨利」及「最近一年營收成長率」進行排名，並將各別排名加總後由小至大排序，選取排名前100檔股票作為成分股，故並非「公司治理評鑑」為單一因素之排行榜。",
        keywords=["公司治理"],
        category=None,
        media="Yahoo奇摩新聞",
        datetime="2021-07-18T11:57:54.000Z",
        link="https://tw.news.yahoo.com/%E5%85%AC%E5%8F%B8%E6%B2%BB%E7%90%86100%E6%8C%87%E6%95%B8-%E6%88%90%E5%88%86%E8%82%A1%E6%96%B0%E5%A2%9E32%E6%AA%94-115754553.html",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return yahoo.Yahoo()


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
