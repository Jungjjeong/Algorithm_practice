from collections import deque
from copy import deepcopy


n, m = map(int, input().split(' '))
field = []
cctv = []
q = deque()
min_answer = 64

for i in range(n):
	f_list = list(map(int, input().split(' ')))
	field.append(f_list)
	for j in range(m):
		if 0 < f_list[j] < 6:
			cctv.append((i, j, field[i][j]))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
print(cctv)

def bfs_solution(y, x):
	global copy_field

	sq = deque()
	sq.append((y, x))
	copy_field[y][x] = 8 # 백색공간
	count  = 1

	while sq:
		y, x = sq.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < n and 0<= nx < m and copy_field[ny][nx] == 0:
				sq.append((ny, nx))
				copy_field[ny][nx] = 8
				count += 1

	return count

def bfs():
	global copy_field, q

	while q:
		y, x, i = q.popleft()
		copy_field[y][x] = 9

		ny = y + dy[i]
		nx = x + dx[i]

		if 0 <= ny < n and 0 <= nx < m and copy_field[ny][nx] != 6:
			q.append((ny, nx, i))
		

copy_field = deepcopy(field)

for i in range(4):
	for c in cctv:
		if c[2] == 1:
			q.append((c[0], c[1], i))
		elif c[2] == 2:
			q.append((c[0], c[1], i))
			q.append((c[0], c[1], i - 2))
		elif c[2] == 3:
			q.append((c[0], c[1], i))
			q.append((c[0], c[1], i - 1))
		elif c[2] == 4:
			q.append((c[0], c[1], i))
			q.append((c[0], c[1], i - 1))
			q.append((c[0], c[1], i - 2))
		elif c[2] == 5:
			q.append((c[0], c[1], i))
			q.append((c[0], c[1], i - 1))
			q.append((c[0], c[1], i - 2))
			q.append((c[0], c[1], i - 3))

	bfs()
	for h in range(n):
		for w in range(m):
			if copy_field[h][w] == 0:
				count = bfs_solution(h, w)
				if min_answer > count:
					min_answer = count

	print(copy_field)
	print(min_answer if min_answer != 64 else 0)
	copy_field = deepcopy(field)
