import time
import sys

for i in range(10):
    startTime = round(time.time() * 1000)
    for j in range(sys.maxsize-1):
        continue
    stopTime = round(time.time() * 1000)
    runTimes[i] = starTime - stopTime
    print("loop {} done\n".format(i))
