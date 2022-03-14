h, w = map(int, input().split())
world = list(map(int, input().split()))

answer = 0

for i in range(1, w - 1):
	left_max = max(world[:i])
	right_max = max(world[i+1:])

	min_height = min(left_max, right_max)

	if world[i] < min_height:
		answer += min_height - world[i]

print(answer)