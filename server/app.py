from flask import Flask, request, render_template
from flask_cors import CORS
from tinydb import TinyDB, Query
db = TinyDB('./db/db.json')
db2 = TinyDB('./db/questions.json')

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
    db.insert({'hello': 'hello'})
    return ('hello')

@app.route('/query-db')
def query_db():
    Question = Query()
    actual_ques = db2.search(Question.question_num == 'one')[0]
    print(actual_ques)
    return (actual_ques)
