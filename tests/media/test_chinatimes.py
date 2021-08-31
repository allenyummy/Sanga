# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import chinatimes
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
    name="中時新聞網_1",
    link="https://www.chinatimes.com/realtimenews/20210712002325-260410",
    expected_output=NewsStruct(
        title="《盤中解析》衝高近300點後 航海王落水、漲點腰斬",
        content="美股帶頭衝，台股大漲逾200點！上週五美股強勢收高，化解上週五因航運等重挫帶衰，終止周K連7紅的台股探底壓力，今天由將於本週舉行法說會的台積電(2330)穩盤及股王-矽力-KY(6415)強勢大漲，站上4000元關卡領軍帶動半導體類股表現強勢，強茂(2481)、漢磊(3707)、杰力(5299)、威鋒(6756)及華東(8110)盤中股價亮燈漲停，砷化鎵廠-宏捷科(8086)、穩懋(3105)及全新(2455)也連袂走高，車用零組件也表現強勢，康普(4739)、健和興(3008)及佳凌(4976)同步亮燈，在電子股帶頭衝，以及玻璃類股因台玻(1802)強勢大漲領軍走高下，台股指數跳空開高，一度大漲近300點，逼近17950點。\n\n\n\n不過中場過後，利多大放送的航運類股再現賣壓，股價開高走低，長榮(2603)及新興(2605)盤中股價由紅翻黑，觀光類股也持續弱勢，致使台股指數漲幅縮小，截至11點25分為止，加權股價指數約17815.56點，上漲154.08點，成交量約3710.63億元，OTC指數為218.84點，上漲2.99點，成交量約750.94億元。\n\n今天盤中上市各類股以玻璃類股表現最佳，上漲3.89%，其次是半導體類股及鋼鐵類股，分別上漲1.82%及1.48%，表現較差者為觀光類股、造紙類股及油電氣類股，其中觀光類股下跌2.64%，造紙類股下跌2.27%，油電氣類股下跌2.12%；上櫃部分，表現最佳化工類股，上漲4.83%，表現最差為觀光類股，下跌2.11%。\n\n就技術面來看，上週台股指數由電子類股接棒帶領，在7月6日創下歷史新高，不過航運等傳產股拖累台股在下半周拉回，終場加權股價指數以17661.48點作收，累計一週下跌48.67點，跌幅約0.27%，週K收黑，終止週K連7紅，日均量為5955.8億元；OTC收盤指數為215.85點，累計一週上漲2.17點，漲幅為1.02%，週K連8紅，日均量約911.41億元。今天台股在電子股及金融續強下，台股指數一度大漲近300點，站上17900點。\n\n上週台股指數週線終止連7紅。加權指數跌破10日均線，上漲慣性遭受破壞，短線恐轉為震盪整理格局，月線17528點將是多方防守的支撐所在，月線不跌破前可偏多操作。分析師表示，歐美疫苗積極施打、疫情已有所趨緩；美國基建計畫達成協議，經濟加速復甦，加上美國財報季登場，預期將釋出正面訊息，激勵美股持續多方走勢；在台股部分，台灣確診人數降溫，並逐步開放管控，有利內需恢復；且時序進入傳產及電子產業旺季，加上緊接而來的股東會、法說會與財報季陸續登場，可望釋出正面訊息，利多行情可期，搭配台股技術面多頭排列，成交量能溫和擴大，有利台股維持強勢；不過，上週台股指數雖然攻上18000點，再創新高，但過去的主流類股航運及鋼鐵等已出現利多鈍化，且上週航運帶量殺低，資金出傳產轉電子趨勢日益明確，加上蘋果股價創下新高，低基期的蘋概股近期開始加溫，建議做多電子類股，對於漲多的航運及原物料個股見好就收。\n\n在選股方面，以高殖利率概念股及業績題材股為主，如：IC載板、Server供應鏈、APPLE供應鏈及汽車相關等族群為主；精華(1565)因中國訂單動能明確，日本轉佳中，美國回穩，中國市場客戶包括國際品牌博士倫、Seed、當地新銳品牌可拉拉、mitata等，當前中國線上彩片市場需求動能強勁，預估今年中國營收有機會成長50%以上，日本第2季兩大客戶下單狀況持續轉佳，預估今年整體成長率約20%，美國市場則是成長10%，可逢低佈局。\n\n\n\n",
        keywords=["加權股價指數", "OTC指數", "長榮", "新興", "航運"],
        category="財經",
        media="中時新聞網",
        datetime="2021-07-12T12:01:21+08:00",
        link="https://www.chinatimes.com/realtimenews/20210712002325-260410",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="中時新聞網_2",
    link="https://www.chinatimes.com/realtimenews/20210428001632-260410",
    expected_output=NewsStruct(
        title="《台北股市》盤中焦點股：第一銅、欣興、智原、定穎、普安、東和",
        content="1.威剛(3260)：昨獲三大法人聯手買超1736張，帶動盤初股價漲逾7%，創波段新高。\n\n2.廣穎(4973)：昨外資擴大買超241張，激勵早盤股價一度漲近4%，續創37.4元高價。\n\n3.聯電(2303)：法說今日登場，惟昨外資大舉調節44272張、昨夜ADR跌3.31%，今早股價貼近平盤整理。\n\n4.第一銅(2009)：周二銅價逼近1萬美元，不理外資昨賣超3156張，今早股價漲逾9.5%，突破60關。\n\n5.杰力(5299)：首季登頂、每股賺3.14元，激勵早盤上漲逾3%。\n\n6.欣興(3037)：Q1淡季獲利創次高，挾4.1萬張量能衝上112.5元漲停，突破波段新高價。\n\n7.景碩(3189)：景碩Q1不如預期，內外資反喊買，晨盤反彈漲逾4.5%，重返10日線。\n\n8.文曄(3036)：Q1獲利登頂，Q2營收年增上看3成，早盤一度爆量強漲近5%。\n\n9.智原(3035)：第1季獲利創16季高，季增逾6倍，Q2營運向上，股價登漲停，再寫短波高價。\n\n10.萬海(2615)：傳5月調漲台越線出口運價，且可能在10月跟進調薪，晨盤飆漲逾5%，持平前高。\n\n11.裕民(2606)：周二BDI指數創近10年新高，多方續湧，早盤上揚逾2.5%。\n\n12.敦泰(3545)：不畏列警示股，3月每股盈餘1.99元，倍數成長，股價漲逾4.5%。\n\n13.台玻(1802)：漲價題材不退燒，人氣持續高蓬，晨盤高漲逾9%，觸及32.85元漲停價、短高價。\n\n14.定穎(6251)：可轉債競拍題材，多方簇擁，早盤爆量續漲逾8%，衝上波段高點。\n\n15.佳龍(9955)：銅價強漲，掀比價效應，早盤續漲5%，改寫前高。\n\n16.普安(2495)：PC產業淡季不淡，供應鏈看俏，早盤亮燈漲停，攻克20元。\n\n17.榮星(1617)：挾漲價題材，線纜股受惠，早盤登頂。\n\n18.建碁(3046)：資金追捧銅板股，外資昨擴大買超，早盤拉出第2根漲停。\n\n19.大統益(1232)：Q1每股賺3.05元，早盤聞訊勁揚8%以上。\n\n20.憶聲(3024)：新台幣狂升，資產股吸引買盤湧入，近日股價連日攀揚，早盤強彈5%，改寫逾10年高價。\n\n21.ABC-KY(6598)：股價跌深，獲低接買盤敲進，連兩日亮燈觸頂。\n\n22.東和(1414)：第1季每股盈餘0.08元，早盤放量攻頂，衝上今年最高。\n\n23.兆赫(2485)：東奧照辦，概念股強勢表態，在外資連4買力挺下，早盤續攀揚近5%，來到近3年高位。\n\n24.元太(8069)：今年成長動能強勁，獲外資連10買，早盤勁升半根停板，站上逾9年高峰。\n\n25.大東(1441)：台幣勁升，資產股強強滾，早盤火速攻頂，衝上逾1年高價。\n\n26.森寶(3489)：短多出擊，早盤亮燈攻頂，站上半年高點。\n\n\n\n",
        keywords=["台股", "焦點股", "佳龍", "定穎", "景碩"],
        category="財經",
        media="中時新聞網",
        datetime="2021-04-28T10:18:15+08:00",
        link="https://www.chinatimes.com/realtimenews/20210428001632-260410",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return chinatimes.Chinatimes()


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
