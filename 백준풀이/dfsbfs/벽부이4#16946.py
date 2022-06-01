import sys
from collections import deque as d
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
count_fill = []
count = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = ["" for _ in range(N)]

def fill(cnt, r, c):
    rtn = 1
    que = d([(r, c)])
    board[r][c] = cnt
    while que:
        cr, cc = que.popleft()
        # print(cnt, cr, cc)

        for i in range(len(delta)):
            nr, nc = cr + delta[i][0], cc + delta[i][1]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '0':
                    que.append((nr, nc))
                    board[nr][nc] = cnt
                    rtn += 1
    return rtn

def find_can_go(r, c):
    rtn = 0
    can_go = set()
    for i in range(len(delta)):
        nr, nc = r + delta[i][0], c + delta[i][1]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] != '1' and board[nr][nc] not in can_go:
                rtn += count_fill[board[nr][nc]]
                can_go.add(board[nr][nc])

    return rtn


for i in range(N):
    for j in range(M):
        if board[i][j] == '1':
            continue
        elif board[i][j] == '0':
            # print('\n', i, j, board[i][j])
            count_fill.append(fill(count, i, j))
            count += 1
# print(*board, sep='\n')
# print(count_fill)
for i in range(N):
    for j in range(M):
        if board[i][j] == '1':
            ans[i] += str((find_can_go(i, j) + 1) % 10)
        else:
            ans[i] += '0'

print(*ans, sep="\n")