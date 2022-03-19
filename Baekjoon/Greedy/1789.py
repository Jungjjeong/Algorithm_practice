s = int(input())
n = 1
count = 0

while s >= 0:
	s -= n
	n += 1
	count += 1


print(count - 1)