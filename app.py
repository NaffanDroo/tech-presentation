from flask import Flask, render_template, redirect, url_for
from authlib.flask.client import OAuth
from loginpass import create_flask_blueprint, GitHub, Google

name = ''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobesecret'
app.config['GOOGLE_CLIENT_ID'] = '258173943691-hnojrp0pq26hvlq70rojik8floes0lc4.apps.googleusercontent.com'
app.config['GOOGLE_CLIENT_SECRET'] = 'aKwAWp99QWUC2FJVrWLvLKOm'
# app.config['GITHUB_CLIENT_ID'] = 'd81dd1fec70005886003'
# app.config['GITHUB_CLIENT_SECRET'] = 'a6f97b93a5f9235696ef72591261bf21c5364477'
oauth = OAuth(app)

def handle_authorize(remote, token, user_info):
    print('handle authorizer')
    global name
    name = user_info['name']
    print(user_info)
    return render_template('layout.html', name=name)
    # if token:
    #     save_token(remote.name, token)
    # if user_info:
    #     save_user(user_info)
    #     return user_page
    # raise some_error

google_bp = create_flask_blueprint(Google, oauth, handle_authorize)
app.register_blueprint(google_bp, url_prefix='/google')

@app.route('/google/auth')
def github_login():
    return '<h1>Success</h1>'
    return render_template('layout.html')

@app.route('/test')
def user():
    return '<h1>{}</h1>'.format(name) 