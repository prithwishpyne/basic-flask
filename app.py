from flask import Flask

app = Flask(__name__)

app.route('/')
def hello():
    return 'Hello from Flask!'

app.route('/testapi', methods=['GET'])
def test():
    return 'GET Api call working successfully'

if __name__ == "__main__":
    app.run()