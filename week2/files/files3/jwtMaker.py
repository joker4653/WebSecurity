import jwt
from flask import Flask, session, request

app = Flask(__name__)

# Define a secret key for signing the JWT
app.secret_key = '$hallICompareTHEE2aSummersday'

@app.route('/')
def generate():
    # set values

    session['role'] = 'staff'
    session['username'] = 'staff'



    # Return the JWT as a response to the client
    return 'go to /getCookie'


@app.route('/getCookie')
def cookie():
    session_id = session.sid
    
