#입력
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())

display = []
visit = [[False for _ in range(N)] for _ in range(N)]

for _ in range(N):
    display.append(input())

#R,G,B따라 구역을 나눔
# 1.i,j값이 방문하지 않았으면 가져온다.
# 2.사방(동서남북)으로 색이 같은게 있으면 dfs로 들어가고 방문처리한다.
# 3.dfs가 끝나면 RGB_count += 1을 한다.
# 4.방문판별list를 초기화한다.
# 5.사방으로 색이 같은게(R과 G는 동일 색으로 간주)있으면 dfs로 들어가고 방문처리
# 6.dfs가 끝나면 RG_B_count += 1을 한다.
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(y, x, color):
    # 1.i,j값이 방문하지 않았으면 가져온다.
    visit[y][x] = True

    # 2.사방(동서남북)으로 색이 같은게 있으면 dfs로 들어가고 방문처리한다.
    for dy, dx in direction:
        my, mx = dy + y, dx + x

        if 0 <= my < N and 0 <= mx < N and not visit[my][mx] and display[my][mx] in color:
            dfs(my, mx, color)


RGB_count = 0

for i in range(N):
    for j in range(N):
        # 1.i,j값이 방문하지 않았으면 가져온다.
        if not visit[i][j]:
            # 3.dfs가 끝나면 RGB_count += 1을 한다.
            dfs(i, j, display[i][j])
            RGB_count += 1

RG_B_count = 0

# 5.사방으로 색이 같은게(R과 G는 동일 색으로 간주)있으면 dfs로 들어가고 방문처리
def rg_b(x):
    return 'B' if x=='B' else 'RG'

visit = [[False for _ in range(N)]  for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 1.i,j값이 방문하지 않았으면 가져온다.
        if not visit[i][j]:
            #5를 이용
            dfs(i,j,rg_b(display[i][j]))

            # 6.dfs가 끝나면 RG_B_count += 1을 한다.
            RG_B_count += 1
print(RGB_count, RG_B_count)

"""
우선탐색 알고리즘을 이용한 전체탐색
1.dfs를 이용해품, bfs로도 풀어보기
"""