# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Test NewsCrawler

import logging
import pytest
from collections import namedtuple
from Sanga.media import epochtimes
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
    name="大紀元_1",
    link="https://www.epochtimes.com/b5/21/8/15/n13163638.htm",
    expected_output=NewsStruct(
        title="台股連7跌 投顧：搶反彈像火中取栗 - 大紀元",
        content="【大紀元2021年08月15日訊】（大紀元記者侯駿霖台灣台北報導）台股跌跌不休，已連跌7天摜破季線與17000點關卡，與歐美股市創高相比，台股及亞股率先回檔，（16日）將持續測試半年線16949點，以及前波低點16893點。法人15日表示，由於本土主力資金撤出、外資偏空操作，目前盤面缺乏追價力道，主流類股略顯疲弱，台股在短線上恐不樂觀，建議投資人應保守配置。\n富蘭克林華美投信第一富基金經理人周書玄指出，現階段斷線市場訊息雜亂，Delta變種病毒蔓延之下，使長短料供應緊缺，導致電子下游出貨量縮減，就短期走勢推斷，可能以區間盤整為主。\n周書玄認為，目前缺少主流類股帶動，盤面信心盡失，表面經濟景氣看俏，但台股有做頭趨勢，預估指數還會持續修正整理，將回測至半年線位置，操作上建議應保守看待。\n安聯投信台股團隊分析，由於市場雜音在過去一週頻出，包括美國Delta變種病毒延燒跡象，加上市場對部分交易新制傳言的擔憂，但最主要還是缺少盤面主流股帶動、追價力道所致。他們表示，目前還需一段時間才能銷貨市場雜音，台股維持震盪走跌或盤整格局，但部分財報展望較佳的族群，投資價值也逐步浮現。\n從籌碼面觀察，永豐投顧表示，「籌碼面已見鬆動，台股偏向空頭格局。」代表散戶動向的融資餘額，由6日至11日的短短4個交易日，融資大減159億元，透露出本土主力已迅速將資金抽離。\n在外資部分，永豐投顧分析，隨著美國費城半導體指數表現來看，因為忽多忽空，基本上是屬於短線交易；尤以目前市場均關注美國貨幣量化寬鬆（QE）是否撤離，卻忽略加拿大、紐西蘭及澳洲將預估提前縮減QE，並且考慮可能升息，導致原本資金外溢至新興市場的現象，已開始收斂。\n永豐投顧認為，整體台股短期下挫或許有反彈機會，但產業雜音剛起、資金收縮才剛步入進行式，週隨機指標（KD指標）仍在修正當中，想搶反彈如同「火中取栗」。\n觀察三大法人在過去一週對航運股合計賣超近7.5萬張。航運指數本週續跌4%，其中海運主要指標股中，長榮週跌8%；萬海週跌近7%；台驊週跌近3%；僅陽明週漲1.5%有相對有撐。\n大部分業者都認為，海運現階段市況無虞，台驊表示，缺櫃、缺艙、缺工和缺車等情況會延續到今年年底，同時歐美廠商也將擴大回補庫存，預測艙位仍供不應求，樂觀看待全球航運市場，目前正處於榮景中。\n陽明也宣布將擬斥資約9500萬美元（約新台幣26.6億元）訂購13,270個新貨櫃，以因應目前的缺櫃問題，這也意味著市況仍持續熱絡；不過，部分法人內資仍追捧，但外資已陸續發布報告指出，年底前市況可望續強，但明年運價的上漲空間還有待觀察，不排除獲利成長幅度較今年趨緩。\n責任編輯：呂美琪",
        keywords=["台股", "大紀元"],
        category="亞洲",
        media="大紀元",
        datetime="2021-08-15T20:30:08+08:00",
        link="https://www.epochtimes.com/b5/21/8/15/n13163638.htm",
    ),
)

