import numpy as np
import matplotlib.pyplot as plt

ages = [10,15,13,20,78,43,56,22,31,45,67,130,98,76,67,90,80,70,45,1,5,36,12,94]
ids = [x for x in range (len(ages))]
sections = [20,40,60,80,100,120,140]
plt.hist(ages, sections, histtype='bar',label = 'AB')
plt.show()




