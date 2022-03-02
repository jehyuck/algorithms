import sys
input = sys.stdin.readline

#입력

board = []
zeros = []
for i in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))

#백트래킹
#1. 0인 점들을 찾꺼낸다.
#2. set을 이용해 열, 행, 블록 체크를 한다.
#2. 가능한 수들을 구하고 그 수를 바탕으로 dfs를 한다.
#2. 틀리면 0으로 바꾸고 탈출한다.
#3. 맞으면 출력후 종료한다.


def dfs(boards, nexts, crt, f):
    if crt == f:
        return True

    r, c = nexts[crt]
    pos = [0] * 10
    for i in (0, 1, 2, 3, 4, 5, 6, 7, 8):
        pos[boards[i][c]] = 1

    for i in boards[r]:
        pos[i] = 1

    rr, cc = (r // 3) * 3, (c // 3) * 3
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            pos[boards[rr + i][cc + j]] = 1

    for i in range(1, 10):
        if pos[i] == 0:
            boards[r][c] = i
            if dfs(boards, nexts, crt + 1, f):
                return True

    boards[r][c] = 0
    return False


dfs(board, zeros, 0, len(zeros))
for i in range(9):
    print(" ".join(map(str, board[i])))


"""
백트래킹을 이용한 기본 문제
시간을 줄이기 위해
1.처음에 시간을 줄이기 위해 가능성 있는 list를 set에서 비트마스킹과 유사하게 바꿔줌
2.분리했던 가능성 체크 기능들을 dfs에 한꺼번에 넣음
3.몇 개의 값들을 함수가 아닌 상수 값으로 바꿔줌

...
시간을 더 줄이기 위해 (pypy가 아닌 python으로 통과)
가능성에 대한 경우의 수를 미리 구하기(look up table??) 고민해 보기
"""