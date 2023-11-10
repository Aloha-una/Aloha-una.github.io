#Tuyet Nguyen - Date Oct 9 - CS135-03 lab 6 Plotting with Python

import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file using numpy
data = np.loadtxt('lab6.csv',dtype = 'str', usecols =(0,2,3,4,5), skiprows = 1, delimiter=',', unpack = True)

# Extract the columns for Year, Gold, CPI, National Debt, and House Price
year = data[0]
cpi = data[1]
house_price = data[2]
gold = data[3]
nation_debt = data[4]

# Create an array of x-values for positioning 
x = np.arange(len(year))

# Create the chart

plt.plot(year, gold, label='Gold', color='yellow')
plt.plot(year, cpi, label='CPI', color='blue')
plt.plot(year, nation_debt, label='National Debt', color='red')
plt.plot(year, house_price, label='House Price', color='green')

# Customize the plot
plt.title('Trends Over Time')
plt.xlabel('Year', fontsize =18)
plt.ylabel('Adjusted Dollars - $')
plt.xticks(x, year, rotation=45, fontsize=8)
plt.grid(axis='x', linestyle='--', linewidth=0.5)
plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()  
plt.show()