from collections import deque

N, L, R = map(int, input().split(' '))
field = []
answer = 0

for i in range(N):
	field.append(list(map(int, input().split(' '))))


def open(answer):
	f_val = answer[1] // answer[0]

	for i in range(N):
		for j in range(N):
			if visit[i][j] == 1:
				field[i][j] = f_val



def solution(ry, rx):
	dy = [0,0,-1,1]
	dx = [-1,1,0,0]

	q = deque()
	q.append((ry, rx))
	temp = []
	temp.append((ry, rx))
	visit[ry][rx] = 1

	while q:
		y, x = q.popleft()
		val = field[y][x]

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
				if L <= abs(field[ny][nx] - val) <= R:
					q.append((ny, nx))
					temp.append((ny, nx))
					visit[ny][nx] = 1
	
	return temp
		

while True:
	visit = [[0 for _ in range(N)] for _ in range(N)]
	isTrue = False

	for i in range(N):
		for j in range(N):
			if visit[i][j] == 0:
				temp = solution(i,j)
				
				if len(temp) > 1:
					isTrue = True
					num = sum([field[y][x] for y,x in temp]) // len(temp)
					for y, x in temp:
						field[y][x] = num
	
	if not isTrue:
		break
	answer += 1

print(answer)