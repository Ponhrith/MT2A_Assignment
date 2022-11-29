#work

import csv
import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []

with open("TestCSV2.csv") as csvfile:
    plots = csv.reader(csvfile, delimiter = ",")

    for row in plots:
        x.append(row[0])
        y1.append(float(row[1]))
        y2.append(float(row[2]))

plt.bar(x, y1, color= 'r')
plt.bar(x, y2, bottom = y1, color='b')
plt.title("AVERAGE PRICE PER CONTINENTAL REGION")
plt.legend(["Number of Countries", "Average price per region of 1GB (USD)"])
plt.show()
