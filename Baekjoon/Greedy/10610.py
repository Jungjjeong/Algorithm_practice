n_list = list(map(int, input()))
n_list.sort(reverse=True)

sum_num = sum(n_list)

string = ''

if (n_list[-1] == 0) and sum_num % 3 == 0:
	for n in n_list:
		string += str(n)
	print(string)
else:
	print(-1)