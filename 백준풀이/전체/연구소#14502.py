import sys
from collections import deque as d
input = sys.stdin.readline

N, M = map(int,input().split())

board = []

#조합과 bfs를 이용한 전체 탐색
#1. 바이러스와 빈 공간을 입력 받음
#2. 빈 공간에 대한 모든 가능성을 조합을 통해 구한다.
#2-1. 공간을 1로 채우고 바이러스가 퍼질수 있는 공간을 전부 퍼트린다.
#2-1-2. bfs를 이용해 바이러스를 퍼뜨릴 시 꽉 채운 값을 return
#2. 모든 가능성에 대해 최솟값을 구한다.
#3. 출력한다.

for i in range(N):
    board.append(input().split())

virus = []
zero = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            zero.append((i, j))
        elif board[i][j] == '2':
            virus.append((i, j))


def bfs(board_, virus_):
    count = 0
    delta = ((1, 0), (-1, 0), (0, -1), (0, 1))
    while (virus_):
        r, c = virus_.popleft()
        count += 1
        for i in delta:
            dr, dc = i
            pr, pc = r + dr, c + dc

            if 0 <= pr < N and 0 <= pc < M and board_[pr][pc] == '0':
                board_[pr][pc] = '3'
                virus_.append((pr, pc))

    return count


l = len(zero)
comb = []
zeros = len(virus) + len(zero) - 3
answer = 0
for i in range(l - 2):
    ri, ci = zero[i]
    board[ri][ci] = '1'
    for j in range(i + 1, l - 1):
        rj, cj = zero[j]
        board[rj][cj] = '1'
        for k in range(j + 1, l):
            rk, ck = zero[k]
            board[rk][ck] = '1'
            deque = d(virus)
            answer = max(answer, zeros - bfs([i.copy() for i in board], deque))
            board[rk][ck] = '0'
        board[rj][cj] = '0'
    board[ri][ci] = '0'

print(answer)
import sys
from collections import deque as d
input = sys.stdin.readline

N, M = map(int,input().split())

board = []

#조합과 bfs를 이용한 전체 탐색
#1. 바이러스와 빈 공간을 입력 받음
#2. 빈 공간에 대한 모든 가능성을 조합을 통해 구한다.
#2-1. 공간을 1로 채우고 바이러스가 퍼질수 있는 공간을 전부 퍼트린다.
#2-1-2. bfs를 이용해 바이러스를 퍼뜨릴 시 꽉 채운 값을 return
#2. 모든 가능성에 대해 최솟값을 구한다.
#3. 출력한다.

for i in range(N):
    board.append(input().split())

virus = []
zero = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            zero.append((i, j))
        elif board[i][j] == '2':
            virus.append((i, j))


def bfs(board_, virus_):
    count = 0
    delta = ((1, 0), (-1, 0), (0, -1), (0, 1))
    while (virus_):
        r, c = virus_.popleft()
        count += 1
        for i in delta:
            dr, dc = i
            pr, pc = r + dr, c + dc

            if 0 <= pr < N and 0 <= pc < M and board_[pr][pc] == '0':
                board_[pr][pc] = '3'
                virus_.append((pr, pc))

    return count


l = len(zero)
comb = []
zeros = len(virus) + len(zero) - 3
answer = 0
for i in range(l - 2):
    ri, ci = zero[i]
    board[ri][ci] = '1'
    for j in range(i + 1, l - 1):
        rj, cj = zero[j]
        board[rj][cj] = '1'
        for k in range(j + 1, l):
            rk, ck = zero[k]
            board[rk][ck] = '1'
            deque = d(virus)
            answer = max(answer, zeros - bfs([i.copy() for i in board], deque))
            board[rk][ck] = '0'
        board[rj][cj] = '0'
    board[ri][ci] = '0'

print(answer)
