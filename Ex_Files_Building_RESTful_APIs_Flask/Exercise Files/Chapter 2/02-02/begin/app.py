from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/super-simple')
def super_simple():
    return jsonify(message='Sample text from super simple',message2='sample message 2')

if __name__=='__main__':
    app.run()