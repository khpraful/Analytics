import numpy as np
import matplotlib.pyplot as plt


x1 = [1,2,3,4,5]
y1 = [3,5,1, 7, 4]
x2 = [10, 20,30]
y2 = [17, 24, 11]
plt.bar(x1,y1, label = 'FL', color = 'red')
plt.bar(x2,y2, label = 'SL', color = 'green')
plt.show()