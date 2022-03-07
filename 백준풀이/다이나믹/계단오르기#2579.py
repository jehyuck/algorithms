import sys
input = sys.stdin.readline

N = int(input())


if N == 1:
    dp = [int(input())]
else:
    dp = [0] * (N + 1)
    stair = [0] + [int(input()) for _ in range(N)]
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    for i in range(3, N + 1):
        dp[i] = max(stair[i] + stair[i - 1] + dp[i - 3], stair[i] + dp[i - 2])

print(dp[-1])
