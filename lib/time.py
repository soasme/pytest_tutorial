# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

def yesterdaytime(time):
    if isinstance(time, str):
        try:
            time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pass
    now = datetime.now()
    timedelta(days=1)
    if str(time)[:10] == str(now)[:10]:
        return "今天"
    elif str(now-timedelta(days=1))[:10] == str(time)[:10]:
        return "昨天"
    elif now.year == time.year:
        return "%s月%s日" % (time.month, time.day)
    else:
        return "%s年%s月%s日" % (time.year, time.month, time.day)

def mtimeformat(time, show_furthor=False):
    d = datetime.now() - time
    now = datetime.now()
    if str(time)[:10] != str(now)[:10]:
        return show_furthor and yesterdaytime(time) or ''
    elif d.seconds < 3600:
        f = int(d.seconds/60)
        if f == 0:
            return "刚刚"
        else:
            return "%s分钟前" % f
    elif d.seconds < 10800:
        return "%s小时前" % int(d.seconds/3600)
    else:
        return 0 <= time.hour < 6 and "今天凌晨" or 6 <= time.hour < 12 and "今天上午" or 12 <= time.hour < 18 and "今天下午" or 18 <= time.hour < 24 and "今天晚上"