TEST_DATA_2 = TEST_DATA(
    name="大紀元_2",
    link="https://www.epochtimes.com/b5/21/8/10/n13153632.htm",
    expected_output=NewsStruct(
        title="道指和標普指數創高 專家卻擔心美股泡沫化 - 大紀元",
        content="【大紀元2021年08月11日訊】（大紀元記者張東光綜合報導）在美國參院通過1萬億美元基建方案的激勵下，道指和標普500指數週二（10）同步創下歷史新高，前者漲0.5%或162點收報35,264點，後者漲0.1%收報4,436點。但或許市場只有一套資金，在道指上漲的過程中，納指卻下挫0.5%，已透露出詭異的氛圍。\n週二，參院以69票贊成、30票反對的方式通過基建方案。該案現在正送往眾院表決，理論上通過的機率頗高。眾院民主黨人或有意擴大法案支出金額至3.5萬億美元，投資人認為這對能源和工業類股將是一大利多。\n此外，美國10年債殖利率攀高到1.354%，推升金融股齊揚，花旗集團和富國銀行皆上漲2%。市場解讀，美債利率越高，將擴大銀行業的利差，但美債殖利率越高，科技股的估值將被打折。\n然而，基建方案中還包含了寬頻接取計劃、電動車充電站和網絡安全等施政，但相關受惠的科技巨頭週二卻全面下挫，或反映市場資金不繼、無法全方面照顧各類股齊漲的事實。\n儘管週二道指和標普指數創新高，但越來越多的專家認為美股已經泡沫化，追高的風險已越來越大。華爾街知名投資家伯恩斯坦（Rich Bernstein）語出驚人表示，現在的市場泡沫是他職涯以來所見最大的一個。\n今年6月，伯恩斯坦便說比特幣有泡沫，之後比特幣便如滾雪球般崩跌，儘管近期出現反彈，但3個月內比特幣仍下挫20%。伯恩斯坦近日表示，當泡沫出現時，人們將變得短視，只注意非常小的投資範圍。但他同時坦承，儘管有泡沫，但泡沫何時破滅卻誰也不知道。\n另一名華爾街知名的放空高手查諾斯（Jim Chanos）也警告，此時正是散戶投資人積極參與的末段行情。他說，散戶不會在底部積極參與，2009年的底部和2002年的底部他們都不參與的，但他肯定散戶在1999年的網絡泡沫中是積極參與的，而那個時候正好是先知者和內部人士賣股套現的好時機。\n查諾斯最知名的一役是2000年放空安隆公司，這家能源股曾是世界上最大的電力、天然氣以及電訊公司之一，但因為作假帳而在2001年宣布破產。查諾斯放空這一檔股票可謂名利雙收。\n不過，查諾斯去年在放空特斯拉的過程中卻被狠狠嘎空，該股去年大漲7倍，今年初查諾斯結束了放空特斯拉的部位、 鎩羽而歸。\n週三，投資人將密切關注美國的物價報告，經濟學家預期7月的消費者物價指數將比前月增加0.5%，同比大漲5.3%，比6月的5.4%緩增，反映經濟學家預期通脹應該已在6月觸頂。\n通脹數據若大於預期或持續在高峰打轉，很可能讓市場聯想美聯儲將很快啟動縮表的動作。而此一預期心理主要反映在美元指數報價上，週二收報93.073，近日已呈現天天緩漲的牛步，若衝過93.3前高，很可能挑戰95～96反壓區。\n責任編輯：葉紫微#",
        keywords=["美股", "大紀元"],
        category="新聞",
        media="大紀元",
        datetime="2021-08-11T10:14:55+08:00",
        link="https://www.epochtimes.com/b5/21/8/10/n13153632.htm",
    ),
)

TEST_DATA_LIST = [TEST_DATA_1, TEST_DATA_2]


@pytest.fixture(scope="module")
def newsCrawler():
    logger.warning("Init News Crawler ...")
    return epochtimes.EpochTimes()


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
