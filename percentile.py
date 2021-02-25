import psutil
import time
import json
import numpy as np
summ = []
start_time = time.time()

def cpuStat ():
    count = 0
    while True:
        data = psutil.cpu_percent(1)
        time.sleep(1)
        print(data)
        count += 1
        summ.append(data)
        if count == 10:
            break

cpuStat()