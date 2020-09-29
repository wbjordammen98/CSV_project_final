import csv
from datetime import datetime
import matplotlib.pyplot as plt

print("\nSITKA RECORDS: \n")

open_file_sitka = open('sitka_weather_2018_simple.csv', "r")
csv_file_sitka = csv.reader(open_file_sitka, delimiter=",")
header_row_sitka = next(csv_file_sitka)

print(header_row_sitka)

for index_sitka, column_header_sitka in enumerate(header_row_sitka):
    print(index_sitka,column_header_sitka)

sitka_highs = []
sitka_lows = []
sitka_dates = []

for row_sitka in csv_file_sitka:
    try:
        sitka_high = int(row_sitka[5])
        sitka_low = int(row_sitka[6])
        the_sitka_date = datetime.strptime(row_sitka[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {the_sitka_date}")
    else:
        sitka_highs.append(sitka_high)
        sitka_lows.append(sitka_low)
        sitka_dates.append(the_sitka_date)



x = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(x)

print("\n DEATH VALLEY: \n")

open_file_DV = open('death_valley_2018_simple.csv', "r")
csv_file_DV = csv.reader(open_file_DV, delimiter=",")
header_row_DV = next(csv_file_DV)

print(header_row_DV)

for index_DV, column_header_DV in enumerate(header_row_DV):
    print(index_DV,column_header_DV)

DV_highs = []
DV_lows = []
DV_dates = []

for row_DV in csv_file_DV:
    try:
        DV_high = int(row_DV[4])
        DV_low = int(row_DV[5])
        the_DV_date = datetime.strptime(row_DV[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {the_DV_date}")
    else:
        DV_highs.append(DV_high)
        DV_lows.append(DV_low)
        DV_dates.append(the_DV_date)


fig, ax = plt.subplots(2)
fig.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize=16)
ax[0].set_title("SITKA AIRPORT, AK US")
ax[0].plot(sitka_dates,sitka_highs,c='red',alpha=0.5)
ax[0].plot(sitka_dates,sitka_lows,c='blue',alpha=0.5)
ax[0].fill_between(sitka_dates,sitka_highs,sitka_lows,facecolor='blue',alpha=0.05)
ax[0].tick_params(axis="x",labelsize=13)


ax[1].set_title("DEATH VALLEY, CA US")
ax[1].plot(DV_dates,DV_highs,c='red',alpha=0.5)
ax[1].plot(DV_dates,DV_lows,c='blue',alpha=0.5)
ax[1].fill_between(DV_dates,DV_highs,DV_lows,facecolor='blue',alpha=0.05)
ax[1].tick_params(axis="x",labelsize=13)

fig.autofmt_xdate()

plt.show()