import sys
from collections import defaultdict as dd

input = sys.stdin.readline


def solution():
    answer_value, answer_count = 200001, 500001
    N, H = map(int, input().split())

    dp = [0] * (H + 2)
    for i in range(N):
        l = int(input())

        if i % 2 == 0:
            dp[0] += 1
            dp[l] -= 1
        else:
            dp[-1] -= 1
            dp[H - l] += 1

    for i in range(1, len(dp) - 1):
        dp[i] += dp[i - 1]
        if dp[i] < answer_value:
            answer_value = dp[i]
            answer_count = 1
        elif dp[i] == answer_value:
            answer_count += 1

    return answer_value, answer_count


print(*solution())
