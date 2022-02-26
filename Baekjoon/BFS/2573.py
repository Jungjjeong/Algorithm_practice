from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split(' '))
ice_field = []
ice_reduce = [[0 for _ in range(m)] for _ in range(n)]
answer = 0

for _ in range(n):
	ice_field.append(list(map(int, sys.stdin.readline().split(' '))))

dy = [0,0,-1,1]
dx = [-1,1,0,0]

# 주변 4방향 검사해서 줄어들 수 반환
def count_reduce(y, x):
	global dy, dx
	reduce_count = 0

	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if ice_field[ny][nx] == 0 and 0<= ny < n and 0<= nx < m:
			reduce_count += 1

	return reduce_count


# 전체 맵에서 연결된 요소 몇구역인지 BFS
def solution(y, x):
	global dy, dx

	q = deque()
	q.append((y, x))
	visit[y][x] = 1

	while q:
		y, x = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0 and ice_field[ny][nx] > 0:
				q.append((ny, nx))
				visit[ny][nx] = 1



while True:
	count = 0
	visit = [[0 for _ in range(m)] for _ in range(n)]

	for i in range(n):
		for j in range(m):
			if ice_field[i][j] > 0 and visit[i][j] == 0:
				solution(i, j)
				count += 1

	if count >= 2:
		print(answer)
		break
	elif count == 0:
		print(0)
		break

	for i in range(n):
		for j in range(m):
			if ice_field[i][j] > 0:
				ice_reduce[i][j] = count_reduce(i, j)


	for i in range(n):
		for j in range(m):
			ice_field[i][j] -= ice_reduce[i][j]
			if ice_field[i][j] < 0:
				ice_field[i][j] = 0

	answer += 1