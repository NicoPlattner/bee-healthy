import json
import os

from flask import url_for

import Hive
import User


def deserialize(name):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(ROOT_DIR, f'data/{name}.json'), 'r') as f:
        target = json.load(f)
    return target


def serialize(obj, name):
    dict = {name: obj}
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(ROOT_DIR, f'data/{name}.json'), 'w') as f:
        json.dump(dict, default=lambda o: o.__dict__,
                   sort_keys=True, indent=4, fp=f)


def addHive(hive):
    hives = deserialize('hives')['hives']
    hives.append(hive)
    serialize(hives, 'hives')


def addUser(name):
    ser_obj = deserialize('users')
    ser_obj['users'].append(User.User(name))
    serialize(ser_obj, 'users')


def addHiveToUser(user_id, hive):
    users = deserialize('users')['users']
    for user in users:
        if user['userID'] == int(user_id):
            user['hives'].append(hive)
            serialize(users, 'users')
            return
    raise Exception(f'User with id {user_id} not found')


def addHive(userid, hiveName, hiveLocationGPSString, hiveBeeType):
    newHive = Hive.Hive(hiveName, hiveLocationGPSString, hiveBeeType)
    addHiveToUser(userid, newHive)
    hives = deserialize('hives')['hives']
    hives.append(newHive)
    serialize(hives, 'hives')
