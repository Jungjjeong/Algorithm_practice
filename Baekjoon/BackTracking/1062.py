from itertools import combinations

n, k = map(int, input().split())
answer = 0

# 무조건 배워야 하는 알파벳
essential_word = {'a', 'n', 't', 'i', 'c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - essential_word
word_arr = [input()[4:-4] for _ in range(n)]


def count(word_arr, learned_alphabet):
    cnt = 0
    for word in word_arr:
        can_read = 1
        for w in word:
            # 안배운 글자
            if learned_alphabet[ord(w) - ord('a')] == 0:
                can_read = 0
                break
        if can_read == 1:
            cnt += 1
    return cnt


if k >= 5:
    learned_alphabet = [0] * 26
    for x in essential_word:
        learned_alphabet[ord(x) - ord('a')] = 1

    # k-5길이로 만들 수 있는 모든 조합
    for teach in list(combinations(remain_alphabet, k-5)):
        for t in teach:
            learned_alphabet[ord(t) - ord('a')] = 1
        cnt = count(word_arr, learned_alphabet)

        answer = max(cnt, answer)

        for t in teach:
            learned_alphabet[ord(t) - ord('a')] = 0

    print(answer)
else:
    print(0)
