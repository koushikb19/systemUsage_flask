from assets.cpu_stats_new import get_all_data, get_cpu_usage, get_mem_usage, get_gpu_usage, hasGpu
from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
CORS(app)


isConnected = False

# Gets all data from the System


@app.route('/getData', methods=['GET'])
def sendData():
    if request.method == "GET":
        return get_all_data()

# Gets only CPU usage


@app.route('/getData/cpu', methods=['GET'])
def sendCPUData():
    if request.method == "GET":
        return get_cpu_usage()

# Gets only Memory usage


@app.route('/getData/mem', methods=['GET'])
def sendMEMData():
    if request.method == "GET":
        return get_mem_usage()

# Gets only CPU usage


@app.route('/getData/gpu', methods=['GET'])
def sendGPUData():
    if request.method == "GET":
        return get_gpu_usage()


@app.route('/getData/hasGpu', methods=['GET'])
def sendHasGPU():
    return {"hasGPU": hasGpu()}


if __name__ == '__main__':
    app.run()
