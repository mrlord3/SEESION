import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 11560169))

    API_HASH = os.environ.get("API_HASH", "0687c1437fdafaa9e8be8ee6b798bdc6")
