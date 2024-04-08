from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", ""))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "v3nom_world")
UPDATE_CHNL = getenv("UPDATE_CHNL", "TheCchub")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")

# Random Start Images
IMG = [
    "https://graph.org/file/89993d13fd08c45131b2c.jpg",
    "https://graph.org/file/c07189dbf789cc778d03d.jpg",
    "https://graph.org/file/dd2305e8723cb39aee188.jpg",
    "https://graph.org/file/1ada2fdaef82119ea7464.jpg",
    "https://graph.org/file/cfa252c8619886dd9ce28.jpg",
    "https://graph.org/file/ccad9e1d75abedc818611.jpg",
    "https://telegra.ph/file/ffa18225730df716d3532.jpg",
    "https://graph.org/file/5d80085fed89069e0845a.jpg",
    "https://graph.org/file/45242d5fedd04113862f0.jpg",
    "https://graph.org/file/2355db1765e7e73606576.jpg",
    "https://graph.org/file/be989101aff324d2b3074.jpg",
    "https://graph.org/file/01d9d09101fa29950f0a1.jpg",
    "https://graph.org/file/53b138d0babeb06711bbd.jpg",
    "https://graph.org/file/68a2874f92008a3bde3b8.jpg",
    "https://graph.org/file/9aeae4412eaeef506f19d.jpg",
    "https://graph.org/file/9e9866ba58e31b0343166.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAxkBAAIYa2YUNvSlehROrD3cQX2562iuK2H0AAKtCAACgappVgaPLR4YFSkrNAQ",
    "CAACAgUAAxkBAAIYaWYUNuS2fTgjRQtEyfw7hkg0IQUGAAKDEQACBWqhV2s_GglydZlDNAQ",
    "CAACAgUAAxkBAAIYZ2YUNuIzHXMvcYxa6XuhryHfxEqiAAK1CwAC3SjQVjRrfJMrMGtxNAQ",
]


EMOJIOS = [
    "🤡",
    "🔥",
    "😶‍🌫",
    "⛈",
    "🚩",
    "🏴‍☠️",
    "☀️",
    "🖤",
    "⚠️",
    "🎀",
]
