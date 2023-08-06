    #1) Changing the file to include all the data for the year of 2018
    #2) change the title to - daily and low high temperatures - 2018
    #3) extract low temps from the file and add to the chart
    #4) shade in the area between high and low


import csv
from datetime import datetime

infile = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(infile)

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []

some_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
print(type(some_date))

for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    dates.append(datetime.strptime(row[2], "%Y-%m-%d"))

print(highs[:5])
print(dates[:5])


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red", alpha = 0.5)
plt.plot(dates, lows, c="blue", alpha = 0.5)

plt.fill_between(dates,highs,lows, facecolor='blue',alpha = 0.1)


plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("Dates", fontsize=16)
plt.ylabel("Temps(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()