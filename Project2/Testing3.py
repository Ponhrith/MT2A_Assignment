import csv 
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
z = []
N = 13

with open("TestCSV.csv", 'r') as csvfile:

    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
        z.append(int(row[2]))

ind = np.arrange(N)
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ind, y, width, color='r')
ax.bar(ind, z, width, bottom=y, color='b')
plt.title('AVERAGE PRICE PER CONTINENTAL REGION')
ax.legend(labels=["Number of Countrie", "Average price per region of 1GB (USD)"])


plt.show()



