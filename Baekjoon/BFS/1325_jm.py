import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
n, m = map(int, input().split(' '))

graph = [[] for _ in range(n + 1)]
visit = [0] * (n+1)
answer = [0] * (n+1)

for _ in range(m):
	a, b = map(int, input().split(' '))
	graph[b].append(a)

cnt = 0
def dfs(node):
	global cnt

	cnt += 1
	for n in graph[node]:
		if visit[n] != 1:
			visit[n] = 1
			dfs(n)

m = 0 
for node in range(1,n+1):
	visit = [0] * (n+1)
	cnt = 0
	dfs(node)
	if cnt > m :
		m = cnt
	answer[node] = cnt

for node in range(1,n+1):
	if answer[node] == m:
		print(node, end=' ')
