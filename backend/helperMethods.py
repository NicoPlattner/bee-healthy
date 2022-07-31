import json
import os


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


