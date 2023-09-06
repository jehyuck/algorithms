import sys
from collections import deque as d

input = sys.stdin.readline


def check_bound(r, c, n, m):
    return 0 <= r < n and 0 <= c < m


def solution():
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    N, M = map(int, input().split())
    n, m = N - 1, M - 1

    board = [list(map(int, list(input().rstrip()))) for _ in range(N)]

    que = d()
    que.append((0, 0))

    answer = 1
    while que:
        answer += 1
        temp = d()

        for ele in que:
            r, c = ele

            for d_ in range(4):
                nr = r + dr[d_]
                nc = c + dc[d_]

                if not check_bound(nr, nc, N, M): continue
                if board[nr][nc] == 0: continue
                if nr == n and nc == m:
                    return answer

                temp.append((nr, nc))
                board[nr][nc] = 0

        que = temp
    return answer

print(solution())