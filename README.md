[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/allenyummy/Sanga/blob/master/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8%7C3.9-blue)](https://pypi.org/project/Sanga/)
[![PyPi](https://img.shields.io/pypi/v/Sanga)](https://pypi.org/project/Sanga/)
[![Release](https://img.shields.io/badge/release-0.0.1.dev4-blueviolet)](https://github.com/allenyummy/Sanga/releases/tag/0.0.1.dev4)
[![Codecov](https://img.shields.io/badge/codecov-98%25-red)]()

# Sanga

Sanga crawls media news in Taiwan. Given a link, Sanga would collect information of the news, including news title, news content, news keywords, news category, publisher, and published datetime of the news.

The original intention of the repo is that when I develop algorithms of natural language processing, I find that most of them highly depends on large amount of high quality labeled data. However, it's very time-consuming and costly to collect large amount of high quality labeled data. In the same time, I find there's lots of labeled data in the news, just like (title, content) with (category, keywords). All of them are written by professional journalists, which contain large amount of high quality labeled data. All I need to do is to crawl the news. Therefore, this is the origin of the repo.

## QuickStart

### Installation
```
pip install Sanga
```

### Usage

- Crawl news info by news link
```
import Sanga as sg

news_crawler = sg.create_crawler(media_name="yahoo")

news = news_crawler.getInfo(link="https://tw.news.yahoo.com/%E9%98%B2%E7%96%AB%E9%81%8B%E5%B0%87%E5%82%B3%E9%9B%99%E5%8C%97%E5%85%A9%E9%82%8A%E8%B7%91%E8%BB%8A-%E8%BB%8A%E9%9A%8A%E5%90%A6%E8%AA%8D-224915749.html")
```

- Print news
```
print (news)

[TITLE   ]: 防疫運將傳雙北兩邊跑車 車隊否認
[CONTENT ]: 政府去年起推出防疫計程車，但有投訴人爆料，台灣大車隊旗下防疫司機利用台北及新北市管制空隙，30天後換市營業，迴避14天自主隔離規定。但北市交通局表示，若該司機健康無虞，且換到新北開防疫計程車，就沒有違反規定，如果是接送一般乘客，最高罰9萬元；台灣大車隊表示，都有嚴格排班，不會有台北司機跑到新北跑車的行為。 投訴人指出，防疫計程車駕駛需自主隔離14天，之後才能繼續接送居隔者，由於隔離完結束後半個月也就過去了，不少司機為能無痛接軌繼續開車賺錢，在北市及新北沒有互相比對防疫計程車駕駛名單下，台北30天跑完後，即刻轉往新北繼續載居隔者，質疑司機若確診，其足跡恐遍及雙北各角落。 台灣大車隊表示，台北防疫計程車及專責防疫計程車造冊司機，依規定上班30天，每天工作約6小時，防疫計程車專門載送採檢陰性的居家隔離者回家或到防疫旅館，專責防疫計程車載送採檢陽性的確診者至醫院，任務結束後需自主隔離14天。 台灣大車隊表示，原則上不會出現台北司機跑去新北載送居隔或確診者的情況，司機每天上班時，系統會啟動機器司機才能發車，自主隔離時，機器就會關閉，司機不可能有辦法開車載客。 交通局表示，過去疫情嚴峻時，雙北有協議可互相支援，不管防疫計程車司機是跑30天後，在家自主隔離14天，還是跑60天、90天後再隔離14天，只要做好防護，健康狀態無虞即可，倘若違規接送一般民眾，不管是台北司機去新北載送，還是新北司機到台北跑車，雙北市府可依照公路法規定，處業者9000元至9萬元。 更多udn報導在救護車大跳抖音引眾怒 正妹急救員遭批：難怪救不活我阿嬤待台積不到一年「只剩下工作」 過來人用這幾點勸離天龍國套房「只有1張床」 網見房租驚呆：根本糟蹋人！痛風不是吃止痛藥就好 醫揭尿酸超標對身體的危害我嚴防新冠肺炎新北增2例 基隆夜市人潮零距離首例機師「突破性感染」陳時中︰對社區影響小9/1開學 六都教職員須打疫苗或篩檢再進校園太太懷孕7個月「入境遭擋」 父歎不如外籍生台中港菲律賓籍船員確診 同船40人篩檢都陰性
[KEYWORDS]: ['計程車', '台灣大車隊', '自主隔離規定']
[CATEGORY]: None
[MEDIA   ]: Yahoo奇摩新聞
[DATETIME]: 2021-08-31T22:49:15.000Z
[LINK    ]: https://tw.news.yahoo.com/%E9%98%B2%E7%96%AB%E9%81%8B%E5%B0%87%E5%82%B3%E9%9B%99%E5%8C%97%E5%85%A9%E9%82%8A%E8%B7%91%E8%BB%8A-%E8%BB%8A%E9%9A%8A%E5%90%A6%E8%AA%8D-224915749.html
```

- Get news info (Check details in `Sanga::struct::NewsStruct`)
```
title = news.title
content = news.content
keywords = news.keywords
category = news.category
media = news.media
datetime = news.datetime
link = news.link
```

- Transform news struct into dictionary
```
news_dict = news.__2dict__()
```

- Write your own media crawler
```
import Sanga as sg
from Sanga.struct import NewsStruct

class CustomMediaNewsCrawler(sg.BaseMediaNewsCrawler):

    def getInfo(self, link: str) -> NewsStruct:

        ## Write your implementation

        raise NotImplementedError

news_crawler = CustomMediaNewsCrawler()
news = news_crawler.getInfo(link="xxxx")
```

### Supported Media


|    media    |  supported |  main url   |
|:-----------:|:----------:|:-----------:|
|  appledaily |    o <br> (content of past news are locked) | [蘋果日報](https://tw.appledaily.com) 
|   bcc       |    o       | [中國廣播公司](https://www.bcc.com.tw)
|   bnext     |    o       | [數位時代](https://www.bnext.com.tw) <br> [Meet創業小聚](https://meet.bnext.com.tw)
|  chinatimes |    o       | [中時新聞網](https://www.chinatimes.com)
|   cmmedia   |    o       | [信傳媒](https://www.cmmedia.com.tw)
|   cna       |    o       | [中央社](https://www.cna.com.tw)
|   cnews     |    o       | [匯流新聞網](https://cnews.com.tw)
|   ctee      |    o       | [工商時報](https://ctee.com.tw)
|   ctitv     |    o       | [中天新聞](https://gotv.ctitv.com.tw)
|   cts       |    o       |  [華視新聞](https://news.cts.com.tw)
|   ctv       |    x <br> (audio-visual) | [中視新聞](http://new.ctv.com.tw)
|   cynes     |    o       |  [鉅亨網](https://m.cnyes.com) <br> [鉅亨新聞網](https://news.cnyes.com)
|   digitimes |    o       |  [DigiTimes](https://www.digitimes.com.tw)
|   ebc       |    x <br> (contents are locked) | [東森財經新聞](https://fnc.ebc.net.tw)
|  epochtimes |    o       | [大紀元](https://www.epochtimes.com)
|   era       |    o       | [年代新聞](https://www.eracom.com.tw)
|   ettoday   |    o       | [ETtoday新聞雲](https://www.ettoday.net) <br> [ETtoday財經雲](https://finance.ettoday.net)
|   ftv       |    o       | [民視新聞](https://www.ftvnews.com.tw)
|   kairos    |    o       | [風向新聞](https://kairos.news)
|   ltn       |    o       | [自由時報電子報](https://news.ltn.com.tw) <br> [自由財經](https://ec.ltn.com.tw)
|   mirror    |    o       | [鏡週刊](https://www.mirrormedia.mg)
|   moneydj   |    o       | [MoneyDJ理財網](https://www.moneydj.com)
|   moneyudn  |    o       | [經濟日報](https://money.udn.com)
| mypeoplevol |    o       | [民眾新聞網](https://www.mypeoplevol.com)
|   newtalk   |    o       | [新頭殼](https://newtalk.tw)
|   nownews   |    o       | [今日新聞](https://www.nownews.com)
|   pchome    |    o       | [PChome新聞](https://news.pchome.com.tw)
|  peoplenews |    o       | [民報](https://www.peoplenews.tw)
|   pts       |    o       | [公視新聞](https://news.pts.org.tw)
|   rti       |    o       | [中央廣播電臺](https://www.rti.org.tw)
|   setn      |    o       | [三立新聞](https://www.setn.com)
|   sina      |    o       | [新浪新聞](https://news.sina.com.tw)
|   storm     |    o       | [風傳媒](https://www.storm.mg)
|   taiwanhot |    o       | [台灣好新聞](http://www.taiwanhot.net)
|   taronews  |    o       | [芋傳媒](https://taronews.tw)
|   technews  |    o       | [科技新報](https://technews.tw) <br> [財經新報](https://finance.technews.tw)
| thenewslens |    o       | [關鍵評論網](https://www.thenewslens.com) 
|   ttv       |    o       | [台視新聞](https://news.ttv.com.tw)
|   tvbs      |    o       | [TVBS](https://news.tvbs.com.tw)
|   udn       |    o       | [聯合新聞網](https://udn.com)
|   upmedia   |    o       | [上報](https://www.upmedia.mg)
|   ustv      |    o       | [非凡新聞](https://news.ustv.com.tw)
|   wealth    |    o       | [財訊](https://www.wealth.com.tw)
| worldjournal|    o       | [世界新聞網](https://www.worldjournal.com)
|   yahoo     |    o       | [Yahoo奇摩新聞](https://tw.news.yahoo.com) <br> [Yahoo奇摩股市](https://tw.stock.yahoo.com)
