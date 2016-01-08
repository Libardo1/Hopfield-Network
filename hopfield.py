import numpy as np
import csv
import pdb
import matplotlib.pyplot as plt
import scipy
import sys
import copy

file_path = sys.argv[1]
integer = int(sys.argv[2])
input_set = []

#read the file input from the txt file
def read_file(file_path):
	with open(file_path, 'r+') as read_file:
		for line in read_file:
			input_set.append(line)

  
  
#train the hopfield and returns W
def train_hopfield(X):
	C = len(X[0])
	#Creates a set of weights between nodes in a Hopfield network whose
	#size is based on the length of the rows in the input data X.
	W = [[0 for j in range(0,C)] for i in range(0,C)]
	# Number of inputs
	R = len(X)

	W = np.array(W)
	for i in range(0,C):
		for j in range(i,C):
			W[i][j] = 0
			for c in range(0,R):
		 		W[i][j] = W[i][j] + X[c][i]*X[c][j]
			W[j][i] = W[i][j]
		  
	return W;

 
#test the hofield on trained weight and returns converging S
def use_hopfield(W,x):
	
	C = len(x[0])
	R = len(x)
	s_t = copy.deepcopy(x[0])
	s_t1 = [0 for j in range(0,C)]
	W = train_hopfield([x])
	while 1:
		diff = 0
		for i in range(C):
			s = 0
			for j in range(C):
				s = s + W[i][j]*s_t[j]
			if s >=0:
				s_t1[i] = 1
			else:
				s_t1[i] = -1	
			if s_t[i] != s_t1[i]:
				diff = diff + 1
		if diff == 0:
			break
		else:
			s_t = copy.deepcopy(s_t1)

	return numpy.array(s_t1)	 		 
		
#plot the output
def show_plot(s):
	digit = np.array(s).reshape(16,16)
	plt.imshow(digit, interpolation="nearest")
	plt.show()




#read_file(file_path)
#arr = []
#for row in input_set:
#	sets = row.split()
#	arr.append([1 if int(bit) == 1 else -1 for bit in sets])
	
		
	

#arr = np.array(arr)
#weight = train_hopfield(arr[0:4])
#y = arr[integer]
#s = use_hopfield(weight,y)
#digit = np.array(s).reshape(16,16)

