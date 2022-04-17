import random


class VkQueue:
    def __init__(self):
        self.queue = []

    def create_queue(self):
        self.queue = []

    def add_to_queue(self, user_q):
        self.queue.append(user_q)

    def shaffle_queue(self):
        random.shuffle(self.queue)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def print_queue(self):
        return self.queue

    def del_person(self, user):
        self.queue.pop(user)
        a = []
        for i in self.queue:
            a.append(i)
        self.queue = a

    def get_first(self):
        return self.queue[0]

    def get_second(self):
        return self.queue[1]

    def search_by_id(self):
        a = []
        for i in range(len(self.queue)):
            a.append(self.queue[i].get_id())
        return a


    def search_index(self, id):
        return self.queue.index(id)

    def dirty_finger(self, index):
        c = self.queue[index]
        self.queue[index] = self.queue[0]
        self.queue[0] = c



class Users:
    def __init__(self, id: int, name: str, lastname: str):
        self.id = id
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return self.name + ' ' + self.lastname

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname
