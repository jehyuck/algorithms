
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]


def check_bound(r, c, n, m):
    return 0 <= r < n and 0 <= c < m


def solution(N, M, board):
    answer = 0
    dr = (-1, 0, 1)
    m = M - 1

    for i in range(N):
        stack = []
        stack.append((i, 0))

        while stack:
            r, c = stack.pop()
            # print(r, c)
            board[r][c] = 'o'
            if c == m:
                answer += 1
                board[r][c] = 'o'
                break
            for d in range(2, -1, -1):
                nr = r + dr[d]
                nc = c + 1
                if not check_bound(nr, nc, N, M):
                    continue
                if board[nr][nc] == '.':
                    stack.append((nr, nc))


    return answer


print(solution(N, M, board))
# print(*board, sep='\n')
