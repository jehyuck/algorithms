import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

T = int(input())


def dfs(idx, que, vis, cyc):
    rtn = 0
    visit[idx] = 1
    cyc.append(idx)
    next = que[idx]

    if vis[next] == 1:
        if next in cyc:
            rtn += len(cyc[cyc.index(next):])
    else:
        rtn = dfs(next, que, vis, cyc)
    return rtn


for _ in range(T):
    N = int(input())
    query = [0] + list(map(int, input().split()))
    visit = [0] * (N + 1)
    answer = 0
    for i in range(1, N + 1):
        if visit[i] == 0:
            cycle = []
            answer += dfs(i, query, visit, cycle)
    print(N - answer)
