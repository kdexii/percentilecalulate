import psutil
import time
import json
import numpy as np
from tqdm import tqdm
summ = []
start_time = float(time.time())
def welcome ():
    print('☻ cpu load percentile calculator ☻')
    print('Program created by Gorila')
"""
///
@cpuStat - collecting cpu load
///
"""
def cpuStat ():
    count = 0
    while True:
        data = psutil.cpu_percent(0)
        time.sleep(1)
        print('processor load:',data, '%')
        count += 1
        summ.append(data)
        
        if count == 20:
            break
"""
///
@cpuStat - entering the percentile and counting it
///
"""
def percCountSumm ():
    print('enter the percentile value:')
    percCount = input()
    percCount = float(percCount)
    perc = np.percentile(summ, percCount)
    perc = str(perc)
    print('summ percentile value :  ',perc)
"""
///
@all - func call
///
"""
welcome()
cpuStat()
percCountSumm()
print('converted float:', summ,  
    ',to type:', type(summ).__name__)
print("the program was completed in %s seconds\n" % (time.time() - start_time))