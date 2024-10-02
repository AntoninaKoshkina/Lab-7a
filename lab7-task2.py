import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('data2.csv', delimiter=',')

with open('data2.csv', 'r') as file:
    header = file.readline().strip().split(',')


column4_name = str(header[3])
column4 = data[:, 3]


std_dev = np.nanstd(column4)

plt.hist(column4, bins = 20, edgecolor='black')
plt.title("Histogram of " + column4_name + " value frequency")
plt.xlabel("Значение")
plt.ylabel("Частота")


plt.text(0.0, 0.95, f"Cреднеквадратичное отклонение: {std_dev:.2f}", transform=plt.gca().transAxes)
plt.show()
