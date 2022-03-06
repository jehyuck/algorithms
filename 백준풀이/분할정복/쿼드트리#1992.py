import sys
input = sys.stdin.readline

N = int(input())
#분할정복 dfs
#1. 4분할로 왼쪽위부터 오른쪽 아래를 보는 방법을 사용
#2. 분할하고 dfs를 한다.
#2. 괄호를 연다.
#2. 분할된 값이 전부 같으면 칸을 채우고 종료
#2. 분할된 값이 다르면 또 분할해서 dfs
#2. 4분할이 끝나면 괄호를 닫고 종료
#3. 출력
board = [list(input()) for _ in range(N)]


def dfs(crt, N):
    count = 0
    r, c = crt
    for i in range(N):
        count += board[r + i][c:c + N].count('1')
    if count == N * N:
        print('1', end='')
        return
    elif count == 0:
        print('0', end='')
        return
    else:
        half = N // 2
        print('(', end='')
        pos = [(r, c), (r, c + half), (r + half, c), (r + half, c + half)]
        for i in pos:
            dfs(i, half)
        print(')', end='')


dfs((0, 0), N)

