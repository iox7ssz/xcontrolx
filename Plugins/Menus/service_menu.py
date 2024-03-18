# requier modules 
from pyrogram import Client as app, filters, types
from pyrogram import Client


# Requier BOt PLugins 
from Config import config, databesas
from helpers import Message, Keyboard


# on Service Menu 
@app.on_callback_query(filters.regex('^SEERVICE_MENU$'))
async def SERVICE_MENU(app: app, query: types.CallbackQuery):
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id ,
        text=Message.HOME_MESSAGE['SERVICE_MENU_MESSAGE'], reply_markup=Keyboard.Keyboard.SERVICE_MENU()
    )


