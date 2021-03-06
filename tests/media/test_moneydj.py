# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import moneydj
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
    name="MoneyDJ理財網_1",
    link="https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=6f1bfd5e-30bb-4fcf-b7ee-4fcb0c19696e",
    expected_output=NewsStruct(
        title="力旺總座沈士傑辭世，董座徐清祥暫代職務",
        content="\nMoneyDJ新聞 2021-07-22 07:51:01 記者 新聞中心 報導力旺(3529)昨(21)日公告，公司董事兼總經理沈士傑辭世，由董事長徐清祥暫代總經理職務。力旺表示，公司各項業務均由專業經理人分層負責，並有代理人制度，公司營運一切正常。\r\n\n\n\r\n據了解，沈士傑為徐清祥在清大任教時的第一屆學生，而後徐清祥與一群學生創立力旺電子，沈士傑於2001年加入，師徒情誼深厚，成為業界美談。沈士傑加入力旺後，曾任技術與營運中心副總經理，負責督導技術開發、行銷業務及建立客戶服務團隊，也擔任過技術暨設計服務處主管，將公司的技術發展由0.7微米微縮至90奈米，並於2009年接任力旺總經理。\n",
        keywords=["設計IP", "力旺"],
        category="財經",
        media="MoneyDJ理財網",
        datetime="2021-07-22T07:51:01+08:00",
        link="https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=6f1bfd5e-30bb-4fcf-b7ee-4fcb0c19696e",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="MoneyDJ理財網_2",
    link="https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=6c236fc2-97e0-4676-9846-a4d45c9ec199",
    expected_output=NewsStruct(
        title="《DJ在線》體溫計國內已飽和，有無汰換需求待觀察",
        content="\nMoneyDJ新聞 2021-05-18 11:10:15 記者 劉莞青 報導體溫量測產品壽命約在2年左右，經歷去年年初首波疫情後，國內商場與家戶普遍已經建立有體溫量測設備與相關動線安排，國內業者坦承體溫量測產品國內需求估計不會顯著增加，校正後應可持續使用、汰舊換新需求仍需觀察，目前以熱映（3373）、豪展（4735）、泰博（4736）等體溫量測設備製造商業績來看，今年以來以海外代工訂單為主要業績的豪展仍是三間業者當中業績續航力較佳者。\r\n\n\n\r\n去年二月新冠疫情首度於國內蔓延，體溫量測產品炙手可熱，國內當時具有產能的業者包括熱映、泰博均有自有品牌與國內產能，在國內一度禁止體溫量測產品出口下，加上國內需求強，拉抬兩家業者的業績顯著走高，豪展則因主要產能在中國，客戶以代工為主，去年上半年業績表現相對偏平。\n\n\n\r\n不過去年自下半年起，體溫量測業者業績出現翻轉，國內疫情降溫以後，國際疫情仍持續嚴峻，豪展的品牌客戶也積極下單，帶動豪展業績持續向上，表現較泰博、熱映兩間業者均強勢。\n\n\n\r\n但整體而言去年對於體溫量測製造商都是豐收的一年，以三間業者去年營運成績來看，豪展去年營收26.07億、年增107%、EPS 14.66元；熱映去年營收26.17億、年增233%，EPS 17.01元；泰博營收59.04億(含血糖量測等其他產品)年增約43%，EPS 17.08元。\n\n\n\r\n在去年國內首波疫情過後，國內家戶與商場普遍已經建立起完善的人流導流與體溫量測設施，體溫量測產品壽命約在2年上下，過去1年積極使用下，業者坦言多數產品應僅需進行校正即可提升準確度，汰舊換新需求應不顯著。\n\n\n\r\n在價格方面，通路方面亦可觀察到從去年下半年起體溫量測產品價格也逐漸走降，從高端額溫槍產品終端報價來看，從平均2,500元左右下滑至1,800元左右，需求也趨穩定、斷貨限購狀況均已改善。\n\n\n\r\n今年前4月來看，泰博前4月營收來到16.77億、年減約12%；熱映前4月營收來到4.82億、年減約2成；豪展以國際客戶代工訂單為主，前4月營收則是來到12.85億、年增仍高達292%，第一季獲利上，豪展EPS 4.89元、泰博EPS 5.24元(業外貢獻近1.8元)、熱映EPS 1.5元，以海外代工訂單為主要業績的豪展，仍是三間業者當中業績續航力較佳者。\n",
        keywords=["體溫計", "熱映", "豪展", "泰博", "財務比率", "生物科技-診斷監測用醫材", "供需面"],
        category="財經",
        media="MoneyDJ理財網",
        datetime="2021-05-18T11:10:15+08:00",
        link="https://www.moneydj.com/kmdj/news/newsviewer.aspx?a=6c236fc2-97e0-4676-9846-a4d45c9ec199",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return moneydj.MoneyDJ()


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
