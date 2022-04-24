from copy import deepcopy


def solution(tstring, variables):
    answer = ''
    dict = {}
    change_dict = {}
    count = 1

    for v in variables:
        v_key = '{{{0}}}'.format(v[0])
        dict[v_key] = v[1]
        change_dict[v_key] = v[1]

    is_change = True

    while is_change:
        change_dict2 = deepcopy(change_dict)
        is_change = False
        same = 0

        for k, v in change_dict.items():
            if v in dict.keys():
                is_change = True
                change_dict[k] = dict[v]

            if count > 1 and v == dict[k]:
                change_dict[k] = v + '@'
            elif count > 1 and v == k:
                change_dict[k] = k + '@'

        count += 1

        shared_items = {
            k: change_dict[k] for k in change_dict if k in change_dict2 and change_dict[k] == change_dict2[k]}

        if same == len(dict) or len(shared_items) == len(dict):
            break

    print(change_dict)


solution(
    "{a} {b} {c} {d} {i}", [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]])
