from pyrogram.types import InlineKeyboardButton

import config
from AloneX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="•𝐒ᴜʙsᴄʀɪʙᴇ 𝐓ᴏ 𝐀ɪʀᴛᴇʟ•",url=f"https://t.me/shubhos_timeline"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="⌯ 𝐒ᴜʙsᴄʀɪʙᴇ 𝐓ᴏ 𝐀ɪʀᴛᴇʟ ⌯",url=f"https://t.me/Airtel_updates"),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
    ]
    return buttons
