from flask import Flask, request, abort
from flask_cors import CORS

import controllers.HiveController
import controllers.UserController

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getAllHives/<user_id>', methods=['GET'])
def getAllHives(user_id):
    if request.method == 'GET':
        return controllers.HiveController.getHives(user_id)


@app.route('/createHive/<user_id>', methods=['POST'])
def createHive(user_id):
    if request.method == 'POST':
        controllers.HiveController.addHive(user_id, request.args.get('hiveName'), request.args.get('hiveLocationGPSString'),
                                           request.args.get('beeType'))
        return 'created hive for user ' + user_id


# get a hive by id
@app.route('/getHive/<user_id>/<hive_id>', methods=['GET'])
def getHive(hive_id, user_id):
    if request.method == 'GET':
        response = controllers.HiveController.getHive(user_id, hive_id)
        if response == 'Hive not found':
            abort(404, description="Hive not found")
        return controllers.HiveController.getHive(user_id, hive_id)


# create a new user
@app.route('/createUser/<name>', methods=['POST'])
def createUser(name):
    if request.method == 'POST':
        controllers.UserController.addUser(name)
        return 'User ' + name + ' created'


if __name__ == '__main__':
    app.run()
