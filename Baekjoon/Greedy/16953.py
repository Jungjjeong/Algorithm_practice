a, b = map(str, input().split())

count = 1

while True:
	if int(a) == int(b):
		print(count)
		break
	elif int(a) > int(b):
		print(-1)
		break

	if b[-1] == '0' or int(b) % 2 == 0:
		b = str(int(b) // 2)
	elif b[-1] == '1':
		b = b[:-1]
	else:
		print(-1)
		break

	count += 1