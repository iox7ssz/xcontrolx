# Requier Modules 
from pyrogram import Client, filters, types

# Requier Plugins 
from Config import config


# Join Chat Apis 
async def JOIN_CHAT(session: str, username: str):
    try:
        async with Client(':memory:', api_hash=config.API_HASH, api_id=config.API_ID, session_string=session) as app:
            try:
                response = await app.join_chat(
                    chat_id=username
                )
            except Exception as Errs:
                print(Errs)
                return False
            print(response)
            return True
    except Exception as Errs:
        print(Errs)
        return False
    

# LEave Chat Apis 
async def LEAVE_CHAT(session: str, username: str):
    try:
        async with Client(':memory:', api_hash=config.API_HASH, api_id=config.API_ID, session_string=session) as app:
            try:
                response = await app.leave_chat(
                    chat_id=username
                )
            except Exception as Errs:
                print(Errs)
                return False
            print(response)
            return True
    except Exception as Errs:
        print(Errs)
        return False