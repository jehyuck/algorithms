import sys

input = sys.stdin.readline

#백트래팅
#두가지 대각선에 대해 한곳을 기준으로 잡고 한곳은 판별만
#1. 한 점에 대해서 왼쪽 아래 대각선으로 한개 씩 채워 나간다.
#2. 방문할 수 없는 곳이면 다음 경우의 수를 본다.
#3. 그 점에서 다른 대각선을 봤을때 이미 칠해져 있으면 pass한다.
#4. 2n - 1이 그려지거나 가장 많이 그려진 경우를 return 한다.

N = int(input())
diagnal_visit_neg = [0] * (2 * N - 1)
diagnal_visit_pos = [0] * (2 * N - 1)

board = []
for i in range(N):
    board.append(list(map(int,input().split())))

def back_track(level, crt_level):
    if crt_level >= level:
        return 0
    rtn = 0
    idx_r, idx_c = (0, crt_level) if crt_level < N else (crt_level - N + 1, N - 1)
    # print(diagnal_visit_neg, level, crt_level)
    while 0 <= idx_r < N and 0 <= idx_c < N:
        if board[idx_r][idx_c] != 0 and diagnal_visit_neg[idx_c - idx_r + N - 1] == 0:
            # print(idx_r, idx_c)
            diagnal_visit_neg[idx_c - idx_r + N - 1] = 1
            rtn = max(rtn, 1 + back_track(level, crt_level + 2))
            diagnal_visit_neg[idx_c - idx_r + N - 1] = 0
        idx_r += 1
        idx_c -= 1
    zero_rtn = max(rtn, back_track(level, crt_level + 2))
    return max(rtn, zero_rtn)

print(back_track(2 * N - 1, 0) + back_track(2 * N - 1, 1))
# print(N, *board, sep="\n")

"""
대각선을 기준으로 n_queen을 풀듯이 idx를 나눠서 풀면 될줄알았는데 시간초과가 나서
대각선을 기준으로 나눈것은 동일하게 풀었지만 여기에 흑색바닥이면 흑색 바닥끼리만 보도록
흰색 바닥이면 흰색 바다만 보도록 하여 반복횟수를 줄여주었다.
"""