import numpy as np
import math
from sys import argv
import matplotlib.pyplot as plt

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
	if currCountry != matrixCountry[i + 1][j] or currCountry != matrixCountry[i - 1][j] or currCountry != matrixCountry[i][j + 1] or currCountry != matrixCountry[i][j - 1]:
		return True
	return False

countryCount = np.amax(matrixCountry) + 1


# cellsByCountry = np.zeros(np.amax(matrixCountry) + 1)

# for i in range(dimensions[0]):
# 	for j in range(dimensions[1]):
# 		if i == 0 or i == dimensions[0] - 1 or j == 0 or j == dimensions[1] - 1:
# 			cellsByCountry[matrixCountry[i][j]] += 1
# 		else:
# 			if checkBorder(i, j, matrixCountry[i][j]):
# 				cellsByCountry[matrixCountry[i][j]] += 1

sums = np.zeros((countryCount, 3))

for i in range(dimensions[0]):
	for j in range(dimensions[1]):
		sums[matrixCountry[i][j]][0] += i
		sums[matrixCountry[i][j]][1] += j
		sums[matrixCountry[i][j]][2] += 1

capitalLocatoins = np.zeros((countryCount, 2), dtype=np.int64)

for i in range(countryCount):
	capitalLocatoins[i][0] = math.floor(sums[i][0] / sums[i][2])
	capitalLocatoins[i][1] = math.floor(sums[i][1] / sums[i][2])

cells = np.empty(countryCount, dtype=object)
cells.fill(np.empty((0, 2), dtype=object))

for i in range(dimensions[0]):
	for j in range(dimensions[1]):
		if i == 0 or i == dimensions[0] - 1 or j == 0 or j == dimensions[1] - 1:
			continue
		if not checkBorder(i, j, matrixCountry[i][j]): cells[matrixCountry[i][j]] = np.vstack((cells[matrixCountry[i][j]], [i, j]))

for i in range(countryCount):
	capital = capitalLocatoins[i]
	if not checkBorder(capital[0], capital[1], i) and matrixCountry[capital[0]][capital[1]] == i:
		continue
	euclidean = [math.sqrt(abs(capital[0] - cell[0])**2 + abs(capital[1] - cell[1])**2) for cell in cells[i]]
	capitalLocatoins[i] = cells[i][euclidean.index(min(euclidean))]

# for cell in cells[1]:
# 	matrixCountry[cell[0]][cell[1]] = 10

# plt.imshow(matrixCountry)
# plt.colorbar()
# plt.show()

for capital in capitalLocatoins:
	print(capital[1], capital[0])
