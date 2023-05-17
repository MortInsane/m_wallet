from environs import Env


env = Env()
env.read_env()


DJANGO_SECRET = env.str("DJANGO_SECRET")
