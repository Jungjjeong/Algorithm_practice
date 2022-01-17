from queue import PriorityQueue

num_q = PriorityQueue(maxsize=100000)

n = int(input())
for _ in range(n):
    num_q.put(int(input()))

result = 0

while num_q.qsize() > 1:
    num1 = num_q.get()
    num2 = num_q.get()  # 가장 작은 값 두개
    num_sum = num1 + num2
    result += num_sum
    num_q.put(num_sum)

print(result)
