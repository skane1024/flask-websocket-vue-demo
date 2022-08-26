import random
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

# create and configure the server
server = Flask(__name__)
CORS(server)
async_mode = None
thread = None
socketio = SocketIO(server, async_mode=async_mode, cors_allowed_origins="*")

def background_thread():
    while True:
        socketio.sleep(1)
        t = random.randint(10000, 10000000)
        socketio.emit('message_to_client', {'data': t})

@socketio.on('SEND_MESSAGE')
def client_send_message(data):
    print('client sent message to the server!')
    global thread
    # with thread_lock:
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    socketio.run(server,host='0.0.0.0', debug=True, port=8055)
