from flask import Flask, render_template, flash, session, redirect, request, url_for
from flask.ext.github import GitHub
from flask.ext.session import Session
from config import github_client_id, github_client_secret, github_base_url, github_auth_url

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = github_client_id
app.config['GITHUB_CLIENT_SECRET'] = github_client_secret
app.config['GITHUB_BASE_URL'] = github_base_url
app.config['GITHUB_AUTH_URL'] = github_auth_url

github = GitHub(app)

sess = Session()

nextID = 0

def verifySessionID():
	global nextID

	if not 'userID' in session:
		session['userID']=nextID
		nextID += 1
		sessionID = session['userID']
		print("set userID[" + str(session['userID']) + "]")
	else:
		print("using already set userID[" + str(session['userID']) + "]")

	sessionID = session.get('userID', None)
	return sessionID

#return access token as part of URL when redirected to the callback URL mentioned.
@app.route('/login')
def login():
	print('	here1')
	return github.authorize()


@app.route('/github-callback', methods=["GET"])
@github.authorized_handler
def authorized(oauth_token):
	print('here2')
	next_url = request.args.get('next')
	print(next_url)
	#next_url = url_for('index')

	print(oauth_token)
	
	userID = verifySessionID()
	print("userID[" + str(userID) + "]")

	if oauth_token is None:
		flash("Authorization failed.")
		return redirect('next_url')
	#else:
	#	return redirect('index.html')

	user = User.query.filter_by(github_access_token=oauth_token).first()
	if user is None:
		user = User(oauth_token)
		db_session.add(user)

	user.github_access_token = oauth_token
	db_session.commit()
	return redirect(next_url)

if __name__=="__main__":
	app.secret_key = 'secret key'
	app.config['SESSION_TYPE'] = 'mongodb'
	sess.init_app(app)
	app.run(host='localhost',port=8888,debug=True)