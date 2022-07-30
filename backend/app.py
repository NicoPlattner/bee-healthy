from flask import Flask, request
import User
import helperMethods

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getAllHives/<user_id>', methods=['POST'])
def getAllHives(user_id):
    if request.method == 'POST':
        return 'getAllHives' + user_id


@app.route('/createHive/<user_id>', methods=['POST'])
def createHive(user_id):
    if request.method == 'POST':
        helperMethods.addHive(user_id, request.args.get('hiveName'), request.args.get('hiveLocationGPSString'),
                              request.args.get('beeType'))
        return 'created hive for user ' + user_id


# create a new user
@app.route('/createUser/<name>', methods=['POST'])
def createUser(name):
    if request.method == 'POST':
        helperMethods.addUser(name)
        return 'User ' + name + ' created'


if __name__ == '__main__':
    app.run()
