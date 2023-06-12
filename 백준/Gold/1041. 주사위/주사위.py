from itertools import combinations as c

N = int(input())
inf = (6 ** N) * 50 + 1
dice = list(map(int, input().split()))


def find_comb(n, s, r):
    rtn = inf

    for ele in c(range(6), n):
        set_ele = set(ele)
        continue_flag = False
        for false_target in r:
            if len(set_ele - false_target) == n - 2:
                continue_flag = True
                break

        if continue_flag: continue
        sum_ = 0
        for i in ele:
            sum_ += s[i]
        rtn = min(rtn, sum_)

    return rtn


def solution(n, shape):
    rules = [{0, 5}, {1, 4}, {3, 2}]

    if n == 1:
        max_five = sum(shape) - max(shape)
        return max_five

    max_two = find_comb(2, shape, rules)
    max_three = find_comb(3, shape, rules)
    two_shapes = (n * 8 - 12)
    # print(((n ** 2) * 5 - two_shapes * 2 - 12))
    # print(max_two, max_three)
    return max_three * 4 + max_two * two_shapes + min(shape) * ((n ** 2) * 5 - two_shapes * 2 - 12)


print(solution(N, dice))
