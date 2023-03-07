# https://developers.google.com/identity/protocols/oauth2

from flask import Flask, render_template, request, url_for, redirect, session
import requests
from base64 import b64decode
from json import loads
app = Flask(__name__, static_folder = 'static', static_url_path = '')
app.secret_key = "hello!"


googleID = 'HIDDEN'
googleSec = 'HIDDEN'
REDIRECT_URI  = 'http://127.0.0.1:5000/auth'


@app.route('/')
def hello():
    return app.send_static_file('login.html')

@app.route('/logout')
def logout():
    email = session.get("email")
    return render_template('loggedin.html', email=email)



@app.route('/login')
def login():


    # client id + redirect url + response=code + scope (in this case, just email profile for testing)
    # build to request an authorisation code and redirect user
    # https://developers.google.com/identity/openid-connect/openid-connect#exchangecode
    auth_url = (
        
        # end point for oauth request for google
        'https://accounts.google.com/o/oauth2/v2/auth?' +

         # request code
        'response_type=code&' +

        # personal registered oauth id
        f'client_id={googleID}&' +

        # where to take user after request approved
        f'redirect_uri={REDIRECT_URI}&' +

        # request just email to print back out to user
        'scope=email%20profile'
    )
    # print(redirect_uri)

    return redirect(auth_url)


@app.route('/auth')
def google_auth():
    # pull out response code given the request was accepted:
    authCode = request.args.get('code')

    # now build new request to get an access cookie.
    data = {
        # auth code received after sending other request
        'code': authCode,
        # application id
        'client_id': googleID,
        # application secret
        'client_secret': googleSec,

        # Where to go after sending the request for access token
        'redirect_uri': REDIRECT_URI,

        # type which is to get an access cookie
        'grant_type': 'authorization_code',
    }


    response = requests.post('https://oauth2.googleapis.com/token', 
                            data=data)

    GOOGLETOKEN = response.json()['id_token']
    decodedToken = GOOGLETOKEN.split(".")
    # print(decodedToken[1])

    # incorrect padding?? just add more padding 
    body = loads(b64decode(decodedToken[1] + "="))
    email = body.get('email')

    session["email"] = email
    
    # response should contain id token which contains info about user
    # decode jwt and pull email out
    # with access to email, send to logged in page with their email printed out

    return redirect(url_for('logout')) 
