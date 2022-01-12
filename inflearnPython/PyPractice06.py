import numpy as np

첫번째밭 = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1]
]

두번째밭 = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 3],
    [0, 0, 0, 0, 4],
    [0, 2, 0, 0, 2],
    [4, 5, 0, 2, 0],
] # 90도 돌려야 해요

print(np.rot90(두번째밭, 1) + np.array(첫번째밭)) # 더해봄
print(np.rot90(두번째밭, 1) - np.array(첫번째밭)) # 빼봄
print(np.rot90(두번째밭, 1) * np.array(첫번째밭)) # 곱해봄
print(np.rot90(두번째밭, 1) @ np.array(첫번째밭)) # 행렬의 곱셈

# 더한것을 이용하자
정답 = np.rot90(두번째밭, 1) + np.array(첫번째밭)
print(정답)

for j in range(5):
    print(chr(int(''.join(str(i) for i in 정답[j]), 8)))
