import csv
import numpy as np

def load_ds1054z_csv(filename):
	rd = []
	with open(filename,newline='') as csvfile:
		spamreader=csv.reader(csvfile,delimiter=',', quoting=csv.QUOTE_NONE)
		for row in spamreader:
			rd.append(row)

	datasize = np.size(rd,0)-1
	num_datas = np.size(rd,1)-1

	t = np.zeros(datasize)
	data = []
	for i in range(0,num_datas):
		data.append(np.zeros(datasize))


	for row in range(0,datasize):
		t[row] = float(rd[row+1][0])
	for row in range(0, datasize):
		for col in range(0,num_datas):
			data[col][row] = float(rd[row+1][col+1])
	return t, data
