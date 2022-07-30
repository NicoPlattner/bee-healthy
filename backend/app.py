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

@app.route('/createAndAddHive/<user_id>', methods=['POST'])
def createAndAddHive(user_id):
    if request.method == 'POST':
        User.createAndAddHive(user_id, request.args.get('hiveName'), request.args.get('hiveLocationGPSString'),
                              request.args.get('hiveBeeType'))


# create a new user
@app.route('/createUser/<name>', methods=['POST'])
def createUser(name):
    if request.method == 'POST':
        helperMethods.addUser(name)
        return 'User ' + name + ' created'


if __name__ == '__main__':
    app.run()
