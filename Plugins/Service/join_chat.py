# requier modules 
from pyrogram import Client as app, filters, types
from pyrogram import Client


# Requier BOt PLugins 
from Config import config, databesas
from helpers import Message, Keyboard
from Plugins.apis import chat_apis


@app.on_callback_query(filters.regex('^SERVICE_JOIN_CHAT$'))
async def SERVICE_JOIN_CHAT(app: app, query: types.CallbackQuery):
    _type = "دخول قناة"
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id, 
        text=Message.HOME_MESSAGE['GET_CHAT_USERNAME'], reply_markup=Keyboard.Keyboard.BACK_HOME()
    )

    data = await app.listen(chat_id=query.from_user.id, filters=filters.text & filters.private)
    ChatUsername = data.text

    if '@' in ChatUsername:
        ChatUsername = str(ChatUsername).strip('@')
    # Start JOisn chat 
    try:
        chat = await app.get_chat(ChatUsername)
    except:
        await app.send_message(
            chat_id=query.message.chat.id, text=Message.HOME_MESSAGE['GET_CHAT_USERNAME_ERR'], 
            reply_markup=Keyboard.Keyboard.BACK_HOME()
        )
        return
    
    message_data = await app.send_message(
        chat_id=query.message.chat.id ,text=Message.HOME_MESSAGE['WITH_LODING']
    )

    sessions = databesas.GET_ALL_SESSIONS()
    SessionCount = databesas.GET_SESSIONS_COUNT()
    DONE, ERRO = 0,0,

    # Start Order
    await app.edit_message_text(
        chat_id=query.message.chat.id ,message_id=message_data.id,
        text=Message.HOME_MESSAGE['ORDER_MESSAGE'].format(
            SessionCount, _type, DONE, ERRO, 'جاري التحميل '
        ),
    )

    for session in sessions:
        try:
            response = await chat_apis.JOIN_CHAT(sessions[session]['session_string'], ChatUsername)
            if response == True:
                DONE+=1
            else:
                ERRO+=1
        except Exception as Err:
            ERRO+=1
            print(Err)

        # Start Order
        await app.edit_message_text(
            chat_id=query.message.chat.id ,message_id=message_data.id,
            text=Message.HOME_MESSAGE['ORDER_MESSAGE'].format(
            SessionCount, _type, DONE, ERRO, 'جاري التنفيذ'

            ),
        )
            # Start Order
    await app.edit_message_text(
            chat_id=query.message.chat.id ,message_id=message_data.id,
            text=Message.HOME_MESSAGE['ORDER_MESSAGE'].format(
            SessionCount, _type, DONE, ERRO ,"اكتمل الطلب"

            ),
        )