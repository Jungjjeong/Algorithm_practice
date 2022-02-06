test_num = int(input())  # 테스트케이스의 개수

for _ in range(test_num):
    document_num, order = map(int, input().split(' '))
    # 문서의 개수와 몇 번째로 인쇄되었는지 궁금한 문서
    priority_list = list(map(int, input().split(' ')))
    # 각 문서마다 중요도 나열

    idx_list = list(range(len(priority_list)))
    idx_list[order] = 'target'

    count = 0

    while True:
        max_priority = max(priority_list)  # 최댓값 (가장 먼저 인쇄될 친구)

        if priority_list[0] == max_priority:
            count += 1

            if idx_list[0] == 'target':
                print(count)
                break
            else:
                priority_list.pop(0)
                idx_list.pop(0)

        else:
            priority_list.append(priority_list.pop(0))
            idx_list.append(idx_list.pop(0))
