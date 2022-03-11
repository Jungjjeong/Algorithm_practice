n, m = map(int, input().split(' '))

graph = [[] for _ in range(n)]
visit = [0] * n
isTrue = False

for _ in range(m):
	a, b = map(int, input().split(' '))
	graph[a].append(b)
	graph[b].append(a)


def dfs(num):
	global count, isTrue

	if count >= 4:
		isTrue = True
		return

	for g in graph[num]:
		if visit[g] == 0:
			count += 1
			visit[g] = 1
			dfs(g)
			count -= 1
			visit[g] = 0

for p in range(n):
	visit = [0] * n
	visit[p] = 1
	count = 0
	dfs(p)

	if isTrue == True:
		print(1)
		quit(0)

print(0)
