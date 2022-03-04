import sys
input = sys.stdin.readline

N = int(input())

case = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, 2) ,(-1, 2) ,(1, -2) ,(-1, -2)]
#델타를 이용한 bfs
#1. 나이트가 이동할 수 있는 8가지에 대한 델타값을 구한다.
#2. 8경우에 대한 모든 이동할 수 있는 이동값에 대해 count +1을 하며 queue에 저장
#2. 정답이 나올 때까지 방문하지 않은 경우의 수만 추가하며 계속 구한다.

for i in range(N):
    size = int(input())
    s = tuple(map(int, input().split()))
    t = tuple(map(int, input().split()))
    board = [[0] * size for _ in range(size)]
    crt = [s]
    temp = []
    count = 0
    board[s[0]][s[1]] = 0
    while 1:
        temp = []
        if t == crt[0]:
            print(board[t[0]][t[1]])
            break
        while crt:
            r, c = crt.pop()
            for k in case:
                pr = k[0] + r
                pc = k[1] + c
                if 0 <= pr < size and 0 <= pc < size:
                    if board[pr][pc] == 0:
                        board[pr][pc] = 1 + board[r][c]
                        if (pr, pc) == t:
                            temp = [t]
                            break
                        temp.append((pr, pc))
        crt = temp
