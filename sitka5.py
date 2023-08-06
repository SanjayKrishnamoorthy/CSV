
import csv
from datetime import datetime
import matplotlib.pyplot as plt

infile = open("sitka_weather_2018_simple.csv")
csv_file = csv.reader(infile)
header_row = next(csv_file)

station_index = -1
name_index = -1
name = ""
tempmax_index = -1
tempmin_index = -1
date_index = -1

for index, column_header in enumerate(header_row):
    print(index, column_header)
    if column_header == "STATION":
        station_index = index
    if column_header == "NAME":
        name_index = index
    if column_header == "TMAX":
        tempmax_index = index
    if column_header == "TMIN":
        tempmin_index = index
    if column_header == "DATE":
        date_index = index

highs = []
lows = []
dates = []

for row in csv_file:
    try:
        some_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        high = int(row[tempmax_index])
        low = int(row[tempmin_index])
    except ValueError:
        print(f"\nMissing data for {row[date_indexate_index]}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(some_date)
        nameame = row[name_index]

infile_dv = open("death_valley_2018_simple.csv")
csv_file_dv = csv.reader(infile_dv)
header_row_dv = next(csv_file_dv)

dv_station_index = -1
dv_name_index = -1
dv_name = ""
dv_tempmax_index = -1
dv_tempmin_index = -1
dv_date_index = -1

print("Index and Column Header for Death Valley")
for index, column_header in enumerate(header_row_dv):
    print(index, column_header)
    if column_header == "STATION":
        dv_station_index = index
    if column_header == "NAME":
        dv_name_index = index
    if column_header == "TMAX":
        dv_tempmax_index = index
    if column_header == "TMIN":
        dv_tempmin_index = index
    if column_header == "DATE":
        dv_date_index = index

highs_dv = []
lows_dv = []
dates_dv = []

for row in csv_file_dv:
    try:
        some_date = datetime.strptime(row[dv_date_index], "%Y-%m-%d")
        high = int(row[dv_tempmax_index])
        low = int(row[dv_tempmin_index])
    except ValueError:
        print(f"\nMissing data for {row[dv_date_index]}")
    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(some_date)
        dv_name = row[dv_name_index]

fig = plt.figure()

plt.suptitle(f"Temperature comparison between {name} and {dv_name}")

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.2)

plt.title(f"{name}", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.subplot(2, 1, 2)
plt.plot(dates_dv, highs_dv, c="red", alpha=0.5)
plt.plot(dates_dv, lows_dv, c="blue", alpha=0.5)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor="blue", alpha=0.2)

plt.title(f"{dv_name}", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()