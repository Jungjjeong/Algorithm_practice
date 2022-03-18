import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	r_list = []
	answer = 1
	
	for i in range(n):
		d, i = map(int, input().split())
		r_list.append([d,i])

	r_list = sorted(r_list, key = lambda x : x[0])
	r_best = r_list[0][1]
	
	for i in range(1, n):
		# 순위가 더 높으면!
		if r_best > r_list[i][1]:
			r_best = r_list[i][1]
			answer += 1

	print(answer)