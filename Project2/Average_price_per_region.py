import csv
import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []

with open("Average_price_per_region.csv", 'r') as csvfile:
    csvreader_object = csv.reader(csvfile)
    next(csvreader_object)
    plots = csv.reader(csvfile, delimiter = ",")

    for row in plots:
        x.append(row[0])
        y1.append(float(row[1]))
        y2.append(float(row[2]))



plt.bar(x, y1, color= 'cornflowerblue', width = 0.4)
plt.bar(x, y2, bottom = y1, color='darkorange', width = 0.4)
plt.title("AVERAGE PRICE PER CONTINENTAL REGION")
plt.legend(["Number of Countries", "Average price per region of 1GB (USD)"])
plt.xticks(fontsize = 6.5)
plt.show()
