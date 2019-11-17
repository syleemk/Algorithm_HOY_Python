import random
import time

startTime = time.time()

ran = set()

while(len(ran) < 500):
    ran.add(random.randint(0,999999))

L = list(ran)
L.sort(reverse=True)

print(L[4])

endTime = time.time() - startTime
print("Time : " , endTime)