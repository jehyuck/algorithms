#숫자 갯수 입력
n = int(input())

#문제 입력
numbers = list(map(int,input().split()))

dp = [1]*n

#n개 만큼을 동적계획법으로 실행, 자기보다 작은 것들 중 가장 큰 것을 고른다
for i in range(n):
    maxV = 1

    for j in range(i):
        if numbers[j] < numbers[i]:
            maxV = max(dp[j]+1, maxV)

    dp[i] = maxV

#dp값 중 가장 큰 것을 답으로 제출
print(max(dp))