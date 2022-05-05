import sys
import heapq as h

N = int(input())


#dp와 비트마스킹
#dp[비트][길이][끝자리]
#1. i = 0을 제외한 2**i, 0, i 자리에 1을 넣는다
#2. 각 비트와 자릿수에 대해 0과 9를 제외하고 현재비트 + 2**(i - 1)or 2**(i + 1), 길이 + 1, (i - 1)or (i + 1)에 현재값을 더해준다.
#3. 전부 반복문이 끝나면 1023, N, 0~9에 대해 모든 합을 구한다.

if N < 10:
    print(0)
else:
    dp = [[[0 for k in range(10)] for j in range(N)] for i in range(4)]
    for i in range(1, 9):
        dp[0][0][i] = 1
    dp[2][0][9] = 1
    for i in range(N - 1):
        for j in range(10):
            for k in range(4):
                if dp[k][i][j] != 0:
                    if j == 0:
                        dp[k][i + 1][j + 1] += dp[k][i][j]
                    elif j == 9:
                        dp[k][i + 1][j - 1] += dp[k][i][j]
                    else:
                        if j == 8:
                            dp[k][i + 1][j - 1] += dp[k][i][j]
                            dp[k | 2][i + 1][j + 1] += dp[k][i][j]
                        elif j == 1:
                            dp[k | 1][i + 1][j - 1] += dp[k][i][j]
                            dp[k][i + 1][j + 1] += dp[k][i][j]
                        else:
                            dp[k][i + 1][j - 1] += dp[k][i][j]
                            dp[k][i + 1][j + 1] += dp[k][i][j]
    answer = 0
    for i in range(10):
        answer += dp[3][N - 1][i]
    print(answer % 1000000000)

"""
처음풀이
계단식으로 움직임 a -> a-1 and a+1
DP[기존 비트 |(비트 연산자 or) 1 <<(비트 shift) (a - 1) and (a + 1)][이전길이 + 1][a-1 and a-1]의 위치에 이전 값을 더해준다.

문제 특성상 0과 9를 방문한 기록만 있으면 0 ~ 9 를 전부 방문한 것이 된다.
0과 9만 비트로 다룬다.
배열의 크기를1024 --> 4로 줄일수있음
"""