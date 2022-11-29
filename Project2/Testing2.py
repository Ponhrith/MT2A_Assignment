import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('TestCSV.csv')
continental_region = df["Continental Region"]
num_of_count = df["Number of Countries"]
ave_price = df["Average price of 1GB (USD)"]

plt.bar(continental_region, num_of_count)
plt.bar(continental_region, ave_price, bottom = num_of_count)



plt.show()