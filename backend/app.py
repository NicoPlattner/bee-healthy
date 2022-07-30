from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getAllHives/<user_id>', methods=['POST'])
def getAllHives(user_id):
    if request.method == 'POST':
        return 'getAllHives' + user_id


if __name__ == '__main__':
    app.run()
