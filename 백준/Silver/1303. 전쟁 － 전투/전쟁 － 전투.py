import sys
from collections import deque as d


input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    W, B = 0, 0

    dr = (1, 0, -1, 0)
    dc = (0, 1, 0, -1)

    board = [list(input().rstrip()) for _ in range(M)]
    visit = [[False] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if visit[i][j]: continue

            visit[i][j] = True

            target = board[i][j]

            temp = 1
            que = d()
            que.append((i, j))
            while que:
                r, c = que.popleft()

                for d_ in range(4):
                    nr = r + dr[d_]
                    nc = c + dc[d_]

                    if not check_bound(nr, nc, M, N): continue
                    if visit[nr][nc]: continue
                    if board[nr][nc] != target: continue

                    visit[nr][nc] = True
                    temp += 1
                    que.append((nr, nc))

            if target == 'W':
                W += temp ** 2
            else:
                B += temp ** 2

    return W, B


def check_bound(r, c, n,m ):
    return 0 <= r < n and 0 <= c < m


print(*solution())
