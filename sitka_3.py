# 1) changing the file to include all the ata for the year
# 2) change the title to daily and low high temperatures 2018
# 3)extract low temps from file and add to chart
# 4)shade in the area between high and low


import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")


csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))


# The enumerate() function returns both the index of each item and the value of each
# item ad you loop through a list

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


highs = []
dates = []
lows = []

#
# mydate = '2018-07-01'
# converted_date = datetime.strptime(mydate, '%Y-%m-%d')

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)


# print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt


fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

fig.autofmt_xdate()


plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)


plt.show()


# matplotlibs pyplot API has a convenience function called subplots() which acts as a
# utility wrapper and helps in creating common layouts of subplots, including the
# enclosing figure object, in a single cell.

fig2, a = plt.subplots(2)


a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")


plt.show()