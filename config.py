class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1983756930:AAEfOQSDXx-juZIYIi-q0Yss-uRlQrVoz2A"
    OWNER_ID = "492119454" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "aiemser"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://aiemser:Cucciolo2002@database-1.c5tahux98jdj.us-east-2.rds.amazonaws.com:5431/TutorBotDataBase'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
