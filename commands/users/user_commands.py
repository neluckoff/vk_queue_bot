import csv
from vkbottle.bot import Blueprint, Message
from data.strings import *
from data.keyboards import *
from misc.vk_queue import Users
from data.csv.csv_works import id_in_csv
from settings import path

vk = Blueprint("Only users chat command")

"""
Модуль со всеми командами пользователей
"""


@vk.on.private_message(text=['Начать', 'Ку', 'Привет'])
async def hello(message: Message):
    """Стартовая команда"""
    await message.answer(hello_str, keyboard=keyboard_hello)


@vk.on.private_message(text='Меню')
async def menu(message: Message):
    """Вызов меню со встроенной регистрацией"""
    user = await vk.api.users.get(message.from_id)
    if id_in_csv(user[0].id):
        await message.answer(menu_str, keyboard=keyboard_menu)
    else:
        with open(path, 'a') as outfile:
            csv_writer = csv.writer(outfile, delimiter=',')
            csv_writer.writerow([user[0].id, user[0].first_name, user[0].last_name])
        print(f'Зарегистрирован новый пользователь - {user[0].first_name} {user[0].last_name} - {user[0].id}')
        await message.answer(menu_str, keyboard=keyboard_menu)


@vk.on.private_message(text='Посмотреть')
async def check_q(message: Message):
    """Посмотреть существующую очередь"""
    if new_queue.is_empty():
        await message.answer(queue_was_empty)
    else:
        array_q = new_queue.print_queue()
        new_str = ''
        count = 1
        for i in array_q:
            new_str += f'{count}. {i}\n'
            count += 1
        await message.answer(new_str)


@vk.on.private_message(text='Присоединиться')
async def shaffle_q(message: Message):
    """Присоединиться к существующей очереди"""
    if new_queue.is_empty():
        await message.answer(queue_not_created)
    else:
        user = await vk.api.users.get(message.from_id)
        person = Users(user[0].id, user[0].first_name, user[0].last_name)
        if user[0].id in check:
            await message.answer("📌 Вы уже в очереди")
        else:
            new_queue.add_to_queue(person)
            check.append(user[0].id)
            await message.answer(queue_joined)


@vk.on.private_message(text='Ответил')
async def answer_q(message: Message):
    """Команда для первого в списке после старта,
    чтобы выйти из очереди"""
    user = await vk.api.users.get(message.from_id)
    if new_queue.is_empty():
        pass
    else:
        if new_queue.get_first().get_id() == user[0].id:
            id = new_queue.get_first().get_id()
            await vk.api.messages.send(peer_id=id, message=f'{random_end_answer()} {random_cool_smile()}', random_id=0)
            new_queue.del_person(0)

            if new_queue.is_empty():
                pass
            else:
                id = new_queue.get_first().get_id()
                await vk.api.messages.send(peer_id=id, message=your_next, random_id=0, keyboard=keyboard_answer)
        else:
            await message.answer("Сейчас не твоя очередь!")


@vk.on.private_message(text='Выйти')
async def exit_q(message: Message):
    """Команда для выхода из очереди"""
    if new_queue.is_empty():
        await message.answer(queue_not_created)
    else:
        user = await vk.api.users.get(message.from_id)
        if user[0].id in new_queue.search_by_id():
            a = new_queue.search_by_id()
            new_queue.del_person(a.index(user[0].id))
            await message.answer("🚪 Вы вышли из очереди.")
        else:
            await message.answer("📌 Вас нет в очереди.")
