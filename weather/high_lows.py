import csv

from matplotlib import pyplot as plt

# Get the data
filename = "sitka_weather_07-2018.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    highs = []
    for column in reader:
        high = int(column[4])
        highs.append(high)
        
    print(highs)
 
#    for index, column_header in enumerate(header_row):
#        print(index, column_header)

# Plot data

fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(highs, c = 'red')

plt.title("Daily High Temperature, 07/2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
plt.ylabel('temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
