# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import eracom
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
    name="年代新聞_1",
    link="https://www.eracom.com.tw/EraNews/Home/Entertainment/2021-08-17/544662.html",
    expected_output=NewsStruct(
        title="捲性侵醜聞！ 中國正式逮捕吳亦凡　律師分析：有犯罪證據",
        content="男星吳亦凡先前爆出「酒桌選妃」，還侵犯未成年女孩，不僅遭全面封殺，上個月底更已經被中國警方刑事拘留，16日晚間北京人民檢察院指出，經過依法審查，決定批准以性侵罪嫌逮捕吳亦凡，有中國律師分析，這表示有證據證明犯罪事實，而且其罪刑至少會判處徒刑以上的刑罰。",
        keywords=["吳亦凡", "酒桌選妃", "性疑雲", "封殺", "中國", "北京人民檢察院", "性侵罪", "逮捕"],
        category=None,
        media="年代新聞",
        datetime="2021-08-17 14:01",
        link="https://www.eracom.com.tw/EraNews/Home/Entertainment/2021-08-17/544662.html",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="年代新聞_2",
    link="https://www.eracom.com.tw/EraNews/Home/Finance/2021-08-16/544573.html",
    expected_output=NewsStruct(
        title="EUA未通過！ 聯亞藥股價「跳水式下跌」 收盤跌逾30%",
        content="國產疫苗進度備受關注，今（16）日疫情指揮官陳時中在記者會上公布，聯亞疫苗沒通過EUA審查！消息一出，聯亞股價立刻呈現跳水式跌幅，短短15分鐘就從203元跌到100元，高低震幅高達50%。財經專家表示，生技股的股本較小，易受人為控制，不穩定的股價還會持續一段時間，而聯亞也發出聲明，表示將重新執行第三期臨床試驗的效益評估。▼ 疫情指揮官陳時中宣布聯亞疫苗沒通過EUA審查。（圖／年代新聞）中央疫情指揮官陳時中在防疫記者會上遺憾地宣布，聯亞疫苗療效評估未達到基準，依舊無法取得緊急授權。消息一出，聯亞股價隨即出現跳水式跌幅，16日上午一度破200元高點漲幅高達20%，但到了下午2時後一路大跌，短短15分鐘，從203元跳水至100元，高低震幅高達50%。▼ 台塑生醫從六月開始陸續出脫持股。（圖／年代新聞）對此，財經專家李永年說，「疫苗短期之內不可能上市，直言大震盪恐怕還會持續一段時間」；而台塑生醫恐怕早已嗅到不尋常，從今年六月一路出脫聯亞藥持股，到八月中已出脫近一半股票，從15.15%降到剩7.62%，也讓投資市場傳出不同聲音。另外，財經專家黃世聰提到 ，「生技股很容易受到訊息的影響，譬如說EUA過了，或是說大訂單要出貨，這個就會讓股價出現大幅度波動，因為它的股本比較小，所以容易受到人為的控制。」這回聯亞疫苗出師不利，但我國向聯亞欲採購500萬劑疫苗，這筆帳該怎麼算？▼ 財經專家黃世聰表示，生技股因股本小容易受人為控制。（圖／年代新聞）中央疫情指揮官陳時中表示，「合約裡面我們預採購，訂定相關補償辦法，也根據辦法付那個錢。」言下之意，聯亞沒過關的500萬劑將由中央買單，但羊毛出在羊身上，拿納稅人的錢付這實驗費，恐怕有點說不過去。",
        keywords=["國產疫苗", "聯亞疫苗", "生技股", "聯亞股價"],
        category=None,
        media="年代新聞",
        datetime="2021-08-17 14:11",
        link="https://www.eracom.com.tw/EraNews/Home/Finance/2021-08-16/544573.html",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return eracom.ERACOM()


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
