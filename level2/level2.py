import numpy as np
import math
from sys import argv

matrixTerrain = []
matrixCountry = []
dimensions = None

with open(argv[1], 'r') as f:
	firstLine = True
	for line in f:
		if firstLine:
			firstLine = False
			dimensions = [int(num) for num in line.split(' ')]
			continue
		arrTerrain = []
		arrCountry = []
		i = 0
		for num in line.split(' '):
			if i % 2 == 0:
				arrTerrain.append(int(num))
			else:
				arrCountry.append(int(num))
			i += 1
		matrixTerrain.append(arrTerrain)
		matrixCountry.append(arrCountry)

# print(matrixTerrain)

# print('{} {} {}'.format(np.amin(matrixTerrain), np.amax(matrixTerrain), math.floor(np.mean(matrixTerrain))))

# print(matrixCountry)
# print(np.amax(matrixCountry) + 1)

def checkBorder(i, j, currCountry):
	if currCountry != matrixCountry[i + 1][j]:
		return True
	elif currCountry != matrixCountry[i - 1][j]:
		return True
	elif currCountry != matrixCountry[i][j + 1]:
		return True
	elif currCountry != matrixCountry[i][j - 1]:
		return True
	return False

cellsByCountry = np.zeros(np.amax(matrixCountry) + 1)

for i in range(dimensions[0]):
	for j in range(dimensions[1]):
		if i == 0 or i == dimensions[0] - 1 or j == 0 or j == dimensions[1] - 1:
			cellsByCountry[matrixCountry[i][j]] += 1
		else:
			if checkBorder(i, j, matrixCountry[i][j]):
				cellsByCountry[matrixCountry[i][j]] += 1

for num in list(map(lambda x: int(x) ,cellsByCountry.tolist())):
	print(num)
