from pyrogram.types import InlineKeyboardButton

import config
from Rudra import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [   

InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
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
        [InlineKeyboardButton(text="🐾𝐅ᴇᴀᴛᴜʀᴇs🐾", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🌺𝐎ᴡɴᴇʀ🌺", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="✨𝐆ʀᴏᴜᴘ✨", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="🐰𝐂ʜᴀɴɴᴇʟ🐰", url=config.SUPPORT_CHANNEL),
    ]
    return buttons
