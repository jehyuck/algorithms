import sys
from collections import deque as d
input = sys.stdin.readline

N, K = map(int, input().split())

if K < N:
    print(N - K)
else:
    visit = [0] * 100001
    queue = d([N])
    while 1:
        crt = queue.popleft()
        if crt == K:
            print(visit[crt])
            break
        pos = [crt * 2, crt + 1, crt - 1]
        for i in pos:
            if 0 < i <= 100000 and visit[i] == 0:
                visit[i] = visit[crt] + 1
                queue.append(i)
