import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import Channel, Chat

API_ID = 28324761
API_HASH = "9c0162ea1486f6fce31813f51ef9af07"
SESSION_STRING = os.environ.get("SESSION_STRING", "")

HOURS_MESSAGE_1 = 1    # الرسالة الأولى كل 1 ساعة
HOURS_MESSAGE_2 = 2.5  # الرسالة الثانية كل ساعتين ونصف (2.5 ساعة)

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
    "𝕂𝕚ℕgings 𝕄𝕖𝕥𝕙𝕠𝕕𝕤 👑 ملوك التسويق",
    "Social mony💰",
    "(القراصنة)",
    "أسود المجال 🦁💰",
    "💰 Money Makers صناع المال",
    "حيتان الميديا 🔥🐺",
    "𝐒𝐄𝐋𝐋𝐄R𝐒 𝐇𝐔𝐁 ☠️💸",
    "Social Madia Marketing",
    "صناع المآل // Money Makers 🔥",
    "بيع وشراء انستا يدوي فقط",
    "Mlook Marketing 👑 ملوك ماركتنج", 
    "𝐒𝐄𝐋𝐋𝐄𝐑𝐒 𝐇𝐔𝐁 ☠️💸", 
    "𝕂𝕚𝕟𝕘𝕤 𝕄𝕖𝕥𝕙𝕠𝕕𝕤 👑 ملوك التسويق", 
]

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


def is_target(name):
    if not name:
        return False
    for target in TARGET_GROUPS:
        if target.strip().lower() == name.strip().lower():
            return True
    return False


async def forward_or_send_custom(msg_obj, msg_name):
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
                msg_obj.message,
                formatting_entities=msg_obj.entities
            )
            print(f"[{msg_name}] تم النشر في: {dialog.name}")
            success += 1
            await asyncio.sleep(3)
        except Exception as e:
            print(f"[{msg_name}] فشل في: {dialog.name} | {e}")
            failed += 1
    print(f"--- [{msg_name}] النتيجة: {success} نجح | {failed} فشل ---")


async def task_message_1():
    while True:
        print("🚀 جلب الرسالة الأولى من 'الرسائل المحفوظة'...")
        async for msg in client.iter_messages('me', limit=5):
            if msg.text and "خدمات السوشيال" in msg.text:
                await forward_or_send_custom(msg, "الرسالة الأولى")
                break
        print(f"سيتكرر إرسال الرسالة الأولى بعد {HOURS_MESSAGE_1} ساعة.")
        await asyncio.sleep(int(HOURS_MESSAGE_1 * 3600))


async def task_message_2():
    while True:
        print("💳 جلب الرسالة الثانية من 'الرسائل المحفوظة'...")
        async for msg in client.iter_messages('me', limit=5):
            if msg.text and "كروت باي بيت" in msg.text:
                await forward_or_send_custom(msg, "الرسالة الثانية")
                break
        print(f"سيتكرر إرسال الرسالة الثانية بعد {HOURS_MESSAGE_2} ساعة (ساعتين ونصف).")
        await asyncio.sleep(int(HOURS_MESSAGE_2 * 3600))


async def main():
    await client.connect()
    print("اتصلنا بتلجرام بنجاح!")
    
    asyncio.create_task(task_message_1())
    asyncio.create_task(task_message_2())
    
    await asyncio.Event().wait()


asyncio.run(main())

