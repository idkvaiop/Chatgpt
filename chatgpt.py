from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice

from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
This is ChatGPT AI Telegram Bot!
I can help you with your doubts as much as possible, give me try ❤️

Use /ask {your question} 


"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
axx = bytearray.fromhex("49  54 7A 5F 4C 45 47 45 4E 44 5F 43 4F 44 45 52").decode()
xxc = bytearray.fromhex("4D 52 5F 53 55 4B 4B 55 4E").decode()
SOURCE = xa
UPDATE_CHNL = xxc
DEVELOPER = axx
SOURCE_TEXT = f"""
Hello, This is [{BOT_NAME}. My source code is private but if you are interested to buy, contact @ArsanikBolte!
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="Updates", url=f"https://t.me/ChatGPT_TG4"),
        InlineKeyboardButton(text="Support ", url=f"https://t.me/ChatGPT_TG4"),
    ]
    
    
PNG_BTN = [
   
     [
         InlineKeyboardButton(text="Update", 
                              url=f"https://t.me/ChatGPT_TG4",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('Source', url=f"{SOURCE}")]])
HELP_READ = "Do it by /ChatGPT {question} or /ask {question}"
HELP_BACK = [
     [
           InlineKeyboardButton(text="Question That ChatGPT can solve  ", url=f"https://t.me/ChatGPT_TG4/66"),
           
     ],
    [
           InlineKeyboardButton(text="Back ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Mukesh.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("Welcome...")
        await asyncio.sleep(0.2)
        await accha.delete()
       
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_text(
                        text = HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping","alive"], prefixes=["","+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "pinging..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("pinging.....")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"Hello!\n[{BOT_NAME}](t.me/{BOT_USERNAME}) is alive and working with speed of \n- `{ms}` ms\n\n",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt What is AI?`")
        else:

            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2,
)

            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " MS"
            await message.reply_text(f"{message.from_user.first_name} ASKED:\n\n {a} \n\n {BOT_NAME} Answered:-\n\n {x}\n\nTime Taken {telegram_ping} \n\nPowered by @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**Error:    {e} ")


s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
u = bytearray.fromhex("49  54 7A 5F 4C 45 47 45 4E 44 5F 43 4F 44 45 52").decode()
d= bytearray.fromhex("4D 52 5F 53 55 4B 4B 55 4E").decode()
if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Noob-mukesh/Chatgpt-bot `  else I won't work")
    sys.exit(1)  
if DEVELOPER!=u:
    print("So sad, you have changed Updates, change it back to `ITz_LEGEND_CODER ` else I won't work")
    sys.exit(1)
if UPDATE_CHNL!=d:
    print("So sad, you have change developer, change it back to `MR_SUKKUN ` else I won't work")
    sys.exit(1)


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @ChatGPT_TG4
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
