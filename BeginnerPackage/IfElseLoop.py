import random
import os
import sys

#If Esle Loop
age = 11

if age >=21:
    print("you are eligible to drive on your own")
elif age >= 18:
    print ("you are eligible to drive under supervision")
else:
    print("you are not eligible to drive")

if ((age >=18) and (age <=21)):
    print("you are in perfect period")
elif ((age==14) or (age ==16)):
    print("you are lucky")
elif not (age==15):
    print ("you are saved")
else:
    print("all the best")
