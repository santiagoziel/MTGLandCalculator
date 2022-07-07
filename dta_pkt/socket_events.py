from flask_socketio import emit, SocketIO
from dta_pkt import socketio

@socketio.on('connect')
def user_conecting():
    print("server acknowledgment")
    emit("user acknowledgment", "acknowledgment")
