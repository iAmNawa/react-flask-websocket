from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template
import asyncio
import websockets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            message = ws.receive()
            ws.send(message)
    return

#if __name__ == '__main__':
#    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
#    http_server.serve_forever()

start_server = websockets.serve(app, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
