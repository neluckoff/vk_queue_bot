# [В]контакте бот для очередей

Бот предназначен для групп людей (одноклассников, одногруппников и т.д.), которым необходимо пользоваться электронной очередью для сдачи практических работ.

<p align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/neluckoff/vk_queue_bot">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/neluckoff/vk_queue_bot">
  <a href="https://github.com/neluckoff/vk_queue_bot/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/neluckoff/vk_queue_bot?color=yellow"></a>
  <a href="https://github.com/neluckoff/vk_queue_bot/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/neluckoff/vk_queue_bot?color=orange"></a>
  <a href="https://github.com/neluckoff/vk_queue_bot/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/neluckoff/vk_queue_bot"></a>
  <a href="https://github.com/neluckoff/vk_queue_bot/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/neluckoff/vk_queue_bot"></a>
</p>

## УСТАНОВКА
Для написания кода использовалась библиотека [vkbottle](https://github.com/vkbottle/vkbottle).

Для установки этой библиотеки необходимо открыть терминал и прописать ```pip install vkbottle```

## БЫСТРЫЙ СТАРТ
В файлах [dotenv](https://github.com/neluckoff/vk_queue_bot/blob/master/.env) и [settings.py](https://github.com/neluckoff/vk_queue_bot/blob/master/settings.py) хранится основная информация о вашем боте, а именно ``token``, ``group_id`` и ``admin_list``.

В переменную ``token`` необходимо создать и записать токен сообщества, в которой у Вас будет находиться бот. Для этого нужно открыть настройки группы, перейти в вкладку "Работа с API" и создать или скопировать уже имеющийся токен.

В переменной ``group_id`` хранится ID группы, в которой находится бот, взять его можно в основной информации Вашего сообщества.

В массив переменных ``admin_list`` необходимо вписать ID участников сообщества, у которых будет доступ к командам администрирования очереди.

## ЭКСКУРСИЯ
В боте построена небольшая база данных в csv файле - [data.csv](https://github.com/neluckoff/vk_queue_bot/blob/master/data/csv/data.csv).
Она добавляет в себя новых пользователей после прописывания команды "**Меню**" (только в том случае, если пользователь еще не был добавлен)

Почти весь текст (реакции на команды и т.д.) хранится в файле [strings.py](https://github.com/neluckoff/vk_queue_bot/blob/master/data/strings.py)

Все команды разбиты на две категории: [команды администрации](https://github.com/neluckoff/vk_queue_bot/blob/master/commands/admins/admin_commands.py) и [команды пользователей](https://github.com/neluckoff/vk_queue_bot/blob/master/commands/users/user_commands.py), а также хранятся в отдельных файлах.

Для удобства навигации во время пользования ботом - реализованы [клавиатуры](https://github.com/neluckoff/vk_queue_bot/blob/master/data/keyboards.py), чтобы пользователи не прописывали постоянно команды.

<p align="center"><a href="https://vk.com/neluckoff" target="_blank"><img src="https://i.imgur.com/dXkV3uW.gif"></a></p>

## КОМАНДЫ ПОЛЬЗОВАТЕЛЕЙ

+ **Присоединиться** - команда для присоединения пользователя к существующей очереди.
+ **Посмотреть** - команда для просмотра пользователем существующей очереди.
+ **Регистрация** - команда для добавления пользователя в базу данных (обязательна для рассылки о начале очереди).
+ **Меню** - вызов пользователем меню.
+ **Выйти** - команда для выхода пользователя из очереди.
+ **Ответил** - команда для первого человека в очереди (выход из очереди после ответа).

## КОМАНДЫ АДМИНИСТРАЦИИ
+ **Админ-панель** - вызов администратором панели (меню) для дальнейшей работы.
+ **Создать** - команда администратора для создания очереди. Также можно использовать **Создать ``NAME``** для создания очереди с названием.
+ **Очистить** - команда администратора для полной очистки очереди.
+ **Перемешать** - команда администратора для перемешивания очереди (используется до старта).
+ **Старт** - команда администратора для старта очереди.
+ **Удалить первого** - команда администратора для удаления первого человека в списке.
+ **Переместиться на ``num``** - команда администратора для перемешения его на ``num`` место в списке.
+ **Переместить ``num1`` ``num2``** - команда администратора для перемешения пользователя с ``num1`` на ``num2`` место в списке
