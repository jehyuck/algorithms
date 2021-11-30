#입력
n, k = list(map(int,input().split()))

#입력2
coins = []
for i in range(n):
    coins.append(int(input()))

#다이나믹 값은 코인값을 빼주었을 때 해당하는 메모리값
#핵심 d[i] = for coin in coins  {for n in k} : sum += d[n- coin]
dp = [1] + [0]*k
for i in range(n):
    for j in range(1,k+1):
        target = j-coins[i]
        if target >= 0:
            dp[j] += dp[target]

print(dp[-1])

