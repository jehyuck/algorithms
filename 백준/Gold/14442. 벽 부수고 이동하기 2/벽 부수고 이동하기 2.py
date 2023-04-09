from collections import deque as d

N, M, K = map(int, input().split())
tn = N - 1
tm = M - 1

board = [list(input()) for _ in range(N)]
board_flat = [[11] * M for _ in range(N)]
board_flat[0][0] = 1
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


def check_bound(r, c, n, m):
    return not ( 0 <= r < n and 0 <= c < m)


answer = 1
escape = True
que = d([(0, 0, 0, 1)])
if N == 1 and M == 1:
    que = []
    escape = False

while escape and que:
    answer += 1
    # print(que)
    r, c, k, ans = que.popleft()
    kk = k + 1
    next_ans = ans + 1
    for dir_ in range(4):
        nr = r + dr[dir_]
        nc = c + dc[dir_]

        if not (0 <= nr < N and 0 <= nc < M): continue
        if board_flat[nr][nc] <= k: continue
        if nr == tn and nc == tm:
            answer = next_ans
            escape = False
            break
        if board[nr][nc] == '1':
            if kk <= K and board_flat[nr][nc] > kk:
                board_flat[nr][nc] = kk
                que.append((nr, nc, kk, next_ans))
        elif board[nr][nc] == '0':
            board_flat[nr][nc] = k
            que.append((nr, nc, k, next_ans))

print(answer if not escape else -1)