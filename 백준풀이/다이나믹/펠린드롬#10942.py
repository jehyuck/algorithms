import sys

input = sys.stdin.readline

N = int(input())
num = tuple(map(int, [0] + input().split()))
T = int(input())
que = [tuple(map(int, input().split())) for _ in range(T)]

#dp
#1. 길이가 2인 것까지는 따로 구한다.
#1. 길이가 1이면 무조건 true
#1. 길이가 2이면 두개가 같은지 확인
#2. 길이를 첫 반복문으로
#3. 시작지점을 두번째 반복문으로
#4. 길이가 3부터 양끝이 같고 dp[start + 1][end - 1]이 true 두가지를 만족하면 팰린드롬
#5. 미리구해놓은 dp로 질문지에 대답한다.

dp = [[]] + [[0] * (len(num)) for i in range(len(num) - 1)]

for i in range(1, len(num) - 1):
    dp[i][i] = 1
    dp[i][i + 1] = 1 if num[i] == num[i + 1] else 0
dp[len(num) - 1][len(num) - 1] = 1

for length in range(3, len(num)):
    start = 1
    end = start + length - 1
    while end < len(num):
        # print(start, end)
        if num[start] == num[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1
        start += 1
        end += 1

for i in que:
    print(dp[i[0]][i[1]])
