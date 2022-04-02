from collections import deque


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n+1)
count_list = [0] * (n + 1)
count = 0
answer = []
print(count_list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)


def solution(n):
    q = deque()
    q.append((n, 0))

    while q:
        print(q)
        num, count = q.popleft()
        for g in graph[num]:
            if visit[g] == 0:
                q.append((g, count + 1))
                visit[g] = 1
                count_list[g] = count + 1


solution(x)
for i in range(n+1):
    if count_list[i] == k:
        answer.append(i)
print(count_list)
print(answer)

answer.sort()
for a in answer:
    print(a)
