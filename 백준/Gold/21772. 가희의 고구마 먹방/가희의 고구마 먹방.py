import sys


input = sys.stdin.readline
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


def check_bound(r, c, R, C):
    return 0 <= r < R and 0 <= c < C


def dfs(board, crt, r, c, t, R, C, T):
    global dr, dc

    if t >= T:
        return crt
    rtn = crt


    for d_ in range(4):
        nr = r + dr[d_]
        nc = c + dc[d_]

        if not check_bound(nr, nc, R, C): continue
        if board[nr][nc] == "#": continue

        temp = board[nr][nc]
        board[nr][nc] = '.'
        rtn = max(rtn, dfs(board, crt + (1 if temp == "S" else 0), nr, nc, t + 1, R, C, T))
        board[nr][nc] = temp

    return rtn

def solution():
    R, C, T = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(R)]
    r, c = 0, 0

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'G':
                r = i; c = j
                break
    return dfs(board, 0, r, c, 0, R, C, T)


print(solution())
