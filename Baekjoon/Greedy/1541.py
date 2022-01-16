arr = list(map(str, input().split('-')))

result = 0

for n in list(arr[0].split('+')):
    result += int(n)


for n in arr[1:]:
    for i in list((n.split('+'))):
        result -= int(i)


print(result)
