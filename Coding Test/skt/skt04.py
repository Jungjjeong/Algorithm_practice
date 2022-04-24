from collections import deque


answer = 0

def bfs(root, num, graph, visit):

	q = deque()
	q.append((root, 0))
	visit[root] = 1

	while q:
		r, c = q.popleft()

		if r == num:
			return c

		for g in graph[r]:
			if visit[g] == 0:
				visit[g] = 1
				q.append((g, c+1))


def solution(n, edges):
	global count, answer

	graph = [[] for _ in range(n)]
	visit = [0] * n

	for e in edges:
		graph[e[0]].append(e[1])
		graph[e[1]].append(e[0])


	for i in range(n):
		for j in range(n):
			for k in range(n):
				if i != j and j != k and i != k:
					i_to_j = bfs(i, j, graph, visit)
					visit = [0] * n
					count = 0
					if i_to_j == None:
						break

					j_to_k = bfs(j, k, graph, visit)
					visit = [0] * n
					count = 0
					if j_to_k == None:
						break
					
					i_to_k = bfs(i, k, graph, visit)
					visit = [0] * n
					count = 0
					if i_to_k == None:
						break

					if i_to_j + j_to_k == i_to_k:
						answer += 1

                    
	return answer


print(solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]]))