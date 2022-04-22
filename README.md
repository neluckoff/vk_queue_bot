# [В]контакте бот для очередей

Бот предназначен для групп людей (одноклассников, одногруппников и т.д.), которым необходимо пользоваться электронной очередью для сдачи практических работ.

[![GitHub issues](https://img.shields.io/github/issues/neluckoff/vk_queue_bot)](https://github.com/neluckoff/vk_queue_bot/issues) 
[![GitHub forks](https://img.shields.io/github/forks/neluckoff/vk_queue_bot)](https://github.com/neluckoff/vk_queue_bot/network) 
[![GitHub stars](https://img.shields.io/github/stars/neluckoff/vk_queue_bot)](https://github.com/neluckoff/vk_queue_bot/stargazers) 
[![GitHub license](https://img.shields.io/github/license/neluckoff/vk_queue_bot)](https://github.com/neluckoff/vk_queue_bot) 


___

Для написания кода использовалась библиотека [vkbottle](https://github.com/vkbottle/vkbottle).
Бот полностью готов к вашей эксплуатации, вам остается только заполнить переменные в [secrets.py](https://github.com/neluckoff/vk_queue_bot/blob/master/values/secrets.py).

В боте построена небольшая база данных в csv файле - [data.csv](https://github.com/neluckoff/vk_queue_bot/blob/master/data.csv).
Она добавляет в себя новых пользователей после прописывания команды **Регистрация** пользователем.

Токен группы, ID группы и ID администрации хранятся в файле [secrets.py](https://github.com/neluckoff/vk_queue_bot/blob/master/values/secrets.py).

Почти весь текст (реакции на команды и т.д.) хранится в файле [strings.py](https://github.com/neluckoff/vk_queue_bot/blob/master/values/strings.py)

Все команды разбиты на две категории: [команды администрации](https://github.com/neluckoff/vk_queue_bot/blob/master/commands/admin_commands.py) и [команды пользователей](https://github.com/neluckoff/vk_queue_bot/blob/master/commands/user_commands.py).

Для удобства навигации во время пользования ботом - реализованы [клавиатуры](https://github.com/neluckoff/vk_queue_bot/blob/master/values/keyboards.py), чтобы пользователи не прописывали постоянно команды.

## Команды пользователей

#### Присоединиться
- Команда для присоединения пользователя к существующей очереди.

#### Посмотреть
- Команда для просмотра пользователем существующей очереди.

#### Регистрация
- Команда для добавления пользователя в базу данных (обязательна для рассылки о начале очереди).

#### Меню
- Вызов пользователем меню.

#### Выйти
- Команда для выхода пользователя из очереди.

#### Ответил
- Команда для первого человека в очереди (выход из очереди после ответа).

## Команды администрации
#### Админ-панель
- Вызов администратором панели (меню) для дальнейшей работы.

#### Создать
- Команда администратора для создания очереди.
- Также можно использовать **Создать NAME** для создания очереди с названием.

#### Очистить
- Команда администратора для полной очистки очереди.

#### Перемешать
- Команда администратора для перемешивания очереди.

#### Старт
- Команда администратора для старта очереди.

#### Удалить первого
- Команда администратора для удаления первого человека в списке.

#### Переместиться на num
- Команда администратора для перемешения его на <num> место в списке.
  
#### Переместить num1 num2
- Команда администратора для перемешения пользователя с num1 на num2 место в списке
