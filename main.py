from vkbottle.bot import Bot, Message
from vkbottle import BaseStateGroup

from values.secrets import token, group_id, admin_list
from values.strings import *
from values.keyboards import *
from vk_queue import VkQueue, Users
from json_works import *

vk = Bot(token, group_id)
data = {'people': []}
check = []
was_started = False
new_queue = VkQueue()


@vk.on.private_message(text=['Начать', 'Ку', 'Привет'])
async def hello(message: Message):
    await message.answer(hello_str, keyboard=keyboard_reg)


@vk.on.private_message(text='Меню')
async def menu(message: Message):
    await message.answer(menu_str, keyboard=keyboard_menu)


@vk.on.private_message(text='Регистрация')
async def menu(message: Message):
    user = await vk.api.users.get(message.from_id)
    data['people'].append({
        'id': user[0].id,
        'first_name': user[0].first_name,
        'last_name': user[0].last_name
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
    await message.answer("Регистрация завершена.", keyboard=keyboard_hello)


@vk.on.private_message(text='Админ-панель')
async def admin_panel(message: Message):
    user = await vk.api.users.get(message.from_id)
    if user[0].id in admin_list:
        await message.answer("Добро пожаловать в чил зону администрации\nМеню ниже", keyboard=keyboard_admin_menu)
    else:
        await message.answer("Не шали, у тебя недостаточно прав!")


@vk.on.private_message(text='Создать')
async def create_q(message: Message):
    user = await vk.api.users.get(message.from_id)
    if user[0].id in admin_list:
        if new_queue.is_empty():
            del check[:]
            new_queue.create_queue()
            person = Users(user[0].id, user[0].first_name, user[0].last_name)
            new_queue.add_to_queue(person)
            check.append(user[0].id)
            was_started = True
            await message.answer("Вы создали и подключились к очереди.")
            users_array = id_users_json()
            await vk.api.messages.send(peer_ids=users_array, message="Создана новая очередь!", random_id=0,
                                       keyboard=keyboard_join)
        else:
            await message.answer("Очередь уже существует, обнулить?", keyboard=keyboard_yes_or_no)

            @vk.on.private_message(text='Да')
            async def yes_q(message: Message):
                user = await vk.api.users.get(message.from_id)
                if user[0].id in admin_list:
                    if was_started:
                        del check[:]
                        new_queue.create_queue()
                        person = Users(user[0].id, user[0].first_name, user[0].last_name)
                        new_queue.add_to_queue(person)
                        check.append(user[0].id)
                        await message.answer("Вы создали и подключились к очереди.")
                        users_array = id_users_json()
                        await vk.api.messages.send(peer_ids=users_array, message="Создана новая очередь!", random_id=0,
                                                   keyboard=keyboard_join)

            @vk.on.private_message(text='Нет')
            async def no_q(message: Message):
                user = await vk.api.users.get(message.from_id)
                if user[0].id in admin_list:
                    if was_started:
                        await message.answer("Вы отменили создание очереди.")


@vk.on.private_message(text='Перемешать')
async def shaffle_q(message: Message):
    user = await vk.api.users.get(message.from_id)
    if user[0].id in admin_list:
        if started:
            await message.answer('Очердь уже была начата, перемешать невозможно.')
        else:
            new_queue.shaffle_queue()
            await message.answer('Вы успешно перемешали очередь.')


@vk.on.private_message(text='Посмотреть')
async def check_q(message: Message):
    if new_queue.is_empty():
        await message.answer("Очередь пока пуста.")
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
    if new_queue.is_empty():
        await message.answer("Очередь еще не создана!")
    else:
        user = await vk.api.users.get(message.from_id)
        person = Users(user[0].id, user[0].first_name, user[0].last_name)
        if user[0].id in check:
            await message.answer("Вы уже в очереди")
        else:
            new_queue.add_to_queue(person)
            check.append(user[0].id)
            await message.answer("Вы успешно присоединились к очереди.")


@vk.on.private_message(text='Старт')
async def start_q(message: Message):
    user = await vk.api.users.get(message.from_id)
    if user[0].id in admin_list:
        array_q = new_queue.print_queue()
        id = array_q[0].get_id()
        await vk.api.messages.send(peer_id=id, message="Твоя очередь отвечать, выходи!", random_id=0,
                                   keyboard=keyboard_answer)
    
    
@vk.on.private_message(text='Ответил')
async def answer_q(message: Message):
    if new_queue.is_empty():
        pass
    else:
        id = new_queue.get_first().get_id()
        await vk.api.messages.send(peer_id=id, message="Красавчик!", random_id=0)

        new_queue.del_person(0)

        if new_queue.is_empty():
            pass
        else:
            id = new_queue.get_first().get_id()
            print(id)
            await vk.api.messages.send(peer_id=id, message="Твоя очередь отвечать, выходи!", random_id=0,
                                       keyboard=keyboard_answer)


@vk.on.private_message(text='Выйти')
async def exit_q(message: Message):
    user = await vk.api.users.get(message.from_id)
    new_us = Users(user[0].id, user[0].first_name, user[0].last_name)
    new_queue.del_by_name(new_us)
    await message.answer("Вы вышли из очереди.")

vk.run_forever()
