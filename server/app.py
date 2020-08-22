from flask import Flask, request, render_template

app = Flask(__name__)

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
