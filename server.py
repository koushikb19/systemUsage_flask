from cpu_stats import UsageThread
from socket_app import socketio, app

thread = UsageThread()


@socketio.on('connect')
def handle_connect():
    thread.start()


if __name__ == '__main__':
    socketio.run(app)
