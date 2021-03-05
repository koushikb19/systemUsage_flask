from socket_app import app, socketio


def socketio_test():
    # log the user in through Flask test client
    flask_test_client = app.test_client()

    # connect to Socket.IO without being logged in
    socketio_test_client = socketio.test_client(
        app, flask_test_client=flask_test_client
    )

    # make sure the server rejected the connection
    assert socketio_test_client.is_connected()

    r = socketio_test_client.get_received()
    print(r)


if __name__ == '__main__':
    socketio_test()
