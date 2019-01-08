from flask import Flask

app = Flask(__name__)


@app.route('/greet')
def greet():
    return '<h1>Hello World!<h1>'

@app.route('/greet/<name>')
def greet_name(name):
    return '<h1>Hello, {}<h1>'.format(name)


if __name__ == '__main__':
    app.run()
