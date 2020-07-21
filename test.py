import sys
import GPUtil
import psutil
import math
import time

gpulist = []
memory = []
cpu = []



while True:
    # f = open('./log/2.txt', 'a+')
    # sys.stdout = f
    gpus = GPUtil.getGPUs()
    GPUtil.showUtilization()
    for gpu in gpus:
        gpulist.append(gpu.memoryUsed)
        print('总gpu:', gpu.memoryTotal, 'gpuused:', gpu.memoryUsed)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()  #

    mem_total = mem[0]/math.pow(1024, 3)
    mem_used = mem[2]
    mem1 = mem[3]/math.pow(1024, 3)
    memory.append(mem_used)
    print('cpu:', str(cpu) + '%，', '总memory:', round(mem_total), '占用率', str(mem_used) + '%，', 'memory used:', str(mem1))
    time.sleep(1)
