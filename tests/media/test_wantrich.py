# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import wantrich
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
    name="旺得富_1",
    link="https://wantrich.chinatimes.com/news/20210804S426253",
    expected_output=NewsStruct(
        title="《外資》賣超股：新光金、華邦電、長榮",
        content="【時報-台北電】經統計，前個交易日(20210803)\n 1.外資連續賣超五日以上的股票：\n 富強鑫(6603) 福邦證(6026) 臺企銀(2834) 仁寶(2324)\n 緯創(3231) 炎洲(4306) 瑞儀(6176) 錸德(2349)\n 台微體(4152) 天鈺(4961) \n 2.連續賣超四日的股票：\n 亞泥(1102) 佳凌(4976) 聯強(2347) 正文(4906) 威剛(3260) \n 台虹(8039) 中探針(6217) 台達電(2308) \n 3.連續賣超三日的股票：\n 高技(5439) 利奇(1517) 聯詠(3034) 三商壽(2867)\n 網龍(3083) 廣積(8050) 環球晶(6488) 中裕(4147)\n 宣德(5457) 九豪(6127) 力致(3483) 台嘉碩(3221)\n 倉和(6538)\n4.連續賣超二日的股票：\n 國泰金(2882) 潤泰新(9945) 明基材(8215) 誠美材(4960)\n 聯亞(3081) 群益證(6005) 國票金(2889) 福懋(1434)\n 力麒(5512) 義隆(2458) 鈺創(5351) 穩懋(3105) 欣銓(3264) 東洋(4105) 啟碁(6285) 盛群(6202) 致伸(4915) 台郡(6269) 凱崴(5498) 樺晟(3202) 和鑫(3049) 中光電(5371)\n 佰鴻(3031) 光寶科(2301) 希華(2484) 系統電(5309)\n 長興(1717) 聚和(6509) 廷鑫(2358) \n 5.轉買為賣的股票：\n 鴻海(2317) 網家(8044) 富邦金(2881) 中信金(2891)\n 上海商銀(5876) 台塑化(6505) 宏碁(2353) 寶成(9904)\n 中鋼(2002) 漢翔(2634) 佳世達(2352) 友達(2409)\n 群創(3481) 康普(4739) 建錩(5014) 宏致(3605)\n 華星光(4979) 易華電(6552) 正德(2641) 大國鋼(8415) \n 中航(2612) 漢磊(3707) 盛餘(2029) 建漢(3062)\n 台新金(2887) 第一金(2892) 彰銀(2801) 新光金(2888)\n 遠東銀(2845) 廣達(2382) 英業達(2356) 云辰(2390)\n 宏捷科(8086) 裕隆(2201) 旺宏(2337) 同致(3552)\n 台塑(1301) 華夏(1305) 台化(1326) 集盛(1455)\n 中石化(1314) 遠東新(1402) 南紡(1440) 中纖(1718)\n 長榮(2603) 陽明(2609) 新興(2605) 裕民(2606) 萬海(2615) 華航(2610) 長榮航(2618) 榮運(2607) 慧洋-KY(2637)\n 嘉里大榮(2608) 四維航(5608) 台航(2617) 台驊投控(2636) 東和鋼鐵(2006) 允強(2034) 彰源(2030) 大成鋼(2027)\n 中鴻(2014) 燁輝(2023) 聚亨(2022) 官田鋼(2017)\n 世紀鋼(9958) 方土昶(6265) 農林(2913) 中美晶(5483)\n 嘉晶(3016) 群聯(8299) 茂矽(2342) 榮剛(5009)\n 華邦電(2344) 伍豐(8076) 台玻(1802) 精材(3374)\n 譜瑞-KY(4966) 霖宏(5464) 常珵(8097) 良維(6290)\n 禾昌(6158) 僑威(3078) 沛波(6248) 鉅祥(2476)\n 光磊(2340) 旺矽(6223) 艾笛森(3591) 光洋科(1785)\n 吉祥全(2491) 華新科(2492) 千如(3236) 華容(5328)\n 信昌電(6173) 立敦(6175) 萬潤(6187) 佳邦(6284)\n 元山(6275) 晶技(3042) 強茂(2481) 朋程(8255) 普誠(6129) 加百裕(3323) 十銓(4967) 台康生技(6589) 高端疫苗(6547) 春源(2010) 燁興(2007) \n 6.賣超前20名：\n 金融股：\n 新光金(2888) 臺企銀(2834) 國泰金(2882) \n 電子股：\n 華邦電(2344) 友達(2409) 群創(3481) 鴻海(2317)\n 宏碁(2353) 旺宏(2337) 光磊(2340) \n 傳產股：\n 長榮(2603) 中鋼(2002) 華航(2610) 亞泥(1102)\n 大成鋼(2027) 長榮航(2618) 陽明(2609) 燁興(2007)\n 燁輝(2023) 台驊投控(2636)\n(時報資訊)",
        keywords=["外資", "賣超股"],
        category="上市櫃",
        media="旺得富",
        datetime="2021-08-04 08:25:52.123",
        link="https://wantrich.chinatimes.com/news/20210804S426253",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="旺得富_2",
    link="https://wantrich.chinatimes.com/news/20210819S442332",
    expected_output=NewsStruct(
        title="中航、台航輾壓長榮、陽明 專家揭背後2大秘辛",
        content="受到美股拖累，台股今（19日）盤中大跌逾300點，但航運股仍是盤面「吸金」焦點，成交比重占大盤逾4成，其中散裝輪中航、台航逼近漲停，強壓貨櫃輪。對此，法人分析，貨櫃三雄長榮、陽明、萬海全年每股盈餘（EPS）35～37 元的本益比個位數，這些利多市場都知道，相較之下，散裝輪 EPS爆發力，市場不太清楚，套牢壓力較小；因此下半年黑馬股，挑選籌碼較乾淨、利多不凸顯才是王道。\n\n當沖降稅確定延長3年，吸引當沖客大舉回籠，航海王延續昨日氣勢再度成為主流。航運族群早盤占大盤成交比重一度跳增45%，盤中表現最亮眼的是散裝航運，台航、中航攻上漲停，四維航、慧洋-KY、裕民、新興等漲幅2%~7%不等；而貨櫃的萬海上漲逾1%，長榮、陽明則小跌在平盤附近震盪。\n\n萬寶投顧總監蔡明彰指出，大陸鋼鐵下半年減產，使上游原料鐵礦石期貨自 7 月高點以來下跌 34％，這對鐵礦石生產商是利空，但對鋼鐵生產商及載運的散裝輪卻是利多。前者降低成本、利差擴大，後者受惠大陸港口鐵礦石庫存降低，趁低價趕快回補。除了鐵礦石、煤炭外，散裝輪運送糧食穀物，南美今年乾旱，糧食價格狂漲，9 月是穀物運送旺季，散裝輪運價欲小不易。\n\n他強調，貨櫃三雄上半年 EPS15～17 元，全年估 35～37 元，長榮、陽明、萬海 的本益比個位數市場都知道，就是對利多太瞭解，所以套牢一大票籌碼，未來貨櫃三雄反彈，層層反壓。\n\n蔡明彰認為，相較之下，散裝輪 EPS 爆發力，市場不太清楚，套牢壓力較小。中航今年 EPS 估 7 元，較去年 1.67 元，成長 3.1 倍；台航今年EPS 估2.3 元，較去年1.24元成長 85％；四維航今年 EPS 估 5 元，較去年虧損 3.2 元大幅轉機；裕民今年估 3.8 元，較去年 1.04 元，成長 2.6 倍；慧洋- KY 今年EPS 估 6 元，較去年 0.15 元，成長 39 倍。\n蔡明彰提醒，台股進入下半場，黑馬未必是 EPS 最高、本益比最低的個股，往往是利多比較不知道、籌碼較乾淨的股票。\n(時報資訊)",
        keywords=["航運股", "散裝航運", "大陸鋼鐵", "貨櫃三雄"],
        category="上市櫃",
        media="旺得富",
        datetime="2021-08-19 11:02:50.287",
        link="https://wantrich.chinatimes.com/news/20210819S442332",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return wantrich.WantRich()


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
