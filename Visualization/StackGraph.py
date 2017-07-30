import numpy as np
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
sleeping = [8,7,6,8,9,10,10]
working =  [8,7,8,7,9,2,2]
eating =   [1,2,3,2,1,4,4]
playing=   [7,8,8,8,5,8,8]
plt.stackplot(days, sleeping,working,eating,playing, colors = ['r','b','c','y'])
plt.show()