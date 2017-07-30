import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('test_file.txt', delimiter='\t')

x = np.linspace(0,1,5)
y = np.array([1,2,3.5,10,20])
print(np.mean(x), np.max(x), np.min(x))
plt.plot(y,x,)
plt.show()

