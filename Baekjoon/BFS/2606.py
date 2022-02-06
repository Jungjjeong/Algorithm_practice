from collections import deque


com_n = int(input())
lan_n = int(input())
network = [[0] * (com_n+1) for _ in range(com_n+1)]
check_list = [0] * (com_n + 1)

for _ in range(lan_n):
    a, b = map(int, input().split(' '))
    network[a][b] = network[b][a] = 1


def bfs(root):
    q = deque()
    q.append(root)
    check_list[root] = 1
    count = 0

    while q:
        node = q.popleft()
        for i in range(1, com_n + 1):
            if check_list[i] == 0 and network[node][i] == 1:
                q.append(i)
                check_list[i] = 1
                count += 1

    return count


print(bfs(1))
