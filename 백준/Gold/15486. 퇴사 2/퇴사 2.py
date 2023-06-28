
N = int(input())



def solution(n):
    dp = [0] * (n + 1)

    for i in range(n):
        t, p = map(int, input().split())
        dp[i] = max(dp[i - 1], dp[i])
        if i + t > n:
            continue
        dp[i + t] = max(dp[i] + p, dp[i + t])

    return max(dp[-1], dp[-2])

print(solution(N))