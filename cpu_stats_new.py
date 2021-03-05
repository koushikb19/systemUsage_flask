import psutil
import GPUtil
from socket_app import socketio


def get_all_data():
    return {
        "mem": get_cpu_usage(),
        "cpu": get_cpu_usage(),
        "gpu": get_gpu_usage()
    }


def get_cpu_usage():
    return 100 - psutil.cpu_percent(interval=1)


def get_mem_usage():
    return 100 - psutil.virtual_memory().percent


def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        list_gpus.append(gpu.memoryUsed*100/gpu.memoryTotal)
    return list_gpus
