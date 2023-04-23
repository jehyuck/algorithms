from collections import deque as d
N, M, K = map(int, input().split())

gram = 1e9
n = N - 1
m = M - 1
answer = int(1e9)
board = [list(map(int, input().split())) for _ in range(N)]

visit = [[int(1e9)] * M for _ in range(N)]
visit[0][0] = 0

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

que = d()
que.append((0, 0, 0))


def check_bound(r, c, nn ,mm):
    return 0 <= r < nn and 0 <= c < mm


while que:
    r, c, d_ = que.popleft()

    nd_ = d_ + 1
    for d__ in range(4):
        nr = dr[d__] + r
        nc = dc[d__] + c
        if not check_bound(nr, nc, N, M): continue
        # print(nr, nc)
        if board[nr][nc] == 2:
            gram = min(gram, abs(n - nr) + abs(m - nc) + nd_)
        if board[nr][nc] == 1: continue
        if visit[nr][nc] <= nd_ or nd_ >= K: continue
        visit[nr][nc] = nd_
        que.append((nr, nc, nd_))

res = min(gram, visit[n][m])
if res <= K:
    print(res)
else:
    print('Fail')