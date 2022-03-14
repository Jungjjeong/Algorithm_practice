from collections import deque


h, w = map(int, input().split(' '))
field = []
visit = [[0 for _ in range(w)] for _ in range(h)]
cheese = 0

for _ in range(h):
	f_list = list(map(int, input().split(' ')))
	for f in f_list:
		if f == 1:
			cheese += 1
	field.append(f_list)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def solution(y, x):
	q = deque()
	q.append((y, x))
	visit[y][x] = 1
	
	while q:
		y, x = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < h and 0<= nx < w and visit[ny][nx] == 0:
				if field[ny][nx] == 1:
					field[ny][nx] = 0
					visit[ny][nx] = 1
				elif field[ny][nx] == 0:
					q.append((ny, nx))
					visit[ny][nx] = 1

count = 0

if cheese == 0:
	print(0)
	print(cheese)
	quit(0)

while True:
	local_cheese = 0
	isTrue = False
	solution(0, 0)

	for i in range(h):
		for j in range(w):
			if field[i][j] == 1:
				isTrue = True
				local_cheese += 1

	count += 1
	
	if isTrue == False:
		print(count)
		print(cheese)
		break

	cheese = local_cheese
	visit = [[0 for _ in range(w)] for _ in range(h)]