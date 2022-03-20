string = str(input())

count_0 = 0
count_1 = 0

if string[0] == '0':
	count_0 += 1
elif string[0] == '1':
	count_1 += 1

for i in range(1, len(string)):
	if string[i-1] != string[i]:
		if string[i] == '0':
			count_0 += 1
		elif string[i] == '1':
			count_1 += 1

print(min(count_0, count_1))