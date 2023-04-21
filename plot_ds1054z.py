from load_ds1054z_csv import *
import matplotlib.pyplot as plt


t,data = load_ds1054z_csv('top_rings_voltage.csv')

fig,ax = plt.subplots()
for i in range(0,len(data)):
	ax.plot(t,data[i])
plt.show()

