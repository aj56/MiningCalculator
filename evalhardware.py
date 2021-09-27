#Only public version of code attached

import platform
import GPUtil
import nicehash

def apicrypto():
    host = 'https://api2.nicehash.com'
    public_api = nicehash.public_api(host)
    buy_info = public_api.get_current_global_stats()
    print(buy_info)

def cpustats():
    uname = platform.uname()
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

def gpustats():
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        list_gpus.append((gpu_id, gpu_name))
    print(list_gpus)

if __name__ == "__main__":
    apicrypto()             # api to get mining info.
    cpustats()              # general cpu stats
    gpustats()              #only nvidia worthy
