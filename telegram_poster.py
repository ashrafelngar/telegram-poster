from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import Channel, Chat
import asyncio
import os

# ============================
# بيانات من Environment Variables
# ============================
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

MESSAGE = """عندنا كل خدمات السوشيال ميديا💙🚀
✨ خدماتنا:
🔹 تزويد متابعين فيسبوك 👥
👉 من أول 100 متابع = 3 جنيه 💸
🔹 لايكات 👍 وتعليقات 💬
👉 من أول 100 تعليق = 30 جنيه 🔥
🔹 لايكات ومتابعين على:
📸 إنستغرام
🎵 تيك توك
💬 واتساب
🐦 تويتر (X)
🌐 لينكدإن
⚡ بأسعار حلوة + سرعة تنفيذ
🔹 شحن عملات تيك توك 🎁🔥
🔹 نجوم فيسبوك ⭐
🔹اشتراك جيميناي { برو }
🔹 تفعيل اشتراك CapCut Pro 🎬
🔹 Canva Pro 🎨
👉 3 سنين = 30 جنيه 😍
🔹 اشتراك Perplexity AI 🤖🧠
🔹 نشر أخبار في جرائد 📰
🔹 وخدمات سوشيال ميديا تانية كتير 🚀
👀 في خدمات مش مضافة… اسأل عليها
📲 أي خدمة محتاجها؟
كلمني وهظبطهالك فورًا وبأفضل سعر 💪💙
ك 01102394162"""

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
                f"<blockquote>{MESSAGE}</blockquote>",
                parse_mode="html"
            )
            print(f"✅ تم: {dialog.name}")
            success += 1
            await asyncio.sleep(3)
        except Exception as e:
            print(f"❌ فشل: {dialog.name} | {e}")
            failed += 1
    print(f"\n📊 {success} نجح | {failed} فشل")
    print(f"⏳ هنبعت تاني بعد {HOURS} ساعة\n")

async def main():
    await client.connect()
    print("✅ اتصلنا بتلجرام!")
    while True:
        await send_to_all()
        await asyncio.sleep(HOURS * 60 * 60)

asyncio.run(main())
    "Social Media Services",
    "☬ عتاوله 💵 المجال",
    "𝑲𝒐𝒓𝒐𝒏𝒂𝒎𝒊 𝑮𝒓𝒐𝒖𝒑 ⚔️",
    "NoOor Elzeny 🌹",
    "ماركت ميديا ..🥇",
    "محترفين المجال",
    "𝕂𝕚𝕟𝕘𝕤 𝕄𝕖𝕥𝕙𝕠𝕕𝕤 👑 ملوك التسويق",
    "Social mony💰",
]

# ============================
# 📝 نص البوست
# ============================
MESSAGE = """عندنا كل خدمات السوشيال ميديا💙🚀
✨ خدماتنا:
🔹 تزويد متابعين فيسبوك 👥
👉 من أول 100 متابع = 3 جنيه 💸
🔹 لايكات 👍 وتعليقات 💬
👉 من أول 100 تعليق = 30 جنيه 🔥
🔹 لايكات ومتابعين على:
📸 إنستغرام
🎵 تيك توك
💬 واتساب
🐦 تويتر (X)
🌐 لينكدإن
⚡ بأسعار حلوة + سرعة تنفيذ
🔹 شحن عملات تيك توك 🎁🔥
🔹 نجوم فيسبوك ⭐
🔹اشتراك جيميناي { برو }
🔹 تفعيل اشتراك CapCut Pro 🎬
🔹 Canva Pro 🎨
👉 3 سنين = 30 جنيه 😍
🔹 اشتراك Perplexity AI 🤖🧠
🔹 نشر أخبار في جرائد 📰
🔹 وخدمات سوشيال ميديا تانية كتير 🚀
👀 في خدمات مش مضافة… اسأل عليها
📲 أي خدمة محتاجها؟
كلمني وهظبطهالك فورًا وبأفضل سعر 💪💙
ك 01102394162"""

# ============================
# 🚀 السكريبت
# ============================
client = TelegramClient("session", API_ID, API_HASH)

def is_target(name):
    """يتحقق لو الجروب في القائمة المستهدفة"""
    if not name:
        return False
    name = name.strip()
    for target in TARGET_GROUPS:
        if target.strip().lower() == name.lower():
            return True
    return False

async def send_to_all():
    success = 0
    failed = 0
    not_found = list(TARGET_GROUPS)

    async for dialog in client.iter_dialogs():
        if not isinstance(dialog.entity, (Channel, Chat)):
            continue
        if not is_target(dialog.name):
            continue

        # أزل من قائمة المش متلاقيين
        for t in TARGET_GROUPS:
            if t.strip().lower() == dialog.name.strip().lower():
                if t in not_found:
                    not_found.remove(t)

        try:
            await client.send_message(
                dialog.entity,
                f"<blockquote>{MESSAGE}</blockquote>",
                parse_mode="html"
            )
            print(f"✅ تم الإرسال لـ: {dialog.name}")
            success += 1
            await asyncio.sleep(3)
        except Exception as e:
            print(f"❌ فشل: {dialog.name} | {e}")
            failed += 1

    print(f"\n📊 النتيجة: {success} نجح | {failed} فشل")
    if not_found:
        print(f"\n⚠️ مش لاقيهم ({len(not_found)}):")
        for g in not_found:
            print(f"   - {g}")
    print(f"\n⏳ هنبعت تاني بعد {HOURS} ساعة...\n")

async def main():
    await client.start(phone=PHONE)
    print("✅ اتصلنا بتلجرام بنجاح!")
    print(f"🎯 هنبعت لـ {len(TARGET_GROUPS)} جروب محدد")
    print(f"🚀 الإرسال التلقائي كل {HOURS} ساعة\n")

    while True:
        await send_to_all()
        await asyncio.sleep(HOURS * 60 * 60)

with client:
    client.loop.run_until_complete(main())
