from copy import deepcopy
from collections import deque
from operator import truediv

n, m = map(int, input().split(' '))
graph = []
time = 0
last_cheese = 0

for _ in range(n):
    graph.append(list(map(int, input().split(' '))))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
copy_graph = deepcopy(graph)


def solution(y, x):
    global last_cheese

    q = deque()
    q.append((y, x))
    visit_graph[y][x] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n or visit_graph[ny][nx] == 1:
                continue
            else:
                if graph[ny][nx] == 1:
                    last_cheese += 1
                    copy_graph[ny][nx] = 0
                elif graph[ny][nx] == 0:
                    q.append((ny, nx))

                visit_graph[ny][nx] = 1


def isEmpty():
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 1:
                return True

    return False


while True:
    time += 1
    visit_graph = [[0 for _ in range(m)] for _ in range(n)]
    solution(0, 0)

    if isEmpty() == False:
        break

    graph = deepcopy(copy_graph)
    last_cheese = 0

print(time)
print(last_cheese)
