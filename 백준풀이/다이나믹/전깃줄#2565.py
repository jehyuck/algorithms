#입력
import sys
input = sys.stdin.readline

N = int(input())


#dp 최장공통부분수열(LCS)기초 문제
#1. 한쪽 순서를 기준으로 정렬한다.
#2. 정렬되지 않은 부분을 기준으로 최장공통부분수열 적용
#3. 사용할 전깃줄 만 고르는 과정
#3-1. dp[i] = i보다 작은것중 가장 큰 것 + 1
#4. dp값중 가장 큰 것이 사용될 전깃줄의 수 이므로 답은 = 전깃줄 - max(dp)

lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
#1. 한쪽 순서를 기준으로 정렬한다.
dp = [1]*N

#2. 정렬되지 않은 부분을 기준으로 최장공통부분수열 적용
answer = 0
sortedline = sorted(lines)

for i in range(N):
    for j in range(i-1,-1,-1):
        # 3-1. dp[i] = i보다 작은것중 가장 큰 것 + 1
        if sortedline[i][1] > sortedline[j][1] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

#4. dp값중 가장 큰 것이 사용될 전깃줄의 수 이므로 답은 = 전깃줄 - max(dp)
print(N - max(dp))

"""
dp응용문제 lcs
"""