from vkbottle.bot import Blueprint, Message

from values.strings import *
from values.keyboards import *
from values.secrets import admin_list
from vk_queue import Users
from values.csv_works import *

vk = Blueprint("Only admins chat commands")


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
            users_array = id_users_csv()
            array_q = new_queue.print_queue()
            id = array_q[0].get_id()
            await vk.api.messages.send(peer_ids=users_array, message="Очердь стартовала, первому игроку приготовиться.",
                                       random_id=0)
            await vk.api.messages.send(peer_id=id, message=your_next, random_id=0, keyboard=keyboard_answer)


@vk.on.private_message(text='Убрать первого')
async def exit_q(message: Message):
    if new_queue.is_empty():
        pass
    else:
        user = await vk.api.users.get(message.from_id)
        if user[0].id in admin_list:
            id = new_queue.get_first().get_id()
            await vk.api.messages.send(peer_id=id,
                                       message=f'{new_queue.get_first().get_name()} '
                                               f'{new_queue.get_first().get_lastname()} был убран из очереди.',
                                       random_id=0)
            new_queue.del_person(0)

            if new_queue.is_empty():
                pass
            else:
                id = new_queue.get_first().get_id()
                await vk.api.messages.send(peer_id=id, message=your_next, random_id=0, keyboard=keyboard_answer)


@vk.on.private_message(text='Переместиться на <args>')
async def make_dirty(message: Message, args):
    if new_queue.is_empty():
        await message.answer(queue_not_created)
    else:
        if args is not None:
            user = await vk.api.users.get(message.from_id)
            if user[0].id in admin_list:
                if args[0].isdigit():
                    if int(args[0]) <= len(new_queue.print_queue()):
                        for i in range(len(new_queue.print_queue())):
                            new_queue.dirty_finger(i, int(args[0]) - 1)
                        await message.answer(f'Вы переместились на {int(args[0])} позицию в списке.')
                    else:
                        await message.answer(f'Вы переборщили с числом, всего в списке '
                                             f'{len(new_queue.print_queue())} элемента(-ов).')
                else:
                    await message.answer('Вы ввели не число!')
        else:
            await message.answer("Вы забыли ввести место, на которое хотите встать\nПример: Переместиться на 1")


@vk.on.private_message(text='Переместить <args>')
async def make_dirty(message: Message, args):
    if new_queue.is_empty():
        await message.answer(queue_not_created)
    else:
        if args is not None:
            user = await vk.api.users.get(message.from_id)
            if user[0].id in admin_list:
                if args[0].isdigit() and args[2].isdigit():
                    if int(args[0]) <= len(new_queue.print_queue()) and int(args[2]) <= len(new_queue.print_queue()):
                        new_queue.dirty_finger(int(args[0]) - 1, int(args[2]) - 1)
                        await message.answer(f'Вы переместили {int(args[0])} на {int(args[2])} позицию в списке.')
                    else:
                        await message.answer(f'Вы переборщили с числом, всего в списке '
                                             f'{len(new_queue.print_queue())} элемента(-ов).')
                else:
                    await message.answer('Вы ввели не число!')
