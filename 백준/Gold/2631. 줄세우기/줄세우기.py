import sys


input = sys.stdin.readline


def solution():
    N = int(input())

    idle = [0] * (N)
    dp = [1] * (N)
    for i in range(N):
        idle[i] = int(input())

    for i in range(1, N):
        for j in range(i):
            if idle[j] < idle[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    return N - max(dp)

print(solution())