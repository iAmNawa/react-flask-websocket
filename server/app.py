from flask import Flask, request, render_template
from flask_cors import CORS
from tinydb import TinyDB, Query
db = TinyDB('db.json')

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    ws = request.environ['wsgi.websocket']
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)

@app.route('/get-request')
def get_request():
    print('get request')
    return ('hello')
