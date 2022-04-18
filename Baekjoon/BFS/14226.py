from collections import deque
import sys
input = sys.stdin.readline

s = int(input())
time = [[-1 for _ in range(s + 1)] for _ in range(s + 1)]


def solution(num):
    q = deque()
    q.append((num, 0))

    while q:
        num, clip = q.popleft()

        if num == s:
            print(time[num][clip])
            break

        dx = [clip, 0, -1]

        for i in range(3):
            n_num = num + dx[i]

            if 0 <= n_num < s + 1:
                if i == 1 and time[n_num][num] == -1:
                    time[n_num][num] = time[n_num][clip] + 1
                    q.append((n_num, num))
                elif i != 1 and time[n_num][clip] == -1:
                    time[n_num][clip] = time[num][clip] + 1
                    q.append((n_num, clip))


solution(1)
