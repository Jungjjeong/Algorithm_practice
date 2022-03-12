from collections import deque


dy = [0, 0, -1, 1, 1, -1]
dx = [-1, 1, 0, 0, 1, -1] # 4방향 + 대각선의 경우 고려
count = 0


def solution(width, height, diagonals):
	field = [[[0] * 2 for _ in range(width + 1)] for _ in range(height + 1)]
	answer = 0

	def bfs(y, x, c):
		global count
		q = deque()
		q.append((y, x, c))
		field[y][x][c] = 1

		while q:
			print(q)
			y, x, c = q.popleft()

			if y == 0 and x == width and c == 1:
				count += 1

			for d in diagonals:
				if y == height - d[1] and x == d[0] - 1:
					print('들어옴')
					ny = y + dy[4]
					nx = x + dx[4]
				elif y == height - d[1] + 1 and x == d[0]:
					print('들어옴2')
					ny = y + dy[5]
					nx = x + dx[5]
				else:
					break
				
				if c == 0 and field[ny][nx][1] == 0:
					print('--',ny, nx)
					if 0 <= ny < (height + 1) and 0 <= nx < (width + 1):
						q.append((ny, nx, 1))
						field[ny][nx][1] = field[y][x][c] + 1

			for i in range(4):
				ny = y + dy[i]
				nx = x + dx[i]
				print(ny, nx)
				if 0 <= ny < (height + 1) and 0 <= nx < (width + 1) and field[ny][nx][c] == 0:
					q.append((ny, nx, c))
					field[ny][nx][c] = field[y][x][c] + 1

	bfs(height, width, 0)
	print(field)

	print(field[0][width][0], field[0][width][1], count)
	return answer



solution(2, 2, [[1, 1], [2, 2]])