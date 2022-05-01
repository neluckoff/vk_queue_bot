import random

from misc.vk_queue import VkQueue

"""
Модуль для хранения всех длинных строк,
используемых в проекте
"""

menu_str = "Меню вызвано вместо клавиатуры."
hello_str = "Привет! 👋🏻\nЭто специалист очередей.\nДля начала работы перейдите в меню."
cool_smiles = ["🥳", "👍🏻", "👊🏻", "🤘🏻", "🤟", "💪🏻", "☝🏻", "💩", "😎", "🥃"]
end_answer = ["Красавчик!", "Так держать!", "Ну ты лютый!", "Жоский тип", "Поздравляю!"]
your_next = "Твоя очередь отвечать, выходи!"
queue_not_created = "Очередь еще не создана!"
welcome_admins = "Добро пожаловать зону администрации\nНе забывай про \"Помощь\" 😎" \
                 "\n❗ Для создания используй \"Создать <name>\""
not_enough = "⛔ Не шали, у тебя недостаточно прав!"
admin_queue_created = "🎉 Вы создали и подключились к очереди."
queue_was_created = "♻ Очередь уже существует, обнулить?"
queue_was_cleared = "Очередь успешно очищена, можете создавать новую!"
queue_shaffled = 'Вы успешно перемешали очередь.'
perem_dirty = "Я об этом никому не расскажу!"
queue_was_empty = "Очередь пока пуста."
queue_joined = "✅ Вы успешно присоединились к очереди."
admin_help_str = "Небольшая сводка команд:\n" \
                 "\n\t1. Переместиться на <int> - переместиться на <int> место" \
                 "\n\t2. Поменять <int1> <int2> - поменять местами <int1> <int2> пользователей" \
                 "\n\t3. Удалить <int> - удалить <int> номер из очереди" \
                 "\n\t4. Убрать первого - убирает первого человека из очереди"


def random_cool_smile():
    random_index = random.randint(0, len(cool_smiles) - 1)
    return cool_smiles[random_index]


def random_end_answer():
    random_index = random.randint(0, len(end_answer) - 1)
    return end_answer[random_index]


check = []
new_queue = VkQueue()
