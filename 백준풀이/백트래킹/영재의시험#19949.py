import sys

input = sys.stdin.readline

#백트래킹
#1. 한 층에 대해서 1번부터 5번까지 dfs
#2. 3층 부터는 연속되는 찍기에 대한 유망성 검사
#3. 5층부터 정답갯수에 대한 유망성 검사
#4. 11층에 도달하면 1을 리턴

answer = tuple(input().split())
ans_p = [0] * 10
def dfs(f, ans, cor):
    if f > 5 and f - 5 > cor:
        return 0
    if f == 10:
        if cor > 4:
            return 1
        else:
            return 0
    cnt = 0
    for i in "12345":
        ans_p[f] = i
        if f > 1 and ans_p[f - 2] == ans_p[f - 1] == ans_p[f]:
            continue
        cnt += dfs(f + 1, ans, cor + 1 if answer[f] == i else cor)
    return cnt


print(dfs(0, answer, 0))
