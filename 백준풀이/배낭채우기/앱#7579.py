#입력
N, M = map(int,input().split())
memory = [0] + list(map(int,input().split()))
costs = [0] + list(map(int,input().split()))
cost_boundary = sum(costs)+1
#코스트를 기준으로 하는 배낭 체우기 문제
#코스트의 최대를 열 앱의 갯수를 행으로 한다.
#dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)
#1. i번째 물품을 0cost일때부터 target 메모리를 만족할 때까지 값을 구한다.
#2. 점화식에 맞게 dp(i,j)를 정해준다.
#3. j-cost가 음수이면 바로 위의 값을 복사한다.
#4. 2->3의 과정을 memory가 target을 넘을 때까지 반복한다.
#5. 물품 dp과정(반복문)이 끝날때 answer = j를 저장하고 반복문 종료시 출력한다.

answer = cost_boundary

dp = [[0 for _ in range(cost_boundary)] for _ in range(N+1)]
for i in range(1, N+1):
    up = i - 1
    for j in range(1,cost_boundary):
        if j < costs[i]:
            dp[i][j] = dp[up][j]
        else:
            dp[i][j] =  max(dp[up][j], dp[up][j-costs[i]] + memory[i])
        if dp[i][j] >= M:
            answer = min(j,answer)
            break

# print(*dp, sep="\n")
if M == 0:
    print(0)
else:
    print(answer)