# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import digitimes
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
    name="DigiTimes_1",
    link="https://www.digitimes.com.tw/iot/article.asp?cat=130&cat1=40&cat2=13&id=0000613290_cby1uhlilg4hjclrwlpe5",
    expected_output=NewsStruct(
        title="全民防疫時代來臨  盤點三大防疫神器",
        content="\r\n三級警戒持續延長！面對COVID-19(新冠肺炎)病毒的狡詐多變，可預見未來全球仍會籠罩在其陰影下，在日常生活環境中持續進行防疫，勢必是一場全民馬拉松。\n針對防疫的迫切需求，鴻翊國際(3521)也適時推出解決方案，從整合概念出發，擴大防疫的實際應用層面，期待不只解決企業在防疫上的各項痛點，更為防疫達到多元與效率的加值效果，可以說是協助企業同步提升日常防疫、營運管理、宣傳行銷的「防疫神器」。\n整合測溫與人臉辨識科技的智慧神器\n防疫已經是企業必備的管理措施，準確與效率勢必是優化防疫的重要目標。結合零接觸體溫偵測與人臉辨識的「防疫守門員Facelook X1」，可有效協助實現安全迅速效率的防疫管理。\nFacelook X1具備0.5秒快速測溫，人臉辨識的準確率超過99%，且戴口罩也能辨識。另外Facelook X1也具門禁控制功能，搭配鴻翊國際研發的Facelook Insight數據中心，能和人資系統串聯，取代傳統打卡機作為員工出勤管理工具，達到提升企業營運效率的目的。\nFacelook X1具備相當彈性的擴充功能，能外掛2D掃描模組與OCR辨識模組，可掃描辨識身分證、健保卡、會員卡、票券等，充分滿足多元需求。\n用消毒時間抓住消費者視覺的行銷神器\n手部消毒是落實防疫的重要一環，在駐足消毒時，也同時創造吸引消費者視覺焦點的宣傳時機，DKS-2150防疫數位電子看板便整合了防疫與多媒體展示，可同時呈現包括影片、圖片、跑馬燈等素材，並具備感應式手部消毒，支援人臉辨識與紅外線體溫感測，達到防疫與宣傳一體化。\n高度靈活配置相當適合零售業、百貨業、飯店業、餐飲業、活動會場、娛樂場所、實體展覽、博物館/美術館等多元場景的防疫與宣傳需求。\n消滅環境病毒因子神器\n要減低潛藏細菌病毒的威脅，做好日常清潔維護能讓防疫效果事半功倍。擁有RCI光氫化離子技術的AP10隨身型空氣淨化機與AP50智慧型空氣淨化機，能製造與生成友善氧化淨化因子，有效消滅潛伏在空間中細菌病毒，維護居家與辦公環境最佳品質。\n整合化防疫趨勢已來臨\n鴻翊國際科技事業處執行長許貿程表示，未來防疫絕對會走向整合化的趨勢，滿足更加多元應用需求。鴻翊國際擁有穩固技術基礎與智慧化方案優勢，將持續發揮研發能量，推出更多符合未來趨勢的防疫神器，絕對有信心可以因應「全民防疫時代」的多元防疫需求！相關產品訊息，歡迎查詢鴻翊國際官網防疫產品，或直接撥打02-82272556。\n\n",
        keywords=["人臉辨識"],
        category=None,
        media="DigiTimes",
        datetime="2021-06-29",
        link="https://www.digitimes.com.tw/iot/article.asp?cat=130&cat1=40&cat2=13&id=0000613290_cby1uhlilg4hjclrwlpe5",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="DigiTimes_2",
    link="https://www.digitimes.com.tw/iot/article.asp?cat=158&cat1=20&cat2=&id=0000616397_OKT27NZLLU5LRU60OSZYT",
    expected_output=NewsStruct(
        title="法律科技新創Lawsnote　協助企業提升法務部門效率",
        content="\r\n法律科技是人工智慧(AI)在自然語言處理(NLP)領域的商業應用，雖然海外已經在這領域養出不少獨角獸，台灣這部分的新創卻是相對較晚起步，數量也較少。七法(Lawsnote)法學資料庫是台灣法律科技新創中最先獲得各大金融機構以及科技企業法務處採用的AI解決方案。\nLawsnote創辦人暨執行長郭榮彥表示，獲得全球最大分離式元件(Discrete)達爾科技集團(Diodes)董事長總裁暨執行長盧克修的種子輪投資後，估值已達新台幣1億元，正在努力擴展團隊，完善企業端的解決方案，並向科技業及金融業客戶推廣。\n目前Lawsnote有四大產品線，包括：搜尋引擎、法律遵循、契約審閱和律師學院，服務對象主要是法律工作者和企業法務部門及法遵人員。目前搜尋引擎企業客戶已有大約有500家，並不僅限於律師事務所，因為很多企業的法務也會需要，從最大的台積電到最小的一人公司都有。\n科技業是契約自動審閱最主要的使用者。因為常常要做各式各樣的交易，所以契約量是很大的。目前都是由企業內部的法務人員來審閱，企業規模越大、合約量越多。\n「但是審閱這些契約時，有一個定義基準的清單，法務在審閱這些合約的時候，就有如一個機器人，機械式地去檢查有沒有什麼違反定義基準的地方，但這流程其實是可以透過電腦或是AI來自動判斷的。」郭榮彥說。\n法律遵循自動化和契約自動審閱這兩大功能，都是以AI來輔助專業人員的判斷，提升效率，節省時間。郭榮彥指出，法務人員之前審閱一份合約可能要花1小時，現在透過AI工具只需要5分鐘，就可以辨識出風險何在，但最終修改與否以及修改的內容都還是由專業法務人員判斷。\n他透露，法律遵循自動化解決方案以金融業者為主，而且是金融機構業者在Lawsnote研發階段時就主動提出他們的需求，希望未來的產品設計可以切合他們的需要，協助提升效率。\n由於金融機構所要遵循的法規多如牛毛，光是銀行的部分就有超過2,000部法規，其中任何一部的任何一條只要有修正，就牽一髮而動全身，金融機構就必須因應金融單位遵循金融管理委員會的相關法規變動來調整控制措施，例如要修改內部規章、標準作業流程或是查核等標準程序。\n「光是要找到這些規章並且依照最新法規規定，進行修改，就是曠日費時的大工程。」郭榮彥指出，Lawsnote幫金融業自動監測這2,000部法規，任何一條條文發生變動，就會主動通知法遵人員是哪些內規連動到這條條文，俾利其進行調整。\n郭榮彥指出，法遵主要面向的客戶是金融產業，而企業法務解決方案主要是供應科技產業，其他產業多多少少也都有法律遵循和企業法務的需求。因此未來2~3年，計劃針對不同產業提供適合的服務。\nLawsnote搜尋引擎的商業模式是採用SaaS模式，由個別使用者使用訂閱；企業法務契約審閱與企業法遵則直接與企業客戶對接的B2B模式，並且直接把模組放進客戶的系統或私有雲中，因為如果放上雲端，客戶對資訊安全會有疑慮。\n\n",
        keywords=["AI", "新創企業", "AI", "法律科技", "新創企業"],
        category=None,
        media="DigiTimes",
        datetime="2021-08-10",
        link="https://www.digitimes.com.tw/iot/article.asp?cat=158&cat1=20&cat2=&id=0000616397_OKT27NZLLU5LRU60OSZYT",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return digitimes.DigiTimes()


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
