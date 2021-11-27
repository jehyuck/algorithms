#입력
n = int(input())

#배열입력받기

numbers = list(map(int,input().split()))

#DP list 만들어주기
dp = [numbers[0]]

#D[i] = max(D[i-1] + n, n)
for i in range(1, n):
    dp.append(max(dp[i-1] + numbers[i], numbers[i]))

#출력
print(max(dp))