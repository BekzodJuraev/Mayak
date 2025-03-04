import environ


env = environ.Env()
environ.Env.read_env()
CHANEL_SUPPORT=env('CHANEL_SUPPORT')
BOT_TOKEN=env('BOT_TOKEN')
DEBUG = env.bool('DEBUG', default=False)