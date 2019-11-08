import numpy as np
import math
from sys import argv

matrix = None

with open(argv[1], 'r') as f:
	matrix = [[int(num) for num in line.split(' ')] for line in f]

dimensions = matrix.pop(0)

print('{} {} {}'.format(np.amin(matrix), np.amax(matrix), math.floor(np.mean(matrix))))
