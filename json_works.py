import json

def id_users_json():
    id_array = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            id_array.append(p['id'])
    li = []
    for i in id_array:
        if i not in li:
            li.append(i)
    return li


def all_users_json():
    all_array = []
    with open('data.json') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            all_array.append(str(p['first_name'+ ' ' + p['last_name']]))
    li = []
    for i in all_array:
        if i not in li:
            li.append(i)
    return li