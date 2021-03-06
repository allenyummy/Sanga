# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import nownews
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
    name="今日新聞_1",
    link="https://www.nownews.com/news/5357780",
    expected_output=NewsStruct(
        title="聯亞疫苗EUA沒過 將重評估三期臨床效益",
        content="\n\r\n                                中央流行疫情指揮中心今（16）日宣布聯亞生技的新冠疫苗未通過衛福部食藥署的新冠疫苗專案製造緊急使用授權（EUA）。對此，興櫃上市公司聯亞藥代母公司發表公告，表示目前國內臨床二期試驗持續進行，母公司將重新執行第三期臨床試驗的效益評估。\n\n我是廣告 請繼續往下閱讀\n\n\n\n\n\n\n\n\r\n\t\t\t\t            \t聯亞藥指出，母公司聯亞生技開發股份有限公司於6月30日向台灣衛福部食藥署申請COVID-19疫苗UB-612專案製造EUA，經食藥署8月15日召開專家會議審查，UB-612未符合「新冠疫苗專案製造或輸入技術性資料審查基準」。聯亞藥表示，該公司與母公司簽訂UB-612疫苗委託製造合約，已收取50%不可退還訂金，應可支應已投入生產疫苗成本。另自有產品銷售情形良好，並有穩定國內外客戶藥品委託製造及藥品開發訂單，上述事件對財務業務影響有限。聯亞藥表示，聯亞生技的UB-612新冠疫苗國內臨床二期試驗持續進行，至於下一階段，母公司將重新執行第三期臨床試驗效益評估。6月底聯亞生技的二期臨床試驗期中分析報告記者會中曾表示，該公司的新冠疫苗對變種病毒具保護力，除加速前往印度進行1.1萬人三期臨床試驗，也將在美國進行「混合補強施打」的第二期臨床試驗。",
        keywords=["聯亞藥", "聯亞生技", "疫苗", "EUA", "臨床試驗"],
        category="財經",
        media="今日新聞",
        datetime="2021-08-16T19:54:23+08:00",
        link="https://www.nownews.com/news/5357780",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="今日新聞_2",
    link="https://www.nownews.com/news/5357268",
    expected_output=NewsStruct(
        title="仁寶也出手了 捐贈1億元助慈濟購買BNT疫苗",
        content="\n\r\n                                繼台泥之後，仁寶電腦今（16）日也發布重訊表示，為實踐企業社會責任並支持社會公益，將參與捐贈慈濟慈善事業基金會新台幣1億元，支持慈濟基金會捐助防疫疫苗予台灣，祝愿台灣社會早日戰勝疫情。\n\n我是廣告 請繼續往下閱讀\n\n\n\n\n\n\n\n\r\n\t\t\t\t            \t慈濟基金會在今年7月21日成功簽訂500萬劑BNT疫苗，所購得的疫苗將全數捐給政府主管機關，以作為新冠肺炎（COVID-19）防疫使用。台泥在12日率先宣布，董事長張安平、董事會認同慈濟基金會疫苗捐贈用途，並善盡台泥企業社會責任，因此董事會決議參與捐贈資助慈濟慈善基金會1億元用於購買疫苗。仁寶也在今日發布重訊表示，為實踐企業社會責任並支持社會公益，將參與捐贈慈濟基金會新台幣1億元，支持慈濟基金會捐助防疫疫苗予台灣，祝愿台灣社會早日戰勝疫情。由於此捐贈因屬重大天然災害所為急難救助的公益性質捐贈，將會提公司董事會追認。※【NOWnews 今日新聞】提醒您：因應新冠肺炎疫情，疾管署持續加強疫情監測與邊境管制措施，國外入境後如有發燒、咳嗽等不適症狀，請撥打「1922」專線，或「0800-001922」，並依指示配戴口罩儘速就醫，同時主動告知醫師旅遊史及接觸史，以利及時診斷及通報。",
        keywords=["新冠肺炎疫苗", "仁寶", "台泥", "慈濟", "BNT疫苗"],
        category="生活",
        media="今日新聞",
        datetime="2021-08-16T18:53:37+08:00",
        link="https://www.nownews.com/news/5357268",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return nownews.NowNews()


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
