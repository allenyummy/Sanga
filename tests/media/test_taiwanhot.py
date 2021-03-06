# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import taiwanhot
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
    name="台灣好新聞_1",
    link="https://www.taiwanhot.net/?p=957639",
    expected_output=NewsStruct(
        title="五倍券改免費領　馬英九：為德不卒，應發現金比較好 | 台灣好新聞 TaiwanHot.net",
        content="為振興國內經濟，行政院規劃推出振興五倍券，原先要民眾用「1000換5000」，但引發不少民進黨立委反彈。政院於昨(16)日與黨籍立委溝通後，拍板全民免付1千直接領券。對此，前總統馬英九今(17)日表示，五倍券與當年的消費券很近似，但他還是覺得為德不卒，並表示紓困一定要對症下藥，針對真正需要的民眾紓困才有意義，應該要發現金比較好。\n馬英九指出，現在最需要紓困的是基層服務業，因很多商家都已無法營業、沒有收入，但像工業與貿易情況還不錯，所以今年經濟成長還可以維持百分之5以上，所以一定要對症下藥，對真正需要的民眾紓困才有意義，他認為應該要發現金比較好。\n對於政院拍板全民免費領五倍券，遭外界質疑與當年馬政府時代的消費券有何不同？馬英九說，感謝大家說要還他公道，但還他公道不重要，要讓民眾有公道。\n ",
        keywords=None,
        category=None,
        media="台灣好新聞",
        datetime="2021-08-17 13:01",
        link="https://www.taiwanhot.net/?p=957639",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="台灣好新聞_2",
    link="https://www.taiwanhot.net/?p=957645",
    expected_output=NewsStruct(
        title="七旬老婦匯11萬借香港朋友　行員通報警方阻詐保住老本 | 台灣好新聞 TaiwanHot.net",
        content="板橋警分局後埔所警員薛俊廷、蔡鈺霖日前接獲轄內銀行行員通報，1名七旬老婦欲匯款新臺幣11萬元借給香港朋友，作為友人母親的醫藥費用，行員聽到關鍵詞察覺異狀，即刻通報轄內派出所，請警方派員前來瞭解婦人匯款原因，後埔所員警接獲通報後不敢大意，迅速趕往銀行協助行員了解狀況。\n據該婦人說，1年多前在臉書上認識1名自稱是國外飛行員的網友，之後又透過LINE聊天，該名飛行員網友長期關懷她，並以男女朋友方式相稱，但從6月份開始，網友稱其母親生病住院家中現金不夠付醫藥費，希望能借款以度過難關，婦人不疑有詐，火速前往銀行匯款給男友救急，幸得行員機警，注意到婦人神情慌張，且又無法清楚說明借款原因及對方身分，遂通報警方前來處理，行員與員警一同向婦人解釋類似的詐騙手法，最終成功守護婦人的辛苦積蓄。\n\n板橋警分局提醒該類假交友詐騙，先以噓寒問暖照三餐問候的方式打動芳心降低戒心，再以各種理由向被騙民眾借款，最好的保護就是要過濾來路不明的交友訊息，提到錢財務必提高警覺，並呼籲民眾如遇到疑似詐騙手法，一定要保持冷靜、小心查證、馬上撥打165反詐騙專線諮詢，另外民眾如果發現犯罪不法情事，務必要即刻通知警方到場處理、了解並可深入偵辦，共同創造安居樂業的優質環境。\n ",
        keywords=None,
        category=None,
        media="台灣好新聞",
        datetime="2021-08-17 12:59",
        link="https://www.taiwanhot.net/?p=957645",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return taiwanhot.TaiwanHot()


@pytest.mark.parametrize(
    argnames="name, link, expected_output",
    argvalues=[tuple(t) for t in TEST_DATA_LIST],
    ids=[
        f"{t.name}, {t.link[:50]+'...' if len(t.link) > 50 else t.link}"
        for t in TEST_DATA_LIST
    ],
)
@pytest.mark.skip(
    reason="This media will block IP to not allow us to crawler their data, leading test error."
)
def test_get_info(
    newsCrawler,
    name,
    link,
    expected_output,
):
    output = newsCrawler.getInfo(link=link)
    assert NewsStruct.__2dict__(output) == NewsStruct.__2dict__(expected_output)
