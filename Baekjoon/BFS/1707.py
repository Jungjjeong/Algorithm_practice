from collections import deque
import sys
input = lambda: sys.stdin.readline()

def bfs(i, c):
	q = deque()
	q.append(i)
	visit[i] = True
	color[i] = c

	while q:
		i = q.popleft()
		for g in graph[i]:
			if not visit[g]:
				visit[g] = True
				q.append(g)
				color[g] = 3- color[i]
			else:
				if color[i] == color[g]:
					return False
	return True


k = int(input())

for _ in range(k): 
	v,e = map(int, input().split())
	color = [0] * (v+1)
	graph = [[] for _ in range(v+1)]

	for _ in range(e):
		a,b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
	
	answer = True
	visit = [False] * (v+1)

	for i in range(1, v+1):
		if not visit[i]:
			if not bfs(i, 1):
				answer = False
				break

	print('YES' if answer else 'NO')