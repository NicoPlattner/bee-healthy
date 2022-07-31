from models import User
from helperMethods import deserialize, serialize


def addUser(name):
    ser_obj = deserialize('users')
    ser_obj['users'].append(User.User(name))
    serialize(ser_obj, 'users')
