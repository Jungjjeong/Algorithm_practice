from collections import deque
from copy import deepcopy


h, w = map(int, input().split(' '))

field = []
max_distance = 0

for _ in range(h):
	field.append(list(map(str, input())))


distance = [[0 for _ in range(w)] for _ in range(h)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def solution(y, x):
	global dy, dx, c_distance, max_distance

	q = deque()
	q.append((y, x))
	c_distance[y][x] = 1
	
	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < h and 0<= nx < w and field[ny][nx] == 'L' and c_distance[ny][nx] == 0:
				q.append((ny, nx))
				c_distance[ny][nx] = c_distance[y][x] + 1

				if c_distance[ny][nx] > max_distance:
					max_distance = c_distance[ny][nx]


for i in range(h):
	for j in range(w):
		if field[i][j] == 'L':
			c_distance = deepcopy(distance)
			solution(i, j)

print(max_distance - 1)