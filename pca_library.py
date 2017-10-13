import numpy as np
from sklearn.decomposition import PCA as sk

f = open("pca-data.txt", 'r')
result_matrix = []
for line in f.readlines():
	values_as_strings = line.split()
	arr = np.array(map(float, values_as_strings))
	result_matrix.append(arr)
X = np.array(result_matrix)

sklearn_pca = sk(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(X)

print sklearn_pca.components_