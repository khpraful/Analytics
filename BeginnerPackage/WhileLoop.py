import random
import os
import sys

#While loop
random_num = random.randrange(0,20)

while (random_num != 10):
    print (random_num)
    random_num = random.randrange(0, 20)

i=0
while (i<=20):
    if (i%2 == 0):
        print (i)
    elif (i == 9):
        break
    else:
        i += 1
        continue
    i += 1

