import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('test_file.txt', 'r') as csvfile:
    values = csv.reader(csvfile, delimiter=',')
    for row in values:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label = "Reading from file")
plt.xlabel("X-label")
plt.ylabel("Y-label")
plt.title("My Graph\nHops it's good!")
plt.legend()
plt.show()




