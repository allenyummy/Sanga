# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import udn
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
    name="聯合新聞網_1",
    link="https://udn.com/news/story/7253/5550651",
    expected_output=NewsStruct(
        title="凌華 推出單板電腦",
        content="工業電腦廠凌華科技（6166）昨（22）日推出cPCI-A3525系列CompactPCI® Serial單板電腦，搭載英特爾最新第九代Xeon®或Core™ i7處理器，專為軌道交通、航太與國防、工業自動化等高性能關鍵任務型產業的新一代應用而設計。\n\n\n\r\n凌華網路通訊暨公共建設事業處總經理高福遙表示，鐵路運輸、航太、國防及工業領域的系統整合商及解決方案提供商，需要可提供高性能與持續性可靠度，且同時便於嵌入與升級的新科技。PICMG 2.0 CPCI-S.0 CompactPCI® Serial Rev 2.0序列資料傳輸標準，即是目前開放式工業電腦規範CompactPCI （CPCI）標準中最快速、功能最豐富、最具成本效益，還可支援SATA、USB、Ethernet 等高速介面。\n\n\n\r\n凌華指出，新產品提升的效能規範，能以直接插背板介面形式的P6連接器支援外加固態硬碟子板；PCIe介面也提供多個資料頻寬選擇。另外，還可支援七個6 Gb/s SATA介面，以及高達10個USB 2.0/3.0埠於背板的連接模組。\n\n\n\n\n\n\n\n",
        keywords=["凌華", "航太", "工業電腦"],
        category="股市",
        media="聯合新聞網",
        datetime="2021-06-23T00:17:31+08:00",
        link="https://udn.com/news/story/7253/5550651",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="聯合新聞網_2",
    link="https://udn.com/news/story/7254/5542521",
    expected_output=NewsStruct(
        title="NB散熱概念夯 雙鴻營收帶勁",
        content="法人看好，受惠新冠疫情推升NB需求仍持續，加上因散熱結構改變帶動ASP的提升，預估雙鴻（3324）今年NB散熱的營收將年增逾兩成。\n\n\n\r\n散熱模組廠昨（18）日股價動起來，不僅雙鴻量增，盤中股價攻漲停195元，創波段新高外，泰碩午盤股價也衝上漲停板54.7元，拉動奇鋐股價也跟進大漲達9.19%，終場收77.2元，散熱模組族群股價回神。\n\n\n\r\n此外，顯卡散熱風扇龍頭廠動力-KY終場收4.82%、尼得科超眾漲幅也有2.16%，力致漲幅也有1.8%。\n\n\n\r\n雙鴻昨日成交量放大至1.06萬張，股價為近兩個月高點。雙鴻今年5月營收9.51億元，月減7.4%，仍較去年成長2.9%，雖然筆電需求維持高檔、新機持續出貨，主要原因則為受到客戶缺料影響，累計今年前五月營收54.08億元，年增28.75%，為同期新高。\n\n\n\r\n動力今年5月合併營收1.7億元，月減8.8%，為同期新高，且較去年同期大幅增加57.51％，主要受惠台北國際電腦展線上展（COMPUTEX 2021）於6月初舉行，下游各系統廠商紛紛推出支援NVIDIA最新款GeForce RTX 3080 Ti 和 RTX 3070 Ti晶片的顯示卡產品。",
        keywords=None,
        category="股市",
        media="聯合新聞網",
        datetime="2021-06-19T01:12:50+08:00",
        link="https://udn.com/news/story/7254/5542521",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return udn.UDN()


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
