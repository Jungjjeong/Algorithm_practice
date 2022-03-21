n, l = map(int, input().split())
water = list(map(int, input().split()))
water_list = [0] * 1001
count = 0

for w in water:
	water_list[w] = 1 # 물이 새요

water.sort()

for w in water:
	if water_list[w] == 1:
		for i in range(w, w+l):
			if i > 1000:
				break
			water_list[i] = 0 # 막아
		count += 1
	else:
		pass

print(count)
