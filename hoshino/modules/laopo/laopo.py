import os
import re
import time
import random

from nonebot import on_command, CommandSession, MessageSegment, NoneBot
from nonebot.exceptions import CQHttpError

from hoshino import R, Service, Privilege
from hoshino.util import FreqLimiter, DailyNumberLimiter

_max = 10
EXCEED_NOTICE = f'您今天已经要{_max}次老婆了，再这样下去要犯法的，明早5点后再来叭'
_nlmt = DailyNumberLimiter(_max)
_flmt = FreqLimiter(5)

sv = Service('laopo', manage_priv=Privilege.SUPERUSER, enable_on_default=True, visible=False)
setu_folder = R.img('laopo/').path

def setu_gener():
    while True:
        filelist = os.listdir(setu_folder)
        random.shuffle(filelist)
        for filename in filelist:
            if os.path.isfile(os.path.join(setu_folder, filename)):
                yield R.img('laopo/', filename)

setu_gener = setu_gener()

def get_setu():
    return setu_gener.__next__()


@sv.on_rex(re.compile(r'随机老婆'), normalize=True)
async def setu(bot:NoneBot, ctx, match):
    """随机叫一个老婆，对每个用户有冷却时间"""
    uid = ctx['user_id']
    if not _nlmt.check(uid):
        await bot.send(ctx, EXCEED_NOTICE, at_sender=True)
        return
    if not _flmt.check(uid):
        await bot.send(ctx, '您要得太快了，老婆们忙不过来了，稍后再来吧', at_sender=True)
        return
    _flmt.start_cd(uid)
    _nlmt.increase(uid)

    # conditions all ok, send a setu.
    pic = get_setu()
    try:
        await bot.send(ctx, pic.cqcode)
    except CQHttpError:
        sv.logger.error(f"发送图片{pic.path}失败")
        try:
            await bot.send(ctx, '老婆太可爱了，优衣酱都发不出去了呢...')
        except:
            pass
