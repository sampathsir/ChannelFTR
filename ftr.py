# Channel Forward Tag Remover - Channel management bot
# Copyright (C) 2021 @Alain_xD
#
# This file is a part of < https://github.com/BotzCity/ChannelFTR/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/BotzCity/ChannelFTR/blob/main/LICENSE/>.

import re, os, random, asyncio, html
os.system("pip install pyrogram")
import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

but = InlineKeyboardMarkup([[InlineKeyboardButton("Help 🤔", callback_data="Help"), InlineKeyboardButton("Close 🔐", callback_data="close")],[InlineKeyboardButton("Updates ⬆", url="https://t.me/sinnerBots"), InlineKeyboardButton("Developer", url="Satan_sinx")]])
butt = InlineKeyboardMarkup([[InlineKeyboardButton("Home 🏠", callback_data="home"), InlineKeyboardButton("Updates ⬆", url="https://t.me/sinnerbots")], [InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url="https://t.me/The_Sinners_Empire"), InlineKeyboardButton("Close 🔐", callback_data="close")]])


@app.on_message(filters.command(["start"]))
async def start(lel, message):
    await message.reply_text(f"**Hi** `{message.from_user.first_name}` **!\n\nI'm Channel forward tag remover! I can send the file // messages which is forwarded in your channel without forward tag.🤩..!**", reply_markup=but)

@app.on_message(filters.command(["help"]))
async def help(ha, message):
    await app.send_message(message.chat.id, """**There is nothing no more..!\nJust add me to your channel give rights to delete message and post messages and whichever forwarded message received I will send again without forward tag.\n\nMade with ❤️ by @Satan_sinx**""", reply_markup=butt) 

@app.on_callback_query()
async def button(app, update):
    k = update.data
    if "Help" in k:
       await update.message.delete()
       await help(app, update.message)
    elif "close" in k:
       await update.message.delete()
    elif "home" in k:
       await update.message.delete()
       await start(app, update.message)

@app.on_message(filters.channel & filters.forwarded)
async def copy(sed, message):
    try:
       sed = await message.copy(message.chat.id)
       await message.delete()
    except RCPError as lel:
       await message.reply(lel)
       return


print("Started bot...! ") 
print("Join @sinnerbots for any help !")
app.run()
