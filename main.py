from vkbottle.bot import Bot
from vkbottle import load_blueprints_from_package

from values.secrets import token, group_id

bot = Bot(token, group_id)

for bp in load_blueprints_from_package("commands"):
    bp.load(bot)

bot.run_forever()
