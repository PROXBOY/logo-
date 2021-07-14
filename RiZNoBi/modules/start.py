from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAEKu1Jg5f5zeKsZVlXoVBeQLEkyE7lH3QACTwoAAkleMFGSHO2QzdIk8iAE")
    await message.reply_text(
        f"""➢ ʜᴇʟʟʟᴏᴏᴡ 👋 {message.from_user.first_name}! ɪ'ᴍ ᴏᴘ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [ʀɪᴢᴏᴇʟ](https://t.me/TheRiZoeL) ᴀɴᴅ [ᴅᴇsɪ ɴᴏʙɪᴛᴀ](https://t.me/SOULxDED) \n\n➤ ɪ ᴄᴀɴ ᴍᴀᴋᴇ ᴍᴀɴʏ ᴛᴘʏᴇs ᴏғ ʟᴏɢᴏs ғᴏʀ ʏᴏᴜ !!\n\n➤ ᴜsᴇ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ʏᴏᴜʀ ʟᴏɢᴏ !!\n➤ sᴇɴᴅ ᴍᴇ /help ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🥀ℝ𝚒ℤ𝚘𝚎𝕃 🖤", url="https://t.me/TheRiZoeL")
                  ],[
                    InlineKeyboardButton(
                        "🥀ℕ𝚘𝔹𝚒𝕋𝚊 🖤️", url="https://t.me/SOULxDED"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_sticker("CAACAgEAAxkBAAEKu2hg5gABhWi_kFU9qvgHkDJwxHzzTCoAAlIBAAJRKQ05EAu6KiftBFsgBA")
      await message.reply_text("""**➤ 𝚁𝚒𝚉-𝙽𝚘𝙱𝚒 𝙻𝙾𝙶𝙾 𝙱𝙾𝚃 !!!**""",
      reply_markup=InlineKeyboardMarkup(
           [ 
                [
                    InlineKeyboardButton(
                        "🥀ℝ𝚒ℤ𝚘𝚎𝕃 🖤", url="https://t.me/TheRiZoeL")
                  ],[
                    InlineKeyboardButton(
                        "🥀ℕ𝚘𝔹𝚒𝕋𝚊 🖤️", url="https://t.me/SOULxDED"
                    )
                ]
            ]
        )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEKu1xg5f9AP1o_4sEzWGKKeN4nOwwY0wACXwEAAlEpDTmlH2cmxcHPVyAE")
    await message.reply_text(
        f"""<b>☯︎ ʜᴇʀᴇ ɪs ᴀ sɪᴍᴘʟᴇ ᴄᴍᴅ ᴏғ ʀɪᴢ-ɴᴏʙɪ ☯︎ !
◈ ━━━━━━━╗ ⸙ ╔━━━━━━━ ◈
/logo1 <your name>
/logo2 <your name>
/logo3 <your name>
/logo4 <your name>
/logo5 <your name>
/logo6 <your name>
/logo7 <your name>
/logo8 <your name>
/logo9 <your name>
Use cmd /logo1 to /logo100 we will add more logos as soon as possible !! 
◈ ━━━━━━━╝ ⸙ ╚━━━━━━━ ◈
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        "✙ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ✙", url="https://t.me/@RiZNoBi_LoGo_Bot?startgroup=true"
                    )
                ],[
                    InlineKeyboardButton(
                        "𝔻ℕℍ𝚡ℍ𝔼𝕃", url="https://t.me/DNHxHELL"
                    ) 
                ]
            ]
        )
    )

