from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Callback

keyboard_menu = (
        Keyboard(one_time=False, inline=False)
            .add(Text('Присоединиться'), color=KeyboardButtonColor.POSITIVE)
            .add(Text('Посмотреть'), color=KeyboardButtonColor.PRIMARY)
            .add(Text('Админ-панель'), color=KeyboardButtonColor.NEGATIVE)
    ).get_json()

keyboard_hello = (
    Keyboard(inline=True)
        .add(Text('Меню'), color=KeyboardButtonColor.PRIMARY)
).get_json()

keyboard_admin_menu = (
    Keyboard(one_time=False, inline=False)
    .add(Text('Создать'), color=KeyboardButtonColor.POSITIVE)
    .add(Text('Перемешать'), color=KeyboardButtonColor.PRIMARY)
    .add(Text('Старт'), color=KeyboardButtonColor.PRIMARY)
    .row()
    .add(Text('Меню'), color=KeyboardButtonColor.PRIMARY)
    .add(Text('Сделать грязь'), color=KeyboardButtonColor.NEGATIVE)
).get_json()

keyboard_join = (
    Keyboard(inline=True)
        .add(Text('Присоединиться'), color=KeyboardButtonColor.PRIMARY)
).get_json()

keyboard_answer = (
    Keyboard(inline=True)
        .add(Text('Ответил'), color=KeyboardButtonColor.POSITIVE)
).get_json()

keyboard_yes_or_no = (
    Keyboard(inline=True)
    .add(Text('Да'), color=KeyboardButtonColor.POSITIVE)
    .add(Text('Нет'), color=KeyboardButtonColor.NEGATIVE)
).get_json()

keyboard_reg = (
    Keyboard(inline=True)
    .add(Text('Регистрация'), color=KeyboardButtonColor.POSITIVE)
).get_json()

