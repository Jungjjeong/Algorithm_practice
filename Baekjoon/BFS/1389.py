from collections import deque


n, m = map(int, input().split(' '))

graph = [[] for _ in range(n + 1)]
visit = [0] * (n+1)
count = 0
answer_num = float('inf')
answer_per = 0

for _ in range(m):
	a, b = map(int, input().split(' '))
	graph[a].append(b)
	graph[b].append(a)


def bfs(num, destination):
	global count

	q = deque()
	q.append((num, count))

	while q:
		num, c = q.popleft()

		if num == destination:
			return c

		for g in graph[num]:
			q.append((g, c + 1))


temp_answer = 0

for i in range(1, n + 1):
	for n in range(1, n+1):
		if i != n:
			c = bfs(i, n)
			temp_answer += c
			count = 0

	if temp_answer < answer_num:
		answer_num = temp_answer
		answer_per = i

	temp_answer = 0

print(answer_per)