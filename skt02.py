def conversion(num, first, last, answer, clockwise, n):
	answer[first][first] = num
	answer[first][last] = num
	answer[last][last] = num
	answer[last][first] = num

	middle = []
	for i in range(num + 1, ((num+1)+(last-first-2)) + 1):
		middle.append(i)

	print('---',middle)

	if len(middle) == 0:
		return
		
	start = middle[-1] + 1

	if clockwise == False:
		middle.reverse()

	idx_arr = []
	for i in range(first+1, last):
		idx_arr.append(i)
	print('-',idx_arr)

	for idx, a in enumerate(idx_arr):
		reverse_i = n-a-1
		# 위쪽
		answer[first][a] = middle[idx]
		# 오른쪽
		answer[a][last] = middle[idx]
		# 아래쪽
		answer[last][reverse_i] = middle[idx]
		# 왼쪽
		answer[reverse_i][first] = middle[idx]

	print(answer)
	conversion(start, first+1, last-1, answer, clockwise, n)



def solution(n, clockwise):
	answer = [[0 for _ in range(n)] for _ in range(n)]
	num = 1
	first = 0
	last = n-1

	conversion(num, first, last, answer, clockwise, n)

	return answer

# print(solution(6, False))