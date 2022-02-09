from collections import deque


n, k = map(int, input().split(' '))
MAX = 100000
visited_list = [0] * (MAX + 1)

count = 0


def solution(n):
    global count
    direction = [1, -1]

    q = deque()
    q.append(n)

    while q:
        num = q.popleft()

        if num == k:
            print(visited_list[num])
            break

        for i in range(3):
            if i == 0 or i == 1:
                nnum = num + direction[i]
            else:
                nnum = num * 2

            if 0 <= nnum <= MAX and visited_list[nnum] == 0:
                q.append(nnum)
                visited_list[nnum] = visited_list[num] + 1


solution(n)
