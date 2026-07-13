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

MESSAGE = (
    "💙🚀 كل خدمات الويب والسوشيال ميديا هتلاقيها هنا 🚀💙\n\n"
"🌐 تصميم مواقع احترافية\n\n"
"▫️لاند بيدج (Landing Page)\nتصميم صفحة جذابة لعرض منتج أو خدمة وتحويل الزوار لعملاء\n\n"
"▫️ متجر إلكتروني (E-commerce)\nتصميم متجر متكامل لمنتجاتك (أحذية، ملابس، إكسسوارات... إلخ) من الصفر\n\n"
"▫️ مواقع شركات (Business Website)\nموقع احترافي يعرض خدماتك وتعزيز ثقة العملاء في شركتك\n\n"
"▫️ مواقع بورتفوليو (Portfolio)\nموقع لعرض أعمالك ومشاريعك بشكل احترافي يجذب العملاء\n\n"
"▫️ صفحات هبوط للحملات الإعلانية\nصفحة مخصصة لحملاتك الإعلانية على فيسبوك وإنستغرام لزيادة المبيعات\n\n"
"🔗 ربط ورفع المواقع\n"
"▫️ رفع ملفات الموقع (Index) وربطها بالدومين\n"
"▫️ إعداد وتجهيز الاستضافة بالكامل\n"
"▫️ ضبط الـ DNS وربط الدومين صح\n\n"
"🌍 دومينات واستضافات\n"
"▫️ حجز دومينات بأفضل الأسعار\n"
"▫️ استضافات بأفضل الأسعار\n\n"
"▫️ 📍إضافة موقعك على لوكيشن جوجل\nبالاسم اللي تحبه عشان عملاؤك يلاقوك بسهولة\n\n"
"▫️ تصميم هوية بصرية\nلوجو + كروت شخصية + بروشور احترافي لبيزنسك\n\n"
"━━━━━━━━━━━━━━\n\n"
"✨ خدمات السوشيال ميديا ✨\n\n"
"👥 متابعين فيسبوك\n↳ أول 100 متابع = 3 جنيه 💸\n\n"
"💬 لايكات وتعليقات\n↳ أول 100 تعليق = 30 جنيه 🔥\n\n"
"📸 لايكات ومتابعين على:\nإنستغرام | تيك توك | واتساب | تويتر (X) | لينكدإن\n⚡ بأسعار حلوة + سرعة تنفيذ\n\n"
"🎯 حملات إعلانية رسمية (فيسبوك/تيك توك)\nبأقل عمولة وأعلى نتائج\n\n"
"🛡️ قفل أو استرجاع حسابات فيسبوك/المسروقة\n\n"
"🎁 شحن عملات تيك توك\n"
"⭐ نجوم فيسبوك\n"
"🤖 اشتراك Gemini Pro\n"
"🎬 تفعيل CapCut Pro\n"
"🎨 Canva Pro (3 سنين) = 30 جنيه\n"
"🧠 اشتراك Perplexity AI\n"
"📰 نشر أخبار في جرائد\n"
"🚀 خدمات تانية كتير...\n\n"
"👀 مش لاقي اللي محتاجه؟ اسأل عليه وهظبطهولك\n\n"
"━━━━━━━━━━━━━━\n\n"
"📲 كاش:\n01102394162" 
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
