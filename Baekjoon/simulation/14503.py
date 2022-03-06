from collections import deque


n, m = map(int, input().split(' '))
r,c, d = map(int, input().split(' '))
answer = 0

field = []
for _ in range(n):
	field.append(list(map(int, input().split(' '))))


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1] # 북동남서

def solution(y, x, d):
	global answer

	q = deque()
	q.append((y, x, d))
	field[y][x] = 2 # 청소
	answer += 1

	while q:
		y, x, d = q.popleft()
		count = 0

		if d <= 0:
			d += 4

		for i in range(d-1, d-5 ,-1):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < m and 0 <= ny < n and field[ny][nx] == 0:
				q.append((ny, nx, i))
				field[ny][nx] = 2
				count += 1
				answer += 1
				break
		
		if count == 0:
			# 네칸이 모두 벽이거나 청소가 되어서 이동 못하는 경우, 한칸 후진 
			if 0 <= y + dy[d-2] < n and 0<= x + dx[d-2] < m and field[y + dy[d-2]][x + dx[d-2]] != 1:
				if field[y + dy[d-2]][x + dx[d-2]] == 0:
					count += 1
					field[y + dy[d-2]][x + dx[d-2]] = 2
				q.append((y + dy[d-2], x + dx[d-2], d))
			else:
				break

solution(r, c, d)

print(answer)