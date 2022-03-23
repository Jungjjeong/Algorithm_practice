n = int(input())
word = []
num = [''] * n
alpha_val = [0] * 26
alpha_num = 0
value = 9
answer = 0

for _ in range(n):
	w_list = list(map(str, input()))

	for i, w in enumerate(w_list):
		alpha_val[ord(w) - 65] += 10**(len(w_list)-i)

	word.append(w_list)

for a in range(len(alpha_val)):
	m = max(alpha_val)
	if m == 9:
		break
	i = alpha_val.index(m)

	alpha_val[i] = value
	value -= 1


for i in range(len(word)):
	for w in word[i]:
		num[i] += str(alpha_val[ord(w) - 65])
	answer += int(num[i])

print(answer)
