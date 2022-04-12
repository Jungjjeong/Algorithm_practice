from collections import deque
import sys

input = sys.stdin.readline


n, k = map(int, input().split(' '))
MAX = 100001
visited_list = [0] * (MAX + 1)

min_time = 0
count = 0
direction = [1, -1]

if n == k:
    print(0)
    print(1)
    quit(0)


def bfs(n):
    global min_time, direction, count

    q = deque()
    q.append(n)

    while q:
        num = q.popleft()

        if num == k:
            min_time = visited_list[num]
            count += 1

        for i in range(3):
            if i == 0 or i == 1:
                nnum = num + direction[i]
            else:
                nnum = num * 2

            if 0 <= nnum <= MAX:
                if visited_list[nnum] == 0 or visited_list[nnum] >= visited_list[num] + 1:
                    q.append(nnum)
                    visited_list[nnum] = visited_list[num] + 1


bfs(n)
print(min_time)
print(count)
