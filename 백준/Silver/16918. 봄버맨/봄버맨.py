import sys

input = sys.stdin.readline

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


def check_bound(nr, nc, R, C):
    return 0 <= nr < R and 0 <= nc < C


def bomb(board, R, C):
    global dr, dc
    que = list()
    for r in range(R):
        for c in range(C):

            if board[r][c] == 1:
                que.append((r, c))
            elif board[r][c] == 0:
                continue
            else:
                board[r][c] -= 1

    for ele in que:
        r, c = ele
        board[r][c] = 0
        for d_ in range(4):
            nr = r + dr[d_]
            nc = c + dc[d_]

            if not check_bound(nr, nc, R, C):
                continue
            board[nr][nc] = 0


def find_answer(board,R,C):
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                board[r][c] = '.'
            else:
                board[r][c] = 'O'

    return '\n'.join(map(lambda x : ''.join(x), board))


def insert_bomb(board, R, C):
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                board[i][j] = 3
            else:
                board[i][j] -= 1


def solution():
    count = 1
    R, C, N = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                board[i][j] = 2
            else:
                board[i][j] = 0

    if N == 1: return find_answer(board, R, C)
    while True:
        insert_bomb(board, R, C)

        count += 1
        if count == N: return find_answer(board, R, C)
        bomb(board, R, C)
        count += 1
        if count == N: return find_answer(board, R, C)

print(solution())