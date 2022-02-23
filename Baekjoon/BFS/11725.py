import sys


input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
visit = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)


def solution(index):
    for g in graph[index]:
        if visit[g] == 0:
            parent[g] = index
            visit[g] = 1
            solution(g)

visit[1] = 1
solution(1)

for i in range(2, n+1):
    print(parent[i])
