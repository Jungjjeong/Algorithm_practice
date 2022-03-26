document = list(map(str, input()))
word = list(map(str, input()))

answer = 0
cur_idx = 0

while cur_idx < len(document):
    for idx in range(len(word)):
        if cur_idx + idx >= len(document):
            cur_idx += 1
            break

        if word[idx] != document[cur_idx + idx]:
            cur_idx += 1
            break
    else:
        answer += 1
        cur_idx += len(word)

print(answer)
