from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneX import app
from config import BOT_USERNAME
#from AloneX.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
𝐂ʜᴀʟᴀ 𝐉ᴀᴀ 𝐁ʜᴏsᴅɪᴋᴇ 𝐑ᴇᴘᴏ 𝐏ʀɪᴠᴀᴛᴇ 𝐇ᴀɪ..
**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⌯ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ⌯", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("⌯ 𝐒ᴜᴘᴘᴏʀᴛ ⌯", url=f"https://t.me/+cy6Q9WPYkfs0OGNl"),
          InlineKeyboardButton("⌯ 𝐔ᴘᴅᴀᴛᴇs ⌯", url="https://t.me/shubhos_timeline"),
          ],
               [
                InlineKeyboardButton("⌯ 𝐒ᴜʙsᴄʀɪʙᴇ 𝐓ᴏ 𝐔ᴘᴅᴀᴛᴇs ⌯", url=f"https://t.me/Airtel_updates"),
],
[
InlineKeyboardButton("⌯ 𝐂ɪɴᴇᴋᴏʀɴ 🍿 ⌯", url=f"https://t.me/+diMgtGOhhAdkZDk9"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/9imsfs.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
