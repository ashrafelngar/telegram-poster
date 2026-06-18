import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import Channel, Chat

API_ID = 28324761
API_HASH = "9c0162ea1486f6fce31813f51ef9af07"
SESSION_STRING = os.environ.get("SESSION_STRING", "")
HOURS = 1

TARGET_GROUPS = [
    "خدمات سوشيال ميديا",
    "تسويق سوشيال ميديا Vip🐋👑✌",
    "Online-اون لاين",
    "يلا ماركتينج | Yalla Marketing",
    "Easy money 🔝",
    "بيع وشراء بيدحات فيس بوك",
    "أسود المجال Vip",
    "♦️El-Komy♦️ 🔰Cafe Al-Majal🔰 💲🌐💠🔱🔞🔞📛🚷♨️💯٩",
    "✨ELMAMLKA المملكة🏦",
    "الحيتان",
    "(القراصنة)",
    "World Market 🌏",
    "حيتان 🐋المجال 🔥",
    "صناع المال Money makers 💰",
    "سوشيال ميديا",
    "الأرزاق بيد الله ❤️🤝",
    "Social Media Services",
    "☬ عتاوله 💵 المجال",
    "𝑲𝒐𝒓𝒐𝒏𝒂𝒎𝒊 𝑮𝒓𝒐𝒖𝒑 ⚔️",
    "NoOor Elzeny 🌹",
    "ماركت ميديا ..🥇",
    "محترفين المجال",
    "𝕂𝕚𝕟𝕘𝕤 𝕄𝕖𝕥𝕙𝕠𝕕𝕤 👑 ملوك التسويق",
    "Social mony💰",
]

MESSAGE = (
    "عندنا كل خدمات السوشيال ميديا💙🚀\n"
    "✨ خدماتنا:\n"
    "🔹 تزويد متابعين فيسبوك 👥\n"
    "👉 من أول 100 متابع = 3 جنيه 💸\n"
    "🔹 لايكات 👍 وتعليقات 💬\n"
    "👉 من أول 100 تعليق = 30 جنيه 🔥\n"
    "🔹 لايكات ومتابعين على:\n"
    "📸 إنستغرام\n"
    "🎵 تيك توك\n"
    "💬 واتساب\n"
    "🐦 تويتر (X)\n"
    "🌐 لينكدإن\n"
    "⚡ بأسعار حلوة + سرعة تنفيذ\n"
    "🔹 شحن عملات تيك توك 🎁🔥\n"
    "🔹 نجوم فيسبوك ⭐\n"
    "🔹اشتراك جيميناي { برو }\n"
    "🔹 تفعيل اشتراك CapCut Pro 🎬\n"
    "🔹 Canva Pro 🎨\n"
    "👉 3 سنين = 30 جنيه 😍\n"
    "🔹 اشتراك Perplexity AI 🤖🧠\n"
    "🔹 نشر أخبار في جرائد 📰\n"
    "🔹 وخدمات سوشيال ميديا تانية كتير 🚀\n"
    "👀 في خدمات مش مضافة… اسأل عليها\n"
    "📲 أي خدمة محتاجها؟\n"
    "كلمني وهظبطهالك فورًا وبأفضل سعر 💪💙\n"
    "ك 01102394162"
)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


def is_target(name):
    if not name:
        return False
    for target in TARGET_GROUPS:
        if target.strip().lower() == name.strip().lower():
            return True
    return False


async def send_to_all():
    success = 0
    failed = 0
    async for dialog in client.iter_dialogs():
        if not isinstance(dialog.entity, (Channel, Chat)):
            continue
        if not is_target(dialog.name):
            continue
        try:
            await client.send_message(
                dialog.entity,
                "<blockquote>" + MESSAGE + "</blockquote>",
                parse_mode="html"
            )
            print("تم: " + dialog.name)
            success += 1
            await asyncio.sleep(3)
        except Exception as e:
            print("فشل: " + dialog.name + " | " + str(e))
            failed += 1
    print(str(success) + " نجح | " + str(failed) + " فشل")
    print("هنبعت تاني بعد " + str(HOURS) + " ساعة")


async def main():
    await client.connect()
    print("اتصلنا بتلجرام!")
    while True:
        await send_to_all()
        await asyncio.sleep(HOURS * 60 * 60)


asyncio.run(main())
