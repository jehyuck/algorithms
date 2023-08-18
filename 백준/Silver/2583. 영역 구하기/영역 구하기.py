import sys
from collections import deque as d

input = sys.stdin.readline


dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)


def check_bound(r, c, N, M):
    return 0 <= r < N and 0 <= c < M


def draw(b, c1, r1, c2, r2):
    global dr, dc

    for i in range(r1, r2):
        for j in range(c1, c2):
            b[i][j] = True


def solution():
    global dr, dc

    answer = []
    N, M, K = map(int, input().split())

    board = [[False] * M for _ in range(N)]

    for _ in range(K):
        c1, r1, c2, r2 = map(int, input().split())
        draw(board, c1, r1, c2, r2)

    for i in range(N):
        for j in range(M):
            if board[i][j]:
                continue
            board[i][j] = True

            que = d()
            que.append((i, j))

            temp_size = 1
            while que:
                r, c = que.popleft()

                for d_ in range(4):
                    nr = dr[d_] + r
                    nc = dc[d_] + c

                    if not check_bound(nr, nc, N, M):
                        continue
                    if board[nr][nc]:
                        continue
                    board[nr][nc] = True
                    temp_size += 1
                    que.append((nr, nc))

            answer.append(temp_size)
    answer.sort()
    print(len(answer))
    print(*answer)



solution()