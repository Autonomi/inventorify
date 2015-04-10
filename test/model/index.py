from flask import Flask, render_template, request, session
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'stock'
mongo = PyMongo(app)

data = []
@app.route('/')
def index():
	stock = mongo.db.available.find()
	for i in stock:
		print(i)
		data.append(i)
		print(len(data))
	return render_template('index.html')

app.run(host='localhost',port=8888,debug=True)