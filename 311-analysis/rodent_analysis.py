import csv
import matplotlib.pyplot as plt

import calendar
import matplotlib.pyplot as plt


from collections import Counter
from datetime import datetime

locs = {}

with open('f.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')


    locs = {}

    for row in reader:
        if 'rodent' in row[5].lower():
            if row[7] in locs.keys():
                locs[row[7]] = locs[row[7]] + 1
            else:
                locs[row[7]] = 1

    locations = list(locs.keys())
    values  = list(locs.values())

    plt.bar(locations, values, color ='maroon', 
        width = 0.4)
            

    plt.xlabel("Locations")
    plt.xticks(rotation=90)
    plt.ylabel("# of reports")
    plt.show()