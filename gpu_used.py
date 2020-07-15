import GPUtil
import time
import psutil
import math
import process

gpulist = []
memory = []
cpu = []


while True:
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        gpulist.append(gpu.memoryUsed)
        print('gpuall: ', gpu.memoryTotal, ' ', 'gpuused：', gpu.memoryUsed)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    # print(mem)
    mem_total = mem[0]/math.pow(1024, 3)
    mem_used = mem[2]
    mem1 = mem[3]/math.pow(1024, 3)
    memory.append(mem_used)
    print('cpu: ', str(cpu) + '%', "  ", 'mem：', round(mem_total), '占用率', str(mem_used) + '%', '使用：', str(mem1))
    # print('内存：', round(mem_total), str(mem_used) + '%')
    # with open ('g:/test.txt', 'w') as f:
    #     f.writelines()
    time.sleep(3)