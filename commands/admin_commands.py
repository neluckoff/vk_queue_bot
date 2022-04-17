from vkbottle.bot import Blueprint, Message

from values.strings import *
from values.keyboards import *
from values.secrets import admin_list
from vk_queue import Users
from values.json_works import *

vk = Blueprint("Only admins chat commands")
STARTED = False


@vk.on.private_message(text='Админ-панель')
async def admin_panel(message: Message):
    user = await vk.api.users.get(message.from_id)
    if user[0].id in admin_list:
        await message.answer(welcome_admins, keyboard=keyboard_admin_menu)
    else:
        await message.answer(not_enough)


@vk.on.private_message(text=['Создать', 'Создать <args>'])
async def create_q(message: Message, args=None):
    user = await vk.api.users.get(message.from_id)
    if user[0].id in admin_list:
        if new_queue.is_empty():
            del check[:]
            new_queue.create_queue()
            person = Users(user[0].id, user[0].first_name, user[0].last_name)
            new_queue.add_to_queue(person)
            check.append(user[0].id)
            await message.answer(admin_queue_created)
            users_array = id_users_csv()
            if args is None:
                await vk.api.messages.send(peer_ids=users_array, message="Создана новая очередь!", random_id=0,
                                           keyboard=keyboard_join)
            else:
                await vk.api.messages.send(peer_ids=users_array, message=f'Создана новая очередь для {args}!',
                                           random_id=0,
                                           keyboard=keyboard_join)
        else:
            await message.answer(queue_was_created, keyboard=keyboard_clear_queue)


@vk.on.private_message(text='Очистить')
async def yes_q(message: Message):
    user = await vk.api.users.get(message.from_id)
    if user[0].id in admin_list:
        del check[:]
        new_queue.create_queue()
        await message.answer(queue_was_cleared)


@vk.on.private_message(text='Перемешать')
async def shaffle_q(message: Message):
    if new_queue.is_empty():
        await message.answer(queue_not_created)
    else:
        user = await vk.api.users.get(message.from_id)
        if user[0].id in admin_list:
            new_queue.shaffle_queue()
            await message.answer(queue_shaffled)


@vk.on.private_message(text='Старт')
async def start_q(message: Message):
    if new_queue.is_empty():
        await message.answer(queue_not_created)
    else:
        user = await vk.api.users.get(message.from_id)
        if user[0].id in admin_list:
            array_q = new_queue.print_queue()
            id = array_q[0].get_id()
            await vk.api.messages.send(peer_id=id, message=your_next, random_id=0, keyboard=keyboard_answer)


@vk.on.private_message(text='Сделать грязь')
async def make_dirty(message: Message):
    if new_queue.is_empty():
        await message.answer(queue_not_created)
    else:
        user = await vk.api.users.get(message.from_id)
        if user[0].id in admin_list:
            for i in range(len(new_queue.print_queue())):
                new_queue.dirty_finger(i)
        await message.answer(perem_dirty)
