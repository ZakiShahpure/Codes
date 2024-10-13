#break infinite loop
import time
i=0
while True:
    i += 1
    if i>= 5:
        break
    time.sleep(1)
    print(i)