import sys
from collections import deque as d
input = sys.stdin.readline
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    restart = [[] for _ in range(26)]
    visit = [[0] * (M + 2) for _ in range(N + 2)]
    que = d([(0, 0)])
    rtn = 0
    while que:
        cr, cc = que.popleft()
        for i in delta:
            nr, nc = cr + i[0], cc + i[1]
            if 0 <= nr < N + 2 and 0 <= nc < M + 2:
                # print(nr, nc, board[nr][nc])
                if visit[nr][nc]:
                    continue
                if board[nr][nc] == '*':
                    continue
                elif board[nr][nc] == '$':
                    rtn += 1
                elif board[nr][nc].isupper():
                    if keys_[ord(board[nr][nc]) - 65] == 0:
                        restart[ord(board[nr][nc]) - 65].append((nr, nc))
                        continue
                elif board[nr][nc].islower():
                    # print(board[nr][nc])
                    keys_[ord(board[nr][nc]) - 97] = 1
                    if restart[ord(board[nr][nc]) - 97]:
                        que.extend(restart[ord(board[nr][nc]) - 97])

                que.append((nr, nc))
                visit[nr][nc] = 1
    return rtn
T = int(input())
ans = []
for _ in range(T):
    N, M = map(int, input().split())
    board = [['.'] * (M + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        que = input().rstrip()
        for j in range(1, 1 + M):
            board[i][j] = que[j - 1]
    key = input().rstrip()
    keys_ = [0] * 26

    if key != '0':
        for i in range(len(key)):
            keys_[ord(key[i]) - 97] = 1
    # print(*board, sep='\n')
    ans.append(bfs())
    # print(keys_)
print(*ans, sep='\n')