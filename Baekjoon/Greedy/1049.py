n, m = map(int, input().split())

min_pack = 1000
min_one = 1000
price = 0

for _ in range(m):
	p, o = map(int, input().split())
	if min_pack > p:
		min_pack = p
	if min_one > o:
		min_one = o


price += min_pack * (n // 6)
if min_one * (n % 6) < min_pack:
	price += min_one * (n % 6)
else:
	price += min_pack

print(price if price < min_one * n else min_one * n)