import sys

input = sys.stdin.readline


def solution():
    N, D = map(int, input().split())

    dp = [i for i in range(D + 1)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key= lambda x: x[1])
    for i in arr:
        a, b, c = i
        if b > D:
            continue

        temp = dp[a] + c
        if dp[b] < temp:
            continue
        else:
            dp[b] = temp
            for j in range(b, D + 1):
                dp[j] = min(dp[j - 1] + 1, dp[j])
    return dp[-1]


print(solution())