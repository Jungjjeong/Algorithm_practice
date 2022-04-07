import heapq
import sys

input = sys.stdin.readline

min_heap = []
n = int(input())

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap)[1])
    else:
        heapq.heappush(min_heap, (abs(num), num))
