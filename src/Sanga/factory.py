# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Factory pattern for MediaNewsCrawler

import logging
from .media import (
    appledaily,
    bcc,
    bnext,
    chinatimes,
    cmmedia,
    cna,
    cnews,
    ctee,
    ctitv,
    cts,
    ctv,
    cnyes,
    digitimes,
    ebc,
    epochtimes,
    eracom,
    ettoday,
    ftvnews,
    kairos,
    ltn,
    mirrormedia,
    moneydj,
    moneyudn,
    mypeoplevol,
    newtalk,
    nownews,
    pchome,
    peoplenews,
    pts,
    rti,
    setn,
    sina,
    storm,
    taiwanhot,
    taronews,
    technews,
    thenewslens,
    ttv,
    tvbs,
    udn,
    upmedia,
    ustv,
    wantrich,
    wealth,
    worldjournal,
    yahoo,
)

logger = logging.getLogger(__name__)


def MediaNewsCrawlerFactory(media_name: str):

    LOCALIZERS = {
        "appledaily": appledaily.AppleDaily,
        "bcc": bcc.BCC,
        "bnext": bnext.BNEXT,
        "chinatimes": chinatimes.Chinatimes,
        "cmmedia": cmmedia.CMMedia,
        "cna": cna.CNA,
        "cnews": cnews.CNews,
        "ctee": ctee.CTEE,
        "ctitv": ctitv.CTITV,
        "cts": cts.CTS,
        "ctv": ctv.CTV,
        "cnyes": cnyes.CNYES,
        "digitimes": digitimes.DigiTimes,
        "ebc": ebc.EBC,
        "epochtimes": epochtimes.EpochTimes,
        "eracom": eracom.ERACOM,
        "ettoday": ettoday.ETtoday,
        "ftvnews": ftvnews.FTVNews,
        "kairos": kairos.Kairos,
        "ltn": ltn.LTN,
        "mirrormedia": mirrormedia.MirrorMedia,
        "moneydj": moneydj.MoneyDJ,
        "money.udn": moneyudn.MoneyUDN,
        "mypeoplevol": mypeoplevol.MyPeopleVol,
        "newtalk": newtalk.NewTalk,
        "nownews": nownews.NowNews,
        "pchome": pchome.PChome,
        "peoplenews": peoplenews.PeopleNews,
        "pts": pts.PTS,
        "rti": rti.RTI,
        "setn": setn.SETN,
        "sina": sina.SINA,
        "storm": storm.Storm,
        "taiwanhot": taiwanhot.TaiwanHot,
        "taronews": taronews.TaroNews,
        "technews": technews.TechNews,
        "thenewslens": thenewslens.TheNewsLens,
        "ttv": ttv.TTV,
        "tvbs": tvbs.TVBS,
        "udn": udn.UDN,
        "upmedia": upmedia.UpMedia,
        "ustv": ustv.USTV,
        "wantrich": wantrich.WantRich,
        "wealth": wealth.Wealth,
        "worldjournal": worldjournal.WorldJournal,
        "yahoo": yahoo.Yahoo,
    }
    return LOCALIZERS[media_name]()