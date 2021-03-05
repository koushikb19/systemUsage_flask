from cpu_stats_new import get_all_data
from socket_app import socketio, app

isConnected = False


@socketio.on('connect')
def handle_connect():
    print("Connected")


@socketio.on('get_data')
def handle_get_data():
    socketio.emit("send_data", get_all_data())


if __name__ == '__main__':
    socketio.run(app)
