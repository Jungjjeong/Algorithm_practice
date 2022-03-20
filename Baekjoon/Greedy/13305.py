n = int(input())
road = list(map(int, input().split(' ')))
oil = list(map(int, input().split(' ')))

cur_oil = oil[0]
sum_val = road[0] * oil[0] 

for i in range(1, n-1):
	if oil[i] < cur_oil:
		cur_oil = oil[i]
	
	sum_val += road[i] * cur_oil

print(sum_val)