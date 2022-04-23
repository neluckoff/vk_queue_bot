import csv
from settings import path

"""Модуль для управления CSV файлом"""


def id_users_csv():
    """
    Метод для возвращения массива с ID пользователей,
    находящихся в CSV файле
    """
    data = []
    with open(path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            data.append(row["id"])
    return data


def id_in_csv(id):
    """Проверка на наличие пользователя в CSV файле"""
    result = False
    with open(path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if id == int(row['id']):
                result = True
    return result
