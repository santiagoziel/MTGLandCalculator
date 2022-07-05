from flask import request
from flask_socketio import emit, join_room, leave_room

from dta_pkt import socketio

#when user conects to the socket it changes his room number from empty to his current room
#and lets evrybody know a new user conected
@socketio.on('connect')
def user_conecting():
    print("server acknowledgment")
    emit("user acknowledgment", "acknowledgment")
