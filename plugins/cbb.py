#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>💝 God  : @Sk8903</a>\n📝 Language : <code>Python3</code>\n📰 Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n📢 Channel : @Spkarnan\n📞 Support Group : @sk_tv_group\n🌐 Website : https://www.sktamilserialbots.com/</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🚫 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
