from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Column,Integer,String,Float
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'planets.db')

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/super-simple')
def super_simple():
    return jsonify(message='Sample text from super simple',message2='sample message 2')

@app.route('/not-found')
def not_found():
    return jsonify(message='Resource not found'),404

@app.route('/parameters')
def parameters():
    name=request.args.get('name')
    age=int(request.args.get('age'))

    if age<18:
        return jsonify(message='Sorry '+name+' you are not old enough'),401
    else:
        return jsonify(message='Welcome '+name+" you are old enough"),200

@app.route('/parameters-in-url/<string:name>/<int:age>')
def parameters_in_url(name:str,age:int):
    if age<18:
        return jsonify(message='Sorry '+name+' you are not old enough'),401
    else:
        return jsonify(message='Welcome '+name+" you are old enough"),200

if __name__=='__main__':
    app.run()