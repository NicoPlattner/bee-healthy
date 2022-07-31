import json

from helperMethods import deserialize, serialize


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


def getHives(user_id):
    users = deserialize('users')['users']
    for user in users:
        if user['userID'] == int(user_id):
            return json.dumps(user['hives'], default=lambda o: o.__dict__,
                              sort_keys=True, indent=4)
    raise Exception(f'User with id {user_id} not found')


def getHive(user_id, hive_id):
    users = deserialize('users')['users']
    for user in users:
        if user['userID'] == int(user_id):
            for hive in user['hives']:
                if hive['id'] == int(hive_id):
                    return json.dumps(hive, default=lambda o: o.__dict__,
                                      sort_keys=True, indent=4)
    return 'Hive not found'
