from pyrogram.types import InlineKeyboardButton

import config
from Rudra import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="⚙️𝐅ᴇᴀᴛᴜʀᴇs⚙️", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🐰𝐂ʜᴀɴɴᴇʟ🐰", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="✨𝐆ʀᴏᴜᴘ✨", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="🌺𝐎ᴡɴᴇʀ🌺", url=f"https://t.me/pataka_love_jaat"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="⚙️𝐅ᴇᴀᴛᴜʀᴇs⚙️", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🐰𝐂ʜᴀɴɴᴇʟ🐰", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="✨𝐆ʀᴏᴜᴘ✨", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="🌺𝐎ᴡɴᴇʀ🌺", url=f"https://t.me/pataka_love_jaat"),
        ],
    ]
    return buttons