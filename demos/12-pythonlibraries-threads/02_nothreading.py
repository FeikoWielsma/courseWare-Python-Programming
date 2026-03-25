import time
 
threadBreak = False
def TimeProcess():
    while not threadBreak:
        print (time.time() - startTime)
 
startTime = time.time()
 
TimeProcess()
 
input()
threadBreak = True 
quit()