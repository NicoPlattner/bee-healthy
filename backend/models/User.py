import itertools
import helperMethods

import models.Hive

import json

class User:
    id_iter = itertools.count()

    def __init__(self, name):
        self.name = name
        self.userID = next(User.id_iter)
        self.hives = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
