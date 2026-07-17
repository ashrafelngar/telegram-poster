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
    "(القراصنة)",
    "أسود المجال 🦁💰",
    "sonaa el magal | صناع المجال",
    "حيتان الميديا 🔥🐺",
    "𝐒𝐄𝐋𝐋𝐄𝐑𝐒 𝐇𝐔𝐁 ☠️💸",
    "Social Madia Marketing",
    "صناع المآل // Money Makers 🔥",
    "بيع وشراء انستا يدوي فقط",
]

MESSAGE_1 = (
    "<b>💙🚀 تصميم مواقع احترافية 🚀💙</b>\n\n"
    "▫️<b>لاند بيدج (Landing Page)</b>\nصفحة جذابة لعرض منتج أو خدمة وتحويل الزوار لعملاء\n"
    "▫️<b>متجر إلكتروني (E-commerce)</b>\nمتجر متكامل لمنتجاتك من الصفر\n"
    "▫️<b>مواقع شركات (Business Website)</b>\nموقع احترافي يعزز ثقة العملاء في شركتك\n"
    "▫️<b>مواقع بورتفوليو (Portfolio)</b>\nعرض أعمالك ومشاريعك بشكل احترافي\n"
    "▫️<b>صفحات هبوط للحملات الإعلانية</b>\nصفحة مخصصة لحملاتك على فيسبوك وإنستغرام\n\n"
    "👀 مش لاقي اللي محتاجه؟ اسأل عليه وهظبطهولك\n"
    "<b>📲 كاش:</b> 01102394162"
)

MESSAGE_2 = (
    "<b>💙 خدمات 🚀💙</b>\n\n"
    "<b>🔗 ربط ورفع المواقع</b>\n"
    "▫️ رفع ملفات الموقع (Index) وربطها بالدومين\n"
    "▫️ إعداد وتجهيز الاستضافة بالكامل\n"
    "▫️ ضبط الـ DNS وربط الدومين صح\n\n"
    "<b>🌍 دومينات واستضافات</b>\n"
    "▫️ حجز دومينات بأفضل الأسعار\n"
    "▫️ استضافات بأفضل الأسعار\n\n"
    "    "▫️<b>إضافة موقعك على لوكيشن جوجل</b>\nبالاسم اللي تحبه عشان عملاؤك يلاقوك بسهولة\n"
    "▫️<b>تصميم هوية بصرية</b>\nلوجو + كروت شخصية + بروشور احترافي لبيزنسك\n\n"
    "👀 مش لاقي اللي محتاجه؟ اسأل عليه وهظبطهولك\n"
    "<b>📲 كاش:</b> 01102394162"
)

MESSAGE_3 = (
    "<b>💙🚀 خدمات السوشيال ميديا 🚀💙</b>\n\n"
    "👥 متابعين فيسبوك\n↳ أول 100 متابع = 3 جنيه 💸\n"
    "💬 لايكات وتعليقات\n↳ أول 100 تعليق = 30 جنيه 🔥\n"
    "📸 لايكات ومتابعين على: إنستغرام | تيك توك | واتساب | تويتر (X) | لينكدإن\n⚡ بأسعار حلوة + سرعة تنفيذ\n\n"
    "<b>🎯 حملات إعلانية شرعية (فيسبوك/تيك توك)</b>\nبأقل عمولة وأعلى نتائج\n"
    "<b>🛡️ قفل أو استرجاع حسابات فيسبوك المسروقة\n\n"
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

MESSAGES = [MESSAGE_1, MESSAGE_2, MESSAGE_3]

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


def is_target(name):
    if not name:
        return False
    for target in TARGET_GROUPS:
        if target.strip().lower() == name.strip().lower():
            return True
    return False


async def send_to_all(message):
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
    index = 0
    while True:
        message = MESSAGES[index % len(MESSAGES)]
        print("هنبعت البوست رقم " + str((index % len(MESSAGES)) + 1))
        await send_to_all(message)
        index += 1
        await asyncio.sleep(HOURS * 60 * 60)


asyncio.run(main())
