import time
import random

for i in range(5):
    print("This is loop with i: " + str(i))
    sleepTime = random.randint(1, 60)
    print("Random sleep time is: " + str(sleepTime))
    time.sleep(sleepTime)
    print("Weakup time...")


