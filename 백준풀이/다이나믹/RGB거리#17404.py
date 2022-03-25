import sys
input = sys.stdin.readline

#dp
#첫 방의 값을 고정시키고 끝방의 같은 색일 때의 경우의 수를 제외하고 최솟값을 구한다.
#3번 dp를 돌려 각각에서 나온 2개의 값을 비교 반복문은 3번 answer는 6개 나옴
#1. 첫 방 색을 기준으로 반복문을 3번 돌린다.
#2. 각각의 반복문에서는 dp[i] = color[i] + min(dp[i-1][다른색1], dp[i-1][다른색2])
#3. dp[끝]의 값중에서 첫번째 색을 제외한 색중 작은값을 선택
#4. 모두 비교후 가장 작은 것을 출력

N = int(input())
weight = []
answer = float('inf')
for _ in range(N):
    weight.append(tuple(map(int, input().split())))

for i in range(3):
    dp = [[0,0,0] for _ in range(N)]
    dp[0] = [float('inf')] * 3
    dp[0][i] = weight[0][i]

    for j in range(1, N):
        dp[j][0] = weight[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = weight[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = weight[j][2] + min(dp[j - 1][1], dp[j - 1][0])

    for j in range(3):
        if j != i:
            answer = min(answer, dp[-1][j])

print(answer)