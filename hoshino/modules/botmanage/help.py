from hoshino import Service, priv
from hoshino.typing import CQEvent

sv = Service('_help_', manage_priv=priv.SUPERUSER, visible=False)

<<<<<<< HEAD
TOP_MANUAL = '''
=====================
- HoshinoBot使用说明 -
=====================
发送方括号[]内的关键词即可触发
※功能采取模块化管理，群管理可控制开关

[!帮助] 会战管理v2
[怎么拆日和] 竞技场查询
[星乃来发十连] 转蛋模拟
[pcr速查] 常用网址
[官漫132] 四格漫画（日）
[切噜一下] 切噜语转换
[lssv] 查看功能模块的开关状态（群管理限定）
[来杯咖啡] 联系维护组

发送以下关键词查看更多：
[帮助pcr会战]
[帮助pcr查询]
[帮助pcr娱乐]
[帮助pcr订阅]
[帮助kancolle]
[帮助通用]
========
※除这里中写明外 另有其他隐藏功能:)
※隐藏功能属于赠品 不保证可用性
※本bot开源，可自行搭建
※服务器运行及开发维护需要成本，赞助支持请私戳作者
※您的支持是本bot更新维护的动力
※※调教时请注意使用频率，您的滥用可能会导致bot账号被封禁
'''.strip()

def gen_bundle_manual(bundle_name, service_list, gid):
    manual = [bundle_name]
    service_list = sorted(service_list, key=lambda s: s.name)
    for sv in service_list:
        if sv.visible:
            spit_line = '=' * max(0, 18 - len(sv.name))
            manual.append(f"|{'○' if sv.check_enabled(gid) else '×'}| {sv.name} {spit_line}")
            if sv.help:
                manual.append(sv.help)
    return '\n'.join(manual)


@sv.on_prefix(('help', '帮助', '幫助'))
async def send_help(bot, ev: CQEvent):
    bundle_name = ev.message.extract_plain_text().strip()
    bundles = Service.get_bundles()
    if not bundle_name:
        await bot.send(ev, TOP_MANUAL)
    elif bundle_name in bundles:
        msg = gen_bundle_manual(bundle_name, bundles[bundle_name], ev.group_id)
        await bot.send(ev, msg)
    # else: ignore
=======
MANUAL = '''
============================================
           - 优衣酱の小工具 -
============================================
输入方括号[]内的关键词即可触发相应的功能
※注意其中的【空格】不可省略！
※下面命令中@bot就是艾特我

[@bot来发十连] 十连转蛋模拟
[@bot来发单抽] 单抽转蛋模拟
[@bot来一井] 4w5钻！买定离手！
[@bot妈] 让妈给主人盖章章
[查看卡池] 查看bot现在的卡池及出率
[怎么拆 妹弓] 后以空格隔开接角色名，查询竞技场解法
[rank表] 查看rank推荐表
[pcr速查] 常用网址/速查表
[bcr速查] B服萌新攻略
[@bot官漫132] 官方四格阅览
[启用 pcr-arena-reminder-tw] 背刺时间提醒(UTC+8)
[挖矿 15001] 查询矿场中还剩多少钻
[切噜一下] 后以空格隔开接想要转换为切噜语的话
[切噜～♪切啰巴切拉切蹦切蹦] 切噜语翻译
[翻译 文字]将文字翻译成中文

涩图/萌图功能：
※在发的消息里一句话里只要出现“涩图”或“瑟图”即可获取色图
※在发的消息里一句话里只要出现“萌图”即可获取萌图
※在发的消息里一句话里只要出现“随机老婆”即可获取公主连结画册中的图
============================================
'''.strip()

@sv.on_command('help', aliases=('Help'), only_to_me=False)
async def send_help(session):
    await session.send(MANUAL)
>>>>>>> custom modification
