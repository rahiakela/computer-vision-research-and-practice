from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/user")
def hello_user():
    return "User: Hello World!"


if __name__ == '__main__':
    # In order to make the server publicly available, the parameter
    # host=0.0.0.0 should be added when running the server application.
    app.run(host="0.0.0.0")
