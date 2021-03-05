import psutil
import GPUtil
from socket_app import socketio
import threading


class UsageThread(threading.Thread):
    def __init__(self):
        super(UsageThread, self).__init__()

    def get_all_data(self):
        while True:
            socketio.emit("usage_details", {
                "mem": self.get_cpu_usage(),
                "cpu": self.get_cpu_usage(),
                "gpu": self.get_gpu_usage()
            })

    def run(self):
        self.get_all_data()

    def get_cpu_usage(self):
        return 100 - psutil.cpu_percent(interval=1)

    def get_mem_usage(self):
        return 100 - psutil.virtual_memory().percent

    def get_gpu_usage(self):
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
            list_gpus.append(gpu.memoryUsed*100/gpu.memoryTotal)
        return list_gpus


if __name__ == '__main__':
    thread = UsageThread()
    print(thread.get_cpu_usage())
    print(thread.get_gpu_usage())
    print(thread.get_mem_usage())
