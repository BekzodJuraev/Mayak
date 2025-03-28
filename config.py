import environ


env = environ.Env()
environ.Env.read_env()
CHANEL_SUPPORT=env('CHANEL_SUPPORT')
BOT_TOKEN=env('BOT_TOKEN')
API_KEY_GOOGLE=env('API_KEY_GOOGLE')
ESKIZ=env('ESKIZ')
DEBUG = env.bool('DEBUG', default=False)