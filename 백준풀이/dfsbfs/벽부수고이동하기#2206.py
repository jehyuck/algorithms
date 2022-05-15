import sys
from collections import deque as d

input = sys.stdin.readline
N, M = map(int, input().split())
visit = [[[0] * M for i in range(N)] for _ in range(2)]
maps = []

#bfs
#1. bfs를 이용하여 (좌표, 벽 부숨 가능)을 저장하면 갱신한다.
#2. visit에는 방문 가능여부를 point로 저장
#3. 가장 먼저 도착한 답을 출력

delta = [(1,0), (0,1), (-1,0), (0,-1)]
visit[1][0][0] = 1
for i in range(N):
    maps.append(tuple(input()))

que = d()
que.append((0, 0, 1))
ans = -1

while que:
    crt = que.popleft()
    r, c, canDist = crt
    if r == N - 1 and c == M - 1:
        ans = visit[canDist][r][c]
        break
    for i in delta:
        dr, dc = i
        nr, nc = dr + r, dc + c
        if 0 <= nr < N and 0 <= nc < M:
            if maps[nr][nc] == '1' and canDist == 1:
                visit[0][nr][nc] = visit[1][r][c] + 1
                que.append((nr, nc, 0))
            elif maps[nr][nc] == '0' and visit[canDist][nr][nc] == 0:
                visit[canDist][nr][nc] = visit[canDist][r][c] + 1
                que.append((nr, nc, canDist))

print(ans)
