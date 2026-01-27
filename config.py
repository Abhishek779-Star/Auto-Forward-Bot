import os

API_ID = int(os.environ.get("API_ID", "16402669"))
API_HASH = os.environ.get("API_HASH", "e50b6c6e9dc8077ec3e9db0e565631e4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Abhishek:abhishek@abhishek.3er4sy0.mongodb.net/?appName=abhishek")
DB_NAME = os.environ.get("DB_NAME", "SilentXBotz")

WEB_SERVER = os.environ.get("WEB_SERVER", "True").lower() in ("true", "1", "t")
PORT = int(os.environ.get("PORT", "8080"))
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

TG_WORKERS = int(os.environ.get("TG_WORKERS", "4"))

# Your Koyeb/Heroku App Url
# Example : https://yorappurl.koyeb.app/
APP_URL = os.environ.get("APP_URL", None)
