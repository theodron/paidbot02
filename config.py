#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8009397068:AAEP42Awa4HMt0QdqfWGIE1i-m4as5DQLrg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21505404"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5feffdf4111ed339381056d9476d3fcd")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002500369803"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6061153252"))

#Port
PORT = os.environ.get("PORT", "7070")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://paidtron:paidtron@fl4me.ucvbg.mongodb.net/?retryWrites=true&w=majority&appName=Fl4me")
DB_NAME = os.environ.get("DATABASE_NAME", "Tharakbot1")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1001559864888"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002523174321"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002659175005")) #don't remove 0 from here 😐
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1001952902939")) #don't remove 0 from here 😐


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pic
START_PIC = os.environ.get("START_PIC", "https://envs.sh/s/zpxvZVz6OCXE1kswtoM8tw/E3b.jpg")

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\n<b>I am file share bot by @Theodron. Send me any file and I'll give you a link and with that link anyone can access your file 🗃️</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6122920987 7552265941").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel And Group to use me\n\nKindly Please join both channel and group 👇🏻</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = ""

ADMINS.append(OWNER_ID)
ADMINS.append(6122920987)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
