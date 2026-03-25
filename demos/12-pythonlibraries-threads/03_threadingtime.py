import threading
import time
 
threadBreak = False
def TimeProcess():
    while not threadBreak:
        print (time.time() - startTime)
 
startTime = time.time()
 
threading.Thread(target = TimeProcess).start()
 
input()
threadBreak = True
quit()