from dta_pkt import app, socketio

if __name__ == "__main__":
    #app.run(debug = True, host='0.0.0.0')
    socketio.run(app, debug = True)
