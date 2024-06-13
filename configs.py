# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "12618934"))
	API_HASH = os.environ.get("API_HASH", "49aacd0bc2f8924add29fb02e20c8a16")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "@ARAKAL_THERAVAD_MOVIES_V7_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001974433785"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1297128957"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Autofilterv7:Autofilterv7@cluster0.t5tqe4s.mongodb.net/")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002022755818")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002010307613")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
	ABOUT_BOT_TEXT = f"""
🤖 **𝑴𝒚 𝑵𝒂𝒎𝒆 :** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆:** [𝑷𝒚𝒕𝒉𝒐𝒏](https://www.python.org)

📚 **𝑭𝒓𝒂𝒎𝒆𝒘𝒐𝒓𝒌** [𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎](https://docs.pyrogram.org)

📡 **𝑯𝒐𝒔𝒕𝒆𝒅 𝑶𝒏:** 𝑯𝑬𝑹𝑲𝑼𝑶

🧑🏻‍💻 **𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓:** [𝑵𝒂𝒛𝒓𝒊𝒚𝒂](https://t.me/ARAKAL_THERAVAD_MOVIES_02_bot)

👥 **𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑:** [𝑨𝑻𝑴](https://t.me/DevsZone)

📢 **𝑼𝒑𝒅𝒂𝒕𝒆 𝑪𝒉𝒂𝒏𝒏𝒆𝒍:** [𝑨𝑻𝑴 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍](https://t.me/Discovery_Updates)
"""
	
	HOME_TEXT = """**
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Bro Or Sis, ഈ ഒരു ബോട്ട് @ARAKAL_THERAVAD_GROUP_LINKS ൻ്റെ Files Store Bᴏᴛ ᴠ7 ആണ്, ബോട്ട് Owner ഡെ പർമ്മിഷൻ ഇല്ലാതെ മറ്റു ഒന്നിനും ഈ ബോട്ടിനെ യൂസ് ചെയ്യാൻ കഴിയില്ല..!!  🤗⚠

️📌 𝗔𝗻𝘆 𝗛𝗲𝗹𝗽 𝗣𝗹𝗲𝗮𝘀𝗲 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗔𝗱𝗺𝗶𝗻 : @ARAKAL_THERAVAD_MOVIES_02_bot
**"""
