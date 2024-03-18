# Bot config file and Setting
# Requier Modules 
# Requier Pyrogram telegram bot Modules 
from pyrogram import Client, enums
# Requier os Modules 
import os 
# Requier Bot Databesas 
from Utils.databesas import Databesas

class config:
    API_KEY : str = "<API_KEY>" # Bot Api KEy
    API_HASH: str = "db16cbf9526f37v515451553346a13fd" # api hash
    API_ID  : int = 12345678 # ap id 
    SUDO    : int = 1847435573 # sudo id

# Check Extist 
if not os.path.exists('./.session'): # Check session folder 
    os.mkdir('./.session')  # Create session folder
if not os.path.exists('./data'): # Check data Folder
    os.mkdir('/data') # Create data folder

# Databesas class 
databesas = Databesas()

# Temp Data
temp = {}

# Stary Pyrogram CLient
app = Client(
    name='./.session/rad', 
    api_hash=config.API_HASH, 
    api_id=config.API_ID ,
    bot_token=config.API_KEY, 
    plugins=dict(root="Plugins"),
    parse_mode=enums.ParseMode.DEFAULT
)

