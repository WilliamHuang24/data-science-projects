import csv
import matplotlib.pyplot as plt

import calendar

from collections import Counter
from datetime import datetime

x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


with open('f.csv', 'r', encoding='utf-8') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    noise_type = {}

    for row in reader:
        #if noise complaint
        if 'noise' in row[5].lower():
            date = datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p')

            desc = row[6]

            if desc in noise_type.keys():
                (noise_type[desc])[date.month - 1] = (noise_type[desc])[date.month - 1] + 1
            else:
                noise_type[desc] = [0] * 12


    for k in noise_type.keys():
        plt.plot(x, noise_type[k], label = k)

    plt.legend(loc=2, prop={'size': 5})
    plt.show()

    

    

    
    



    
