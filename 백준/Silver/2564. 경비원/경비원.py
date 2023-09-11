import sys

input = sys.stdin.readline


def find_index(d_, idx, N, M):
    if d_ == 1:
        return idx
    elif d_ == 2:
        return M * 2 + N - idx
    elif d_ == 3:
        return N * 2 + M * 2 - idx
    else:
        return M + idx


def solution():
    answer = 0

    M, N = map(int, input().split())
    shop_len = int(input())
    len_board = 2 * N + 2 * M

    shops = []
    for _ in range(shop_len):
        d, i = map(int, input().split())
        shop = find_index(d, i, N, M)
        shops.append(shop)

    target = find_index(*map(int, input().split()), N, M)
    for ele in shops:
        if target > ele:
            answer += min(target - ele, ele + len_board - target)
        else:
            answer += min(ele - target, len_board - ele + target)
        # answer += min(abs((ele - len_board - target) % len_board), abs(target - ele), abs((target + len_board - ele) % len_board))

    return answer

print(solution())
