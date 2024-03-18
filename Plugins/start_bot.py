# Requier Modules
from pyrogram import Client as app , filters, types 

# Requier BOt PLugins 
from Config import config, databesas
from helpers import Message, Keyboard

# Create Filter

@app.on_message(filters.private & filters.regex('^/start$') &  filters.user(config.SUDO))
async def ON_START_BOT(app: app, message: types.Message):
    # start bot 
    await app.send_message(
        chat_id=message.chat.id, 
        text=Message.HOME_MESSAGE['HOME_MESSAGE'], 
        reply_markup=Keyboard.Keyboard.HOME_KEYBOARD(databesas.GET_SESSIONS_COUNT())
    )


# BAck HOme 
@app.on_callback_query(filters.regex('^BACK_HOME$'))
async def ON_BACK_HOME(app: app, query: types.CallbackQuery):
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id, 
        text=Message.HOME_MESSAGE['HOME_MESSAGE'], 
        reply_markup=Keyboard.Keyboard.HOME_KEYBOARD(databesas.GET_SESSIONS_COUNT())
    )