from requests_oauthlib import OAuth2Session

from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify

app = Flask(__name__)

# This information is obtained upon registration of a new GitHub
client_id = "8ee9ec236dfaec1256a2"
client_secret = "3154c945b7263b3b36377c1b77dcd9c72eeefe4a"
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

@app.route("/login")
def login():
	github = OAuth2Session(client_id)
	authorization_url, state = github.authorization_url(authorization_base_url)

	# State is used to prevent CSRF, keep this for later.
	session['oauth_state'] = state
	return redirect(authorization_url)

@app.route("/callback")
def callback():
	github = OAuth2Session(client_id, state=session['oauth_state'])
	token = github.fetch_token(token_url, client_secret=client_secret,
							   authorization_response=request.url)
	print(token)
	return jsonify(github.get('https://api.github.com/user').json())

if __name__=="__main__":
	app.secret_key = 'secret key'
	app.run(host='localhost',port=8888,debug=True)