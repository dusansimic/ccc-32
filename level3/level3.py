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
	if currCountry != matrixCountry[i + 1][j]:
		return True
	elif currCountry != matrixCountry[i - 1][j]:
		return True
	elif currCountry != matrixCountry[i][j + 1]:
		return True
	elif currCountry != matrixCountry[i][j - 1]:
		return True
	return False

# cellsByCountry = np.zeros(np.amax(matrixCountry) + 1)

countryCount = np.amax(matrixCountry) + 1

sums = np.zeros((countryCount, 3))

# for i in range(dimensions[0]):
# 	for j in range(dimensions[1]):
# 		if i == 0 or i == dimensions[0] - 1 or j == 0 or j == dimensions[1] - 1:
# 			cellsByCountry[matrixCountry[i][j]] += 1
# 		else:
# 			if checkBorder(i, j, matrixCountry[i][j]):
# 				cellsByCountry[matrixCountry[i][j]] += 1

for i in range(dimensions[0]):
	for j in range(dimensions[1]):
		sums[matrixCountry[i][j]][0] += i
		sums[matrixCountry[i][j]][1] += j
		sums[matrixCountry[i][j]][2] += 1

capitalLocatoins = np.zeros((countryCount, 2))

for i in range(countryCount):
	capitalLocatoins[i][0] = math.floor(sums[i][0] / sums[i][2])
	capitalLocatoins[i][1] = math.floor(sums[i][1] / sums[i][2])

# print(capitalLocatoins)

for i in range(countryCount):
	capital = capitalLocatoins[i]
	capital = capital.astype(np.int64)
	if not checkBorder(capital[0], capital[1], i) and i == matrixCountry[capital[0]][capital[1]]:
		continue
	elif capital[0] - 1 >= 0 and not checkBorder(capital[0] - 1, capital[1], i) and i == matrixCountry[capital[0] - 1][capital[1]]:
		capital[0] -= 1
		capitalLocatoins[i] = capital
		continue
	elif capital[0] + 1 < dimensions[0] and not checkBorder(capital[0] + 1, capital[1], i) and i == matrixCountry[capital[0] + 1][capital[1]]:
		capital[0] += 1
		capitalLocatoins[i] = capital
		continue
	elif capital[1] - 1 >= 0 and not checkBorder(capital[0], capital[1] - 1, i) and i == matrixCountry[capital[0]][capital[1] - 1]:
		capital[1] -= 1
		capitalLocatoins[i] = capital
		continue
	elif capital[1] + 1 < dimensions[1] and not checkBorder(capital[0], capital[1] + 1, i) and i == matrixCountry[capital[0]][capital[1] + 1]:
		capital[1] += 1
		capitalLocatoins[i] = capital
		continue
	found = False
	x = capital[0]
	y = capital[1]
	moveI = 1
	moveJ = 1
	xOrY = True
	while not found:
		if xOrY:
			xTempLow = x - moveI
			xTempHigh = x + moveI + 1

			if xTempLow < 0: xTempLow = 0
			if xTempHigh > dimensions[0] - 1: xTempHigh = dimensions[0] - 1

			for i1 in range(x, xTempLow, -1):
				yTempLow = y - moveJ
				yTempHigh = y + moveJ

				if yTempLow < 0: yTempLow = 0
				if yTempHigh > dimensions[1] - 1: yTempHigh = dimensions[0] - 1

				if not checkBorder(i1, yTempHigh, i) and matrixCountry[i1][yTempHigh] == i:
					found = True
					capital[0] = i1
					capital[1] = yTempHigh
				elif not checkBorder(i1, yTempLow, i) and matrixCountry[i1][yTempLow] == i:
					found = True
					capital[0] = i1
					capital[1] = yTempLow
			for i1 in range(x, xTempHigh):
				yTempLow = y - moveJ
				yTempHigh = y + moveJ

				if yTempLow < 0: yTempLow = 0
				if yTempHigh > dimensions[1] - 1: yTempHigh = dimensions[0] - 1

				if not checkBorder(i1, yTempHigh, i) and matrixCountry[i1][yTempHigh] == i:
					found = True
					capital[0] = i1
					capital[1] = yTempHigh
				elif not checkBorder(i1, yTempLow, i) and matrixCountry[i1][yTempLow] == i:
					found = True
					capital[0] = i1
					capital[1] = yTempLow
		else:
			yTempLow = y - moveJ + 1
			yTempHigh = y + moveJ

			if yTempLow < 0: yTempLow = 0
			if yTempHigh > dimensions[1] - 1: yTempHigh = dimensions[0] - 1

			for j1 in range(y, yTempLow, -1):
				xTempLow = x - moveI
				xTempHigh = x + moveI

				if xTempLow < 0: xTempLow = 0
				if xTempHigh > dimensions[0] - 1: xTempHigh = dimensions[0] - 1

				if not checkBorder(xTempHigh, j1, i) and matrixCountry[xTempHigh][j1] == i:
					found = True
					capital[0] = xTempHigh
					capital[1] = j1
				elif not checkBorder(xTempLow, j1, i) and matrixCountry[xTempLow][j1] == i:
					found = True
					capital[0] = xTempLow
					capital[1] = j1
			for j1 in range(y, yTempHigh):
				xTempLow = x - moveI
				xTempHigh = x + moveI

				if xTempLow < 0: xTempLow = 0
				if xTempHigh > dimensions[0] - 1: xTempHigh = dimensions[0] - 1

				if not checkBorder(xTempHigh, j1, i) and matrixCountry[xTempHigh][j1] == i:
					found = True
					capital[0] = xTempHigh
					capital[1] = j1
				elif not checkBorder(xTempLow, j1, i) and matrixCountry[xTempLow][j1] == i:
					found = True
					capital[0] = xTempLow
					capital[1] = j1
		xOrY = not xOrY
		moveI += 1
		moveJ += 1
	capitalLocatoins[i] = capital
	# print(capital)

print(capitalLocatoins)

# print('\n'.join([''.join(['{:1} '.format(int(item)) for item in row]) for row in capitalLocatoins]))

# print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in matrixCountry]))
plt.imshow(matrixCountry)
plt.colorbar()
plt.show()

# for num in list(map(lambda x: int(x) ,cellsByCountry.tolist())):
# 	print(num)
