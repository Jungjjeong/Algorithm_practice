from collections import deque


r, c = map(int, input().split(' '))
map_list = []

for _ in range(r):
	map_list.append(list(map(str, input())))


move = [[0 for _ in range(c)] for _ in range(r)]
destination_x = 0
destination_y = 0
dy = [0,0,-1,1]
dx = [-1,1,0,0]
water_q = deque()
S_q = deque()


def water_bfs():
	global dy, dx, water_len

	while water_len > 0:
		y, x = water_q.popleft()
		water_len -= 1
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0<= ny < r and 0 <= nx < c:
				if map_list[ny][nx] == '.':
					water_q.append((ny, nx))
					map_list[ny][nx] = '*'
					
		water_len -= 1


def bfs():
	global dy, dx, S_len
	count = 0

	while S_len > 0:
		y, x = S_q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0<= ny < r and 0<= nx < c:
				if map_list[ny][nx] == '.':
					S_q.append((ny, nx))
					map_list[ny][nx] = 'S'
					move[ny][nx] = move[y][x] + 1
					count += 1
				elif map_list[ny][nx] == 'D':
					move[ny][nx] = move[y][x] + 1
					count += 1
					return True

		S_len -= 1
	if count == 0:
		print('KAKTUS')
		quit(0)

while True:
	for i in range(r):
		for j in range(c):
			if map_list[i][j] == 'S':
				S_q.append((i, j))
			elif map_list[i][j] == '*':
				water_q.append((i,j))
			elif map_list[i][j] == 'D':
				destination_x = j
				destination_y = i

	S_len = len(S_q)
	water_len = len(water_q)

	water_bfs()

	if bfs() == True:
		print(move[destination_y][destination_x])
		break

