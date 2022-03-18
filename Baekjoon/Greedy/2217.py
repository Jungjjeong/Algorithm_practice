from audioop import reverse
import sys
input = sys.stdin.readline

n = int(input())
rope = []
answer = []

for _ in range(n):
	rope.append(int(input()))

rope.sort(reverse = True)

for i in range(n):
	answer.append(rope[i] * (i+1))

print(max(answer))