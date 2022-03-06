from collections import deque

n, m, y, x, k = map(int, input().split())
field = []
for _ in range(n):
	field.append(list(map(int, input().split())))

k_list = list(map(int, input().split()))

dice = [0] * 7 # 1부터 6까지, 1, 2, 3, 4, 5, 6

dy = [0, 0, 0, -1, 1] # 1 동, 2 서, 3 북, 4 남
dx = [0, 1, -1, 0, 0]

def dice_move(k): 
	# 항상 dice[1]을 값을 바꾸는 곳으로 만들어준다.
	# dice[6]은 항상 윗면이니까 프린트하면 되겠지.
	if k == 1 : # 동쪽
		dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
	elif k == 2: # 서쪽
		dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
	elif k == 3: # 북쪽
		dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]
	elif k == 4: # 남쪽
		dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]

def field_move(y, x):
	q = deque()
	q.append((y, x))

	for i in k_list:
		y, x = q.popleft()

		ny = y + dy[i]
		nx = x + dx[i]

		if 0 <= ny < n and 0 <= nx < m:
			q.append((ny, nx))
			dice_move(i)

			if field[ny][nx] > 0:
				dice[1] = field[ny][nx]
				field[ny][nx] = 0
			elif field[ny][nx] == 0:
				field[ny][nx] = dice[1]

			print(dice[6])
		else:
			# 해당 명령을 무시하고 다시 q에 qppend
			q.append((y, x))
	
field_move(y, x)

