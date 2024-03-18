# Bot InlineKeyboard 
from pyrogram import types 


class Keyboard:

    def HOME_KEYBOARD(sessionCount: int):
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text="↫⚡️︙ ❲ الخدمات ❳", callback_data="SEERVICE_MENU"),
            ],
            [
                types.InlineKeyboardButton(text="↫💠︙ ❲ اضافة حساب ❳", callback_data="ADD_ACCOUNT"),
                types.InlineKeyboardButton(text="↫⚙️︙ ❲ فحص ❳", callback_data="ACCOUNTS_SETTINGS"),
            ],
            [
                types.InlineKeyboardButton(text=f"↫عدد الحسابات︙ ❲ {sessionCount} ❳", callback_data="NOT"),

            ]
        ])
    
    def BACK_HOME():
        return types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton(text="↫🔙︙ ❲ رجوع ❳", callback_data="BACK_HOME")]
        ])
    

    def SERVICE_MENU():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text="↫⚡️︙ ❲ دخول قناة ❳", callback_data="SERVICE_JOIN_CHAT"),
                types.InlineKeyboardButton(text="↫💠︙ ❲ خروج من قناة ❳", callback_data="SERVICE_LAVE_CAHT"),
            ],[
                types.InlineKeyboardButton(text="↫💬︙ ❲ ارسال رسالا ❳", callback_data="SERVCIE_SEND_MESSAGE"),
                types.InlineKeyboardButton(text="↫︙ ❲  ❳", callback_data="NOT"),
            ],[
                types.InlineKeyboardButton(text="↫🔙︙ ❲ رجوع ❳", callback_data="BACK_HOME")
            ]
        ])
    
    def CHECK_KEYBOARD():
        return types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton(text="↫♻️︙ ❲ تنضيف ❳", callback_data="FILTERS_ACCOUNTS"),
                types.InlineKeyboardButton(text="↫🔙︙ ❲ رجوع ❳", callback_data="BACK_HOME")

            ]
        ])