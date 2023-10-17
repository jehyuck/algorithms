import sys

input = sys.stdin.readline


def get_answer(flag, start_r, start_c, k, prefix, board):
    end_r, end_c = start_r + k, start_c + k
    rtn = prefix[end_r][end_c][flag]
    if start_r != 0:
        rtn -= prefix[start_r - 1][end_c][flag]
    if start_c != 0:
        rtn -= prefix[end_r][start_c - 1][flag]
    if start_c != 0 and start_r != 0:
        rtn += prefix[start_r - 1][start_c - 1][flag]
    return rtn



def solution():
    answer = 4000001
    N, M, K = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    prefix = [[[0, 0] for _ in range(M)] for _ in range(N)]

    target1 = 'B'
    target2 = 'W'

    for i in range(N):
        for j in range(M):
            temp_target1 = target1 if (i + j) % 2 == 0 else target2
            temp_target2 = target2 if (i + j) % 2 == 0 else target1

            if temp_target1 != board[i][j]:
                prefix[i][j][0] = 1
            if temp_target2 != board[i][j]:
                prefix[i][j][1] = 1

    for i in range(N):
        for j in range(1, M):
            prefix[i][j][0] += prefix[i][j - 1][0]
            prefix[i][j][1] += prefix[i][j - 1][1]
    for i in range(M):
        for j in range(1, N):
            prefix[j][i][0] += prefix[j - 1][i][0]
            prefix[j][i][1] += prefix[j - 1][i][1]
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            answer = min(answer, get_answer(0, i, j, K - 1, prefix, board))
            answer = min(answer, get_answer(1, i, j, K - 1, prefix, board))
    return answer
print(solution())