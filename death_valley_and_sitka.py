import csv

open_file1 = open("sitka_weather_2018_simple.csv", "r")

open_file2 = open("death_valley_2018_simple.csv", "r")

from datetime import datetime


csv_file1 = csv.reader(open_file1, delimiter=",")

csv_file2 = csv.reader(open_file2, delimiter=",")


header_row1 = next(csv_file1)
header_row2 = next(csv_file2)


print(type(header_row1))
print(type(header_row2))


for index, column_header in enumerate(header_row1):
    print("Index:", index, "Column Name:", column_header)

for index, column_header in enumerate(header_row2):
    print("Index:", index, "Column Name:", column_header)


highs = []
dates = []
lows = []
highs2 = []
lows2 = []
dates2 = []

for row in csv_file1:
    try:
        high = int(row[5])
        low = int(row[6])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(converted_date)

for row in csv_file2:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(converted_date)
"""
print(dates[:20])
print(dates2[:20])
"""
import matplotlib.pyplot as plt


fig, ax = plt.subplots(2)


ax[0].plot(dates, highs, c="red")
ax[0].plot(dates, lows, c="blue")
ax[1].plot(dates2, highs2, c="red")
ax[1].plot(dates2, lows2, c="blue")


ax[0].set_title("Sitka Airport, AK US")
ax[1].set_title("Death Valley, CA US")
ax[0].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax[1].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
fig.suptitle("Temperature Comparison for Sitka and Death Valley")


plt.show()
