# ==============Group Members==================================
# Michelle Becerra mdbecerr@usc.edu
# Amirah Anwar anwara@usc.edu
# Reetinder Kaur reetindk@usc.edu

import math
import numpy as np
import matplotlib.pyplot as plt

# ==============Global Variables==================================
N = 10
X = np.zeros(shape=(N,2)) #reduced dimension output array
PA = np.ndarray(shape=(2,2)) #pivot array
col_num = -1

def main():
	#load text file
	f = open("fastmap-data.txt", 'r')
	result_matrix = []
	for line in f.readlines():
	    values_as_strings = line.split()
	    arr = np.array(map(float, values_as_strings))
	    result_matrix.append(arr)

	#convert to numpy array
	data_points = np.array(result_matrix)

	#get distances
	symetric_distances = data_points[:,2];

	#reduce current dimension to k
	k = 2;

	#fast map algorithm to reduce dimensionality
	coordinates, final_distances = fastMap(k, symetric_distances, data_points)

	print "coordinates in k-plane", coordinates
	print "objects with distances btw them", final_distances

	plot2Dplane(coordinates)

#plots the data points and adds labels from fast-wordlist 
def plot2Dplane(coordinates):
	#load text file
	f = open("fastmap-wordlist.txt", 'r')
	labels = []
	for line in f.readlines():
	    values_as_strings = line.split()
	    labels.append(values_as_strings[0])
	#plot
	plt.scatter(coordinates[:,0], coordinates[:,1])
	#add lables
	for i in range (0,N):
	    xy=(coordinates[:,0][i],coordinates[:,1][i])
	    plt.annotate(labels[i],xy)
	plt.show()

#returns the largest number and its index in array distances
def chooseDistantObjects(distances, data_points):
	index = np.argmax(distances)
	value = data_points[index][2]
	return value, index

#returns the distance between farthest object pair and any random object
def getDistance(o_i, o, objectPairs):
	if o_i == o:
		return 0;
	array1 = np.where(objectPairs[:, 0] == o_i)
	array2 = np.where(objectPairs[:, 1] == o)
	index = np.intersect1d(array1,array2)
	if not index:
		array1 = np.where(objectPairs[:, 0] == o)
		array2 = np.where(objectPairs[:, 1] == o_i)
		index = np.intersect1d(array1,array2)
	return objectPairs[index[0], 2]

#returns the coordinates of objects in k-plane
def fastMap(k, symetric_distances, objectPairs):
	global col_num
	global N

	if k <= 0:
		#return final coordinates and object pair distances
		return X, objectPairs
	else:
		col_num += 1

	#choose pivot objects
	farthest_dist, farthest_pair_index = chooseDistantObjects(symetric_distances, objectPairs)
	farthest_pair = objectPairs[farthest_pair_index, 0:2]

	o_a = farthest_pair[0] #object id having zero coordinate
	o_b = farthest_pair[1]

	#record ids of pivot objects
	PA[0][col_num] = o_a
	PA[1][col_num] = o_b

	#all inter object distances is zero
	if farthest_dist == 0:
		for i in range(0, N):
			X[i][col_num] = 0

	#first coordinate calculation for each object
	for i in range(1,N+1):
		dist_ai = getDistance(i, o_a, objectPairs)
		dist_bi = getDistance(i, o_b, objectPairs)
		x_i = (math.pow(dist_ai, 2) + math.pow(farthest_dist, 2) - math.pow(dist_bi, 2)) / (2*farthest_dist)
		X[i-1, col_num] = x_i

	objectPairsPrime = np.zeros(shape=(objectPairs.shape))

	#constructing the objectPairs with distances
	index = 0
	for i in range(1, N+1):
		for j in range(i+1, N+1):
			new_distance = math.pow(objectPairs[index][2], 2) - math.pow((X[i-1][col_num] - X[j-1][col_num]), 2)
			D = np.array([i, j, math.sqrt(new_distance)])
			objectPairsPrime[index] = D
			index += 1

	#recurrsion
	return fastMap(k-1, objectPairsPrime[:,2], objectPairsPrime)


if __name__ == "__main__":
    main()