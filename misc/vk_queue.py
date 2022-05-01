import random

"""Модуль для реализации очереди"""


class VkQueue:
    """Класс для хранения и управления очередью"""

    def __init__(self):
        self.queue = []

    def create_queue(self):
        """Создание и очищение очереди"""
        self.queue = []

    def add_to_queue(self, user_q):
        """Добавление пользователя в очередь"""
        self.queue.append(user_q)

    def shaffle_queue(self):
        """Перемешивание очереди"""
        random.shuffle(self.queue)

    def is_empty(self):
        """Проверка очереди на пустоту"""
        if len(self.queue) == 0:
            return True
        else:
            return False

    def print_queue(self):
        """Получить текущую очередь"""
        return self.queue

    def del_person(self, user):
        """Удалить пользователя из очереди"""
        self.queue.pop(user)
        a = []
        for i in self.queue:
            a.append(i)
        self.queue = a

    def get_first(self):
        """Получить первого пользователя в очереди"""
        return self.queue[0]

    def get_second(self):
        """Получить второго пользователя в очереди"""
        return self.queue[1]

    def get_by_id(self, index):
        """Получить пользователя по месту в очереди"""
        return self.queue[index]

    def search_by_id(self):
        """Получить массив с ID пользователей в очереди"""
        a = []
        for i in range(len(self.queue)):
            a.append(self.queue[i].get_id())
        return a

    def remove_person_place(self, index, z_index):
        """Поменять местами пользователей в очереди"""
        c = self.queue[index]
        self.queue[index] = self.queue[z_index]
        self.queue[z_index] = c

    def give_first_position(self, index, pos, user):
        """Передвинуть пользователя на <pos> позицию"""
        self.queue.pop(index)
        a = []
        for i in self.queue:
            a.append(i)
        self.queue = a

        self.queue.insert(pos, user)


class Users:
    """Класс с информацией о пользователе"""

    def __init__(self, id: int, name: str, lastname: str):
        self.id = id
        self.name = name
        self.lastname = lastname

    def __str__(self):
        """Метод toString для возвращения только имени и фамилии"""
        return self.name + ' ' + self.lastname

    def get_id(self):
        """Получить ID пользователя"""
        return self.id

    def get_name(self):
        """Получить имя пользователя"""
        return self.name

    def get_lastname(self):
        """Получить фамилию пользователя"""
        return self.lastname
