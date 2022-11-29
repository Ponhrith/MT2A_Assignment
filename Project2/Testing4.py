# workable

import csv
import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []

with open("TestCSV2.csv") as csvfile:
    plots = csv.reader(csvfile, delimiter = ",")

    for row in plots:
        x.append(row[0])
        y1.append(float(row[2]))
        y2.append(float(row[2]))

plt.bar(x, y1, color= 'r')
plt.bar(x, y2, bottom = y1, color='b')
plt.show()




# plt.bar(x, y, color = 'g', width = 0.72, label = "Age")
# plt.xlabel('Names')
# plt.ylabel('Ages')
# plt.title('Ages of different persons')
# plt.legend()
# plt.show()