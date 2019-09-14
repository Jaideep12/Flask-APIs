from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/super-simple')
def super_simple():
    return "Hello from planetary API"

if __name__=='__main__':
    app.run()