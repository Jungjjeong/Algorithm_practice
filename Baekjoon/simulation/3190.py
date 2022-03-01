from collections import deque


n = int(input())
field = [[0 for _ in range(n)] for _ in range(n)]
snake_dirc = []


for i in range(int(input())):
	c, r = map(int, input().split(' '))
	field[c-1][r-1] = 2 # apple이 있어요
# 사과를 먹으면 몸길이가 하나씩 늘어나요


for i in range(int(input())):
	snake_dirc.append(list(map(str, input().split(' '))))


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0] # -> 방향은 오른쪽, <- 방향은 왼쪽
snake_list = []
count = 0 # 진행한 초

def bfs(y, x):
	global dy, dx
	global snake_list, count

	q = deque()
	q.append((y, x))
	field[y][x] = 1 # 뱀의 초기 위치, 몸길이는 0
	dirc = 0 # 움직여야 하는 방향
	snake_list.append((y, x))

	while q:
		y, x = q.popleft()

		# 방향 전환 조건에 도달
		for s in snake_dirc:
			if count == int(s[0]):
				if s[1] == 'D':
					# dy, dx + 1해줌으로써 오른쪽으로 방향 전환
					dirc += 1
				elif s[1] == 'L':
					dirc -= 1
	
				if dirc == 4:
					dirc = 0
				elif dirc == -1:
					dirc = 3

		ny = y + dy[dirc]
		nx = x + dx[dirc]

		if ny < 0 or ny >= n or nx < 0 or nx >= n or field[ny][nx] == 1:
			# 벽에 부딫히거나 자신의 몸에 부딫혀 게임 종료
			break
		else:
			if field[ny][nx] == 0:
				ty, tx = snake_list[0]
				field[ty][tx] = 0 

				del snake_list[0]
				q.append((ny, nx))
				snake_list.append((ny, nx))

				field[ny][nx] = 1
			elif field[ny][nx] == 2:
				q.append((ny, nx))
				snake_list.append((ny, nx))
				field[ny][nx] = 1

		count += 1


bfs(0, 0)
print(count + 1)


	
