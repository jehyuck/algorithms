import sys
import heapq as h

input = sys.stdin.readline
N, E = map(int, input().split())
que = [0] +  [list() for _ in range(N)]

for i in range(E):
    a, b, c = map(int, input().split())
    que[a].append((c, b))
    que[b].append((c, a))

a, b = map(int, input().split())


def dijk(s, t):
    dist = [float('inf')] * (N + 1)
    dist[s] = 0
    heap = [(0, s)]

    while heap:
        w, crt = h.heappop(heap)
        if dist[crt] < w:
            continue
        for i in range(len(que[crt])):
            node = que[crt][i][1]
            value = w + que[crt][i][0]
            if dist[node] > value:
                dist[node] = value
                h.heappush(heap, (value, node))
            else:
                continue
    return [dist[t[0]], dist[t[1]]] if len(t) == 2 else dist[t[0]]


ans = dijk(1, [N])
a_b_1, a_b, a_b_n = dijk(1, [a, b]), dijk(a, [b]), dijk(N, [a, b])
answer = min((a_b_1[0] + a_b + a_b_n[1]), (a_b_1[1] + a_b + a_b_n[0]))
print(-1 if answer == float('inf') else answer)
