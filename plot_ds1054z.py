import numpy as np
import matplotlib.pyplot as plt
import os
import sys 
import fileinput
import csv

name = 'top_rings_voltage.csv'

rd = []
with open(name,newline='') as csvfile:
	spamreader=csv.reader(csvfile,delimiter=',', quoting=csv.QUOTE_NONE)
	for row in spamreader:
		rd.append(row)

datasize = np.size(rd,0)-1
num_datas = np.size(rd,1)

t = np.zeros(datasize)
data = []
for i in range(0,num_datas):
	data.append(np.zeros(datasize))


for row in range(1,datasize):
	t[row] = float(rd[row][0])
for row in range(1, datasize):
	for col in range(0,num_datas-1):
		data[col][row] = float(rd[row][col+1])

fig,ax = plt.subplots()
for i in range(0,num_datas):
	ax.plot(t,data[i])
plt.show()

