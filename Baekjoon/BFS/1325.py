from collections import deque


n, m = map(int, input().split(' '))

graph = [[] for _ in range(n + 1)]
visit = [0] * (n+1)
answer = [0] * (n+1)
answer_per = []


for _ in range(m):
	a, b = map(int, input().split(' '))
	graph[b].append(a)


def solution(num):
	q = deque()
	q.append(num)
	visit[num] = 1
	count = 1

	while q:
		num = q.popleft()

		for g in graph[num]:
			if visit[g] == 0:
				q.append(g)
				count += 1
				visit[g] = 1

	
	return count

for num in range(1, n+1):
	answer[num] = solution(num)
	visit = [0] * (n+1)

for i in range(1, n+1):
	if answer[i] == max(answer):
		answer_per.append(i)

answer_per.sort()

print(*answer_per)