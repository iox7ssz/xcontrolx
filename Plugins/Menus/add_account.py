# requier modules 
from pyrogram import Client as app, filters, types
from pyrogram import Client
# Requier Pyrogram Erro 
from pyrogram.errors import (
    PhoneNumberInvalid, PhoneCodeInvalid, SessionPasswordNeeded, PasswordHashInvalid, PhoneCodeExpired
)
from pyromod import exceptions
import asyncio 

# Requier Bot Plugins 
from Config import databesas, config
from helpers import Message, Keyboard


# ON Add Account 
@app.on_callback_query(filters.regex('^ADD_ACCOUNT'))
async def ADD_SESSIONS(app: app, query: types.CallbackQuery):
    # Get Phone NUmber 
    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=query.message.id , 
        text=Message.HOME_MESSAGE['GET_PHONE'], reply_markup=Keyboard.Keyboard.BACK_HOME()
    )

    # On Listen Phone Number 
    try:
        data = await app.listen(chat_id=query.from_user.id, filters=filters.text & filters.private)
    except exceptions.ListenerTimeout as Err:
        print(Err)
        return 
    
    # Check PHone and start Client 
    PhoneNumber = data.text
    message_data = await app.send_message(
        chat_id=query.message.chat.id, 
        text=Message.HOME_MESSAGE['WITH_LODING']
    )
    
    session_client = Client(
        name=":memory:",
        api_hash=config.API_HASH, api_id=config.API_ID, in_memory=True
    )
    try:
        await session_client.connect()
        phon_code_data = await session_client.send_code(
            phone_number=PhoneNumber
        )

    
    except PhoneNumberInvalid as Err:
        await app.edit_message_text(
            chat_id=query.message.chat.id, message_id=message_data.id, 
            text=Message.HOME_MESSAGE['GET_PHONE_ERROR'], reply_markup=Keyboard.Keyboard.BACK_HOME()
        )
        await session_client.disconnect()
        return    

    await app.edit_message_text(
        chat_id=query.message.chat.id, message_id=message_data.id, 
        text=Message.HOME_MESSAGE['GET_CODE'], reply_markup=Keyboard.Keyboard.BACK_HOME()
    )

    # On Listen Ver Code 
    try:
        data = await app.listen(chat_id=query.from_user.id, filters=filters.text & filters.private)
    except exceptions.ListenerTimeout as Err:
        await session_client.disconnect()
        print(Err)
        return 
    
    message_data = await app.send_message(
        chat_id=query.message.chat.id, 
        text=Message.HOME_MESSAGE['WITH_LODING']
    )

    # Check COde
    try: 
        VerCode = data.text
    except:
        await session_client.disconnect()
        await app.edit_message_text(
            chat_id=query.message.chat.id, message_id=message_data.id, 
            text=Message.HOME_MESSAGE['GET_CODE_ERROR_1'], reply_markup=Keyboard.Keyboard.BACK_HOME()
        )
        return

    # Start Logins Session 
    try:
        await session_client.sign_in(
            phone_code=VerCode, 
            phone_code_hash=phon_code_data.phone_code_hash, 
            phone_number=PhoneNumber
        )

        # Add Session 

        return 
    
    except (PhoneCodeInvalid ,PhoneCodeExpired) as Err:
        await session_client.disconnect()
        await app.edit_message_text(
            chat_id=query.message.chat.id, message_id=message_data.id, 
            text=Message.HOME_MESSAGE['GET_CODE_ERROR_2'], reply_markup=Keyboard.Keyboard.BACK_HOME()
        )
        return
    
    
    except SessionPasswordNeeded as Err:
        await app.edit_message_text(
            chat_id=query.message.chat.id, message_id=message_data.id, 
            text=Message.HOME_MESSAGE['GET_PASSWORD'], reply_markup=Keyboard.Keyboard.BACK_HOME()
        )
        # On Listen Password 
        try:
            data = await app.listen(chat_id=query.from_user.id, filters=filters.text & filters.private)
        except exceptions.ListenerTimeout as Err:
            print(Err)
            return
        
        Password = data.text
        message_data = await app.send_message(
            chat_id=query.message.chat.id, 
            text=Message.HOME_MESSAGE['WITH_LODING']
            )

        # CHcek Password 
        try: 
            await session_client.check_password(Password)
            session_String = await session_client.export_session_string()
            sessio_data = await  session_client.get_me()
            databesas.ADD_NEW_SESSIONS(sessio_data.id, sessio_data.phone_number
                                    , sessio_data.first_name, sessio_data.username, session_String)

            await app.edit_message_text(
                    chat_id=query.message.chat.id, message_id=message_data.id, 
                    text=Message.HOME_MESSAGE['DONE_ADD_SESSION'].format(databesas.GET_SESSIONS_COUNT()), reply_markup=Keyboard.Keyboard.BACK_HOME()
            )
            await session_client.disconnect()


        except PasswordHashInvalid as Err:
            await app.edit_message_text(
                    chat_id=query.message.chat.id, message_id=message_data.id, 
                    text=Message.HOME_MESSAGE['GET_PASSWORD_ERROR'], reply_markup=Keyboard.Keyboard.BACK_HOME()
            )
            await session_client.disconnect()
            return
        
        return
        


    #  ADD Session Data 
    session_String = await session_client.export_session_string()
    sessio_data = await  session_client.get_me()
    databesas.ADD_NEW_SESSIONS(sessio_data.id, sessio_data.phone_number
                               , sessio_data.first_name, sessio_data.username, session_String)
    
    await app.edit_message_text(
            chat_id=query.message.chat.id, message_id=message_data.id, 
            text=Message.HOME_MESSAGE['DONE_ADD_SESSION'].format(databesas.GET_SESSIONS_COUNT()), reply_markup=Keyboard.Keyboard.BACK_HOME()
        )
    
    await session_client.disconnect()




 



    
