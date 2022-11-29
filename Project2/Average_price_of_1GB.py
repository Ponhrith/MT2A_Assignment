import csv
import matplotlib.pyplot as plt

x = []
y2020 = []
y2021 = []


with open("Average_price_of_1GB.csv",'r') as csvfile:
    csvreader_object = csv.reader(csvfile)
    next(csvreader_object)
    plots = csv.reader(csvfile, delimiter = ",")

    for row in plots:
        x.append(row[0])
        y2020.append(float(row[1]))
        y2021.append(float(row[2]))
      


plt.plot(x, y2020, color = 'cornflowerblue', linestyle = 'dashed', marker = 'o')
plt.plot(x, y2021, color = 'darkorange', linestyle = 'dashed', marker = 'o')
plt.ylim([0,8])
plt.title("Average price of 1GB(USD at the start of 2020 and 2021)")
plt.legend(["2021", "2020"])
plt.xticks(fontsize = 6.5)
plt.grid()
plt.show()