from environs import Env


env = Env()
env.read_env()


DJANGO_SECRET = env.str('DJANGO_SECRET')

POSTGRES_DB = env.str('POSTGRES_DB')
POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
POSTGRES_PORT = env.str('POSTGRES_PORT')
