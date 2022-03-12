from collections import deque
from copy import deepcopy


n, m = map(int, input().split(' '))
field = []
cctv = []

for i in range(n):
	f_list = list(map(int, input().split(' ')))
	field.append(f_list)
	for j in range(m):
		if 0 < f_list[j] < 6:
			cctv.append((i, j, field[i][j]))

