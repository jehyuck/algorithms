import sys

input = sys.stdin.readline

def solution():
    answer = 0

    R, C, H = map(int, input().split())
    N = int(input())

    total = R * C * H
    cube = [tuple(map(int, input().split())) for _ in range(N)]
    cube.sort(reverse=True)

    total_now = 0
    for c_idx, c_count in cube:
        c_len = 2 ** c_idx
        total_now *= 8

        cnt_limit = (R // c_len) * (C // c_len) * (H // c_len) - total_now
        cnt_limit = min(c_count, cnt_limit)

        answer += cnt_limit
        total_now += cnt_limit


    if total == total_now:
        return answer
    else:
        return -1

print(solution())