import psutil
import GPUtil

# returns usage of CPU, GPU and Memory


def get_all_data():
    return {
        "mem": get_mem_usage(),
        "cpu": get_cpu_usage(),
        "gpu": get_gpu_usage()
    }

# returns CPU usage


def get_cpu_usage():
    return {"cpu": 100 - psutil.cpu_percent(interval=1)}

# returns GPU usage


def get_mem_usage():
    return {"mem": 100 - psutil.virtual_memory().percent}

# Checks if system has a GPU


def hasGpu():
    gpus = GPUtil.getGPUs()
    if len(gpus) == 0:
        return False
    return True

# returns GPU usage


def get_gpu_usage():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        list_gpus.append(gpu.memoryUsed*100/gpu.memoryTotal)
    return {"gpu": list_gpus}
