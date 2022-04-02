from collections import deque


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n+1)
count_list = [0] * (n + 1)
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def solution(n):
    q = deque()
    q.append((n, 0))
    visit[n] = 1

    while q:
        num, count = q.popleft()

        if count == k:
            answer.append(num)

        for g in graph[num]:
            if visit[g] == 0:
                q.append((g, count + 1))
                visit[g] = 1
                count_list[g] = count + 1


solution(x)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)
