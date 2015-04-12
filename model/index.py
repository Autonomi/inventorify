#!/usr/bin/env python3

import os, json, bson, re
from bottle import Bottle, request

application = Bottle()
app = application

@app.route('/')
def index():
    return  '''
                test!
            '''

@app.route('/hello')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return 'Hello %s, how are you?' % name
