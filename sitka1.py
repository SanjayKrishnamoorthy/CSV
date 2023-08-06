import csv


infile = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(infile)

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

for row in csv_file:
    highs.append(int(row[5]))

print(highs[:5])

import matplotlib.pyplot as plt

plt.plot(highs, c="red")


plt.title("Daily high temp for Sitka Alaska, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()