count = 1

while True:
	answer = 0
	l, p, v = map(int, input().split())

	if l == p == v == 0:
		break

	answer += l * (v // p)
	if v % p > l:
		answer += l
	else:
		answer += v % p
	
	print("Case %d: %d"%(count,answer))
	count += 1
		