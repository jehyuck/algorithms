import sys
input = sys.stdin.readline

N = int(input())


def find_123(n):
    dp = [0, 1, 2, 4]
    for i in range(4, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    return dp[n]


for i in range(N):
    print(find_123(int(input())))