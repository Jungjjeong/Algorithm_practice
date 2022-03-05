k = int(input())

def dfs(index):
	for g in graph[index]:
		if visit[g] == 0:
			visit[g] = 1

			if color[g] == color[index]:
				print(g, index)
				print(color)
				return False

			if color[index] == -1:
				color[g] = 1
			elif color[index] == 1:
				color[g] = -1

			if dfs(g) == False:
				return False
			
			visit[g] = 0




for _ in range(k):
	v, e = map(int, input().split(' '))

	graph = [[] for _ in range(v+1)]
	visit = [0] * (v+1)
	color = [0] * (v+1)

	for _ in range(e):
		a,b = map(int, input().split(' '))
		graph[a].append(b)
		graph[b].append(a)

	print(graph)

	for i in range(1, v+1):
		if color[i] == 0:
			print(i)
			visit[i] = 1
			color[i] = -1
			if dfs(i) == False:
				print('NO')
				quit(0)

	print('Yes')
