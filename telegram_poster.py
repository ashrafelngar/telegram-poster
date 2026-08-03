import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import Channel, Chat

API_ID = 28324761
API_HASH = "9c0162ea1486f6fce31813f51ef9af07"
SESSION_STRING = os.environ.get("SESSION_STRING", "")

# تحديد أوقات النشر (بالساعات)
HOURS_MESSAGE_1 = 1  # الرسالة الأولى كل 1 ساعة
HOURS_MESSAGE_2 = 3  # الرسالة الثانية كل 3 ساعات

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
    "𝕂𝕚𝕟gings 𝕄𝕖𝕥𝕙𝕠𝕕𝕤 👑 ملوك التسويق",
    "Social mony💰",
    "(القراصنة)",
    "أسود المجال 🦁💰",
    "💰 Money Makers صناع المال",
    "حيتان الميديا 🔥🐺",
    "𝐒𝐄𝐋𝐋𝐄𝐑𝐒 𝐇𝐔𝐁 ☠️💸",
    "Social Madia Marketing",
    "صناع المآل // Money Makers 🔥",
    "بيع وشراء انستا يدوي فقط",
]

MESSAGE_1 = (
    "<b>💙🚀 خدمات السوشيال ميديا 🚀💙</b>\n\n"
    "👥 متابعين فيسبوك\n↳ أول 100 متابع = 3 جنيه 💸\n"
    "💬 لايكات وتعليقات\n↳ أول 100 تعليق = 30 جنيه 🔥\n"
    "📸 لايكات ومتابعين على: إنستغرام | تيك توك | واتساب | تويتر (X) | لينكدإن\n⚡ بأسعار حلوة + سرعة تنفيذ\n\n"
    "<b>🎯 حملات إعلانية شرعية (فيسبوك/تيك توك)</b>\nبأقل عمولة وأعلى نتائج\n"
    "<b>🛡️ قفل أو استرجاع حسابات فيسبوك المسروقة</b>\n\n"
    "🎁 شحن عملات تيك توك\n"
    "⭐ نجوم فيسبوك\n"
    "🤖 اشتراك Gemini Pro\n"
    "🎬 تفعيل CapCut Pro\n"
    "🎨 Canva Pro (3 سنين) = 30 جنيه\n"
    "🧠 اشتراك Perplexity AI\n"
    "📰 نشر أخبار في جرائد\n"
    "🚀 خدمات تانية كتير...\n\n"
    "👀 مش لاقي اللي محتاجه؟ اسأل عليه وهظبطهولك\n"
    "<b>📲 كاش:</b> 01102394162"
)

MESSAGE_2 = (
    "موجود كروت باي بيت Bybit فريش 🔥\n\n"
    "متوفر فيزا 30 جنيه ✅\n"
    "متوفر مستر 40 جنيه ✅\n\n"
    "الفيزا بتطلع ليك فريش بدقيقة ❤️\n"
    "وصلاحية 24 ساعة كاملين 🔥\n\n"
    "<b>📲 للتواصل كاش:</b> 01102394162"
)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


def is_target(name):
    if not name:
        return False
    for target in TARGET_GROUPS:
        if target.strip().lower() == name.strip().lower():
            return True
    return False


async def send_to_all(message, msg_name):
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
                "<blockquote>" + message + "</blockquote>",
                parse_mode="html"
            )
            print(f"[{msg_name}] تم النشر في: {dialog.name}")
            success += 1
            await asyncio.sleep(3)
        except Exception as e:
            print(f"[{msg_name}] فشل في: {dialog.name} | {e}")
            failed += 1
    print(f"--- [{msg_name}] النتيجة: {success} نجح | {failed} فشل ---")


# مهمة الرسالة الأولى (كل ساعة)
async def task_message_1():
    while True:
        print("🚀 بدء إرسال الرسالة الأولى (خدمات السوشيال)...")
        await send_to_all(MESSAGE_1, "الرسالة الأولى")
        print(f"سيتكرر إرسال الرسالة الأولى بعد {HOURS_MESSAGE_1} ساعة.")
        await asyncio.sleep(HOURS_MESSAGE_1 * 3600)


# مهمة الرسالة الثانية (كل 3 ساعات)
async def task_message_2():
    while True:
        print("💳 بدء إرسال الرسالة الثانية (كروت باي بيت)...")
        await send_to_all(MESSAGE_2, "الرسالة الثانية")
        print(f"سيتكرر إرسال الرسالة الثانية بعد {HOURS_MESSAGE_2} ساعات.")
        await asyncio.sleep(HOURS_MESSAGE_2 * 3600)


async def main():
    await client.connect()
    print("اتصلنا بتلجرام بنجاح!")
    
    # تشغيل المهام في الخلفية بشكل مستقل بدون أن تتعارض مع بعضها
    asyncio.create_task(task_message_1())
    asyncio.create_task(task_message_2())
    
    # الإبقاء على البوت يعمل بشكل مستمر
    await asyncio.Event().wait()


asyncio.run(main())

