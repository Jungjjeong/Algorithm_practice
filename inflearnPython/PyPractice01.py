# 섬으로 향하라!

# '   + -- + - + -   '
# '   + --- + - +   '
# '   + -- + - + -   '
# '   + - + - + - +   '

# 해(1)와 달(0),
# Code의 세상 안으로!(En-Coding)

# encoding -> 부호화 : 문자나 기호들의 집합을 컴퓨터에서 표현하는 방법
# 이진법 -> 알파벳으로 나타내자

text = [ ' + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ',]
result=[]
for i in text:
    result.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'), 2))) 
#strip -> 앞 뒤 공백 삭제, replace , 2를 적을 시 이진법으로 자동 인식

#ord() : 문자 -> 숫자
#chr() : 숫자 -> 문자

print(''.join(result)) #문자열 출력

#list
print([i for i in range(10)]) #list 생성
print([i for i in range(10) if i%2 == 0]) 
print([f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1,10)]) # j for문은 i for문에 소속

'111'.zfill(10) # default 0, 자릿수를 맞춰줌


s = [i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]
print(s)

print(list(map(lambda x : chr(int(x,2)), s))) # lambda function

def f(x):
    return chr(int(x,2))
#zip

print(''.join(list(map(f , s))))
