# 

# requier modules 
from pyrogram import Client as app, filters, types
from pyrogram import Client
import asyncio

# Requier BOt PLugins 
from Config import config, databesas, temp
from helpers import Message, Keyboard



@app.on_callback_query(filters.regex('^ACCOUNTS_SETTINGS$'))
async def ACCOUNTS_SETTINGS(app: app, query: types.CallbackQuery):
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id, 
        text=Message.HOME_MESSAGE['WITH_LODING']
    )

    sessions = databesas.GET_ALL_SESSIONS()
    Done, Err, count = 0,0,0

    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id, 
        text=Message.HOME_MESSAGE['ACCOUNT_CHECKING'].format(
            len(sessions), 
            count, 
            Done, 
            Err, 
            'جراي التحميل'
        )
    )
    await asyncio.sleep(1.5)
    PopList = []
    for i in sessions:
        try:
            async with Client(":memory:", api_hash=config.API_HASH, api_id=config.API_ID, session_string=sessions[i]['session_string']) as ses:
                Done+=1

        except:
            PopList.append(i)
            Err+=1
        
        await app.edit_message_text(
            chat_id=query.message.chat.id, message_id=query.message.id, 
            text=Message.HOME_MESSAGE['ACCOUNT_CHECKING'].format(
                len(sessions), 
                count, 
                Done, 
                Err, 
                'جاري التنفيذ'
            ))

    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id, 
        text=Message.HOME_MESSAGE['DONE_CHECK'].format(
            Done, 
            Err, 
        ), reply_markup=Keyboard.Keyboard.CHECK_KEYBOARD())
    
    temp['poplist'] = PopList
    


@app.on_callback_query(filters.regex('^FILTERS_ACCOUNTS$'))
async def FILTERS_ACCOUNT(app: app, query: types.CallbackQuery):
    poplist = temp['poplist']
    sessions = databesas.GET_ALL_SESSIONS()

    await app.edit_message_text(
        chat_id=query.message.chat.id ,message_id=query.message.id ,
        text=Message.HOME_MESSAGE['WITH_CLEAR'],
    )

    await asyncio.sleep(1.5)

    for i in poplist:
        databesas.DELETE_SESSION(i)
    
    
    await app.edit_message_text(
        chat_id=query.message.chat.id ,message_id=query.message.id ,
        text=Message.HOME_MESSAGE['DONE_CLEAR_ACCOUNT'].format(len(poplist)),
    )



