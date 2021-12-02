import os
import time
from datetime import datetime

def BGT_disktest():
    while True:
        print ("wait progress 10 m")
        localtime = time.localtime()
        result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
        print(result)
        time.sleep(3)
        with open('C:/Program Files (x86)/Universal RAID Utility/server/raid.log') as f:
            if 'Initiaze start' in f.read():
                print("pass")
                break
    
            else:
                continue
    
        #os.system("storcli /c0/v4 start cc")
BGT_disktest()
