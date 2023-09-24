import sys
from collections import deque as d

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

input = sys.stdin.readline


def find_area(N, h, board):
    global dr, dc

    rtn = 0
    visit = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visit[i][j]: continue

            visit[i][j] = True

            if board[i][j] <= h:
                continue

            rtn += 1
            que = d()

            que.append((i, j))
            while que:
                r, c = que.popleft()
                for d_ in range(4):
                    nr = r + dr[d_]
                    nc = c + dc[d_]

                    if not check_bound(nr, nc, N): continue
                    if visit[nr][nc]: continue
                    visit[nr][nc] = True
                    if board[nr][nc] <= h: continue

                    que.append((nr, nc))

    return rtn


def check_bound(r, c, n):
    return 0 <= r < n and 0 <= c < n


def solution():
    answer = 1
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    h = 0
    for i in range(1, 101):
        answer = max(answer, find_area(N, i, board))

    return answer


print(solution())