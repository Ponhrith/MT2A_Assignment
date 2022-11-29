import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []

with open("TestCSV2.csv") as csvfile:
    plots = csv.reader(csvfile, delimiter = ",")

    for row in plots:
        x.append(row[0])
        y1.append(float(row[1]))
        y2.append(float(row[2]))

fig, ax = plt.subplot()
p1 = ax.bar(x, y1, color= 'cornflowerblue', width = 0.4)
p2 = ax.bar(x, y2, bottom = y1, color='darkorange', width = 0.4)

ax.bar_label(p1, Label_type ="center")
ax.bar_label(p2, Label_type ="center")

plt.title("AVERAGE PRICE PER CONTINENTAL REGION")
plt.legend(["Number of Countries", "Average price per region of 1GB (USD)"])
plt.xticks(fontsize = 6.5)
plt.show()
