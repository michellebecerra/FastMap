# ==============Group Members==================================
# Michelle Becerra mdbecerr@usc.edu
# Amirah Anwar anwara@usc.edu
# Reetinder Kaur reetindk@usc.edu

import random
import numpy as np
import sys

def main():
	f = open("pca-data.txt", 'r')
	result_matrix = []
	for line in f.readlines():
	    values_as_strings = line.split()
	    arr = np.array(map(float, values_as_strings))
	    result_matrix.append(arr)
	X = np.array(result_matrix)
	
	x_mu = np.mean(X[:,0])
	y_mu = np.mean(X[:,1])
	z_mu = np.mean(X[:,2])

	mu = np.array([x_mu,y_mu,z_mu])

	# Dim: 6000X3
	D = X - mu
	N = len(result_matrix)
	# Dim: 3x3
	Cov = (1.0/N)*np.dot(D.T,D)
	eig_val, eig_vec = np.linalg.eig(Cov)


	eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(len(eig_val))]

	#Sort by decreaing eigenvalues
	eig_pairs.sort(key=lambda x: x[0], reverse=True)
	#for i in eig_pairs:
		#print i[0], " , ", i[1]
	U = np.array([eig_pairs[0][1], eig_pairs[1][1]])
	print 'Direction of PC1: ', U[0,:], "\n", 'Direction of PC2: ', U[1,:]

	U_prime = U.T

	#2D Representation
	Z = []
	for i in range(N):
		Z.append(np.dot(X[i],U_prime))
	Z = np.array(Z)


if __name__ == "__main__":
    main()