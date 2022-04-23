from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("TOKEN")
group_id = env.int("group_id")
