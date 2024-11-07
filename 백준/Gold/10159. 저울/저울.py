import sys
from collections import defaultdict as dd


input = sys.stdin.readline


def getAdj(n, m):
    adj = [[0] * n for _ in range(n)]
    for _ in range(m):
        h, l = map(lambda x: int(x) - 1, input().split())
        adj[h][l] = 1
    return adj


def fw(arr, n):
    for j in range(n):
        for i in range(n):
            for k in range(n):
                if arr[i][j] == 1 and arr[j][k] == 1:
                    arr[i][k] = 1
    pass


def getAnswer(adj, n):
    rtn = [0] * n
    for i in range(n):
        cnt = 0
        for j in range(n):
            if adj[i][j] == 1:
                cnt += 1
            if adj[j][i] == 1:
                cnt += 1
        rtn[i] = n - cnt - 1
    return rtn


def solution():
    N = int(input())
    M = int(input())

    adj = getAdj(N, M)
    fw(adj, N)

    rtn = getAnswer(adj, N)
    return "\n".join(map(str, rtn)).rstrip()


print(solution())