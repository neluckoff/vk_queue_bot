import csv
from settings import path


def id_users_csv():
    data = []
    with open(path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            data.append(row["id"])
    return data


def id_in_csv(id):
    result = False
    with open(path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if id == int(row['id']):
                result = True
    return result

