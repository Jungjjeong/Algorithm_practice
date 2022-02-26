n = int(input())
p1, p2 = map(int, input().split(' '))

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(int(input())):
	u, v = map(int, input().split(' '))
	graph[u].append(v)
	graph[v].append(u)


def dfs(node):
	for i in graph[node]:
		if visit[i] == 0:
			visit[i] = visit[node] + 1
			dfs(i)

dfs(p1)
print(visit[p2] if visit[p2] > 0 else -1)