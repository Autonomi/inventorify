from flask import Flask, render_template, flash, session, redirect
from flask.ext.github import GitHub
from flask.ext.session import Session

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = '8ee9ec236dfaec1256a2'
app.config['GITHUB_CLIENT_SECRET'] = '3154c945b7263b3b36377c1b77dcd9c72eeefe4a'
#app.config['GITHUB_BASE_URL'] = 'https://github.com/login/oauth/authorize'
#app.config['GITHUB_AUTH_URL'] = 'https://github.com/login/oauth/access_token'

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


@app.route('/login')
def login():
	return github.authorize()


@app.route('/callback', methods=["GET"])
@github.authorized_handler
def authorized(oauth_token):
	userID = verifySessionID()
	print("userID[" + str(userID) + "]")
	
	next_url = request.args.get('next')
	url_for('index')
	print(oauth_token)
	if oauth_token is None:
		print('Nothing here.')
		flash("Authorization failed.")
		return redirect('error.html')
	else:
		return redirect('index.html')

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