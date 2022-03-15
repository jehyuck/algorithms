import sys

input = sys.stdin.readline

#dp
#1. 3가지 방향에 대해 각각 다르게 dp로 전달.
#2. 직선 방향은 전달 가능하다면 직선과 대각선에 전달. 가운데는 전부, 아래는 아래 대각선,
#2. 벽을 만나면 전달하지 않는다.(전달된 값이 존재하지 않았던 것으로 처리)
#2. 위에서 차례대로 진행한다.
#3. 3가지 방법(가로 새로 대각)으로 도착한 값에 대한 합산을 한다.
N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
crt = (0, 0)


def check_first(in_, to_):
    cr, cc = in_[0] + to_[0], in_[1] + to_[1]
    if 0 <= cr < N and 0 <= cc < N:
        if to_ == (1, 0):
            if maps[cr][cc]:
                return 0
        elif to_ == (1, 1):
            if maps[cr][cc] or maps[cr - 1][cc] or maps[cr][cc - 1]:
                return 0
        elif to_ == (0, 1):
            if maps[cr][cc]:
                return 0
        return 1
    return 0


for i in range(N):
    for j in range(N):
        if check_first((i, j), (0, 1)):
            dp[i][j + 1][0] += dp[i][j][0] + dp[i][j][1]
        if check_first((i, j), (1, 1)):
            dp[i + 1][j + 1][1] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
        if check_first((i, j), (1, 0)):
            dp[i + 1][j][2] += dp[i][j][2] + dp[i][j][1]
if maps[N - 1][N - 1] == 1:
    print(0)
else:
    print(sum(dp[N - 1][N - 1]))
