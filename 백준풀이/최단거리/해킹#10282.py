import sys
import heapq as h

input = sys.stdin.readline
T = int(input())


def dijk(s, n):
    dist[s] = 0
    heap = [(0, s)]
    cnt = 0
    while heap:
        w, crt = h.heappop(heap)
        if dist[crt] < w:
            continue
        cnt += 1
        if cnt == n:
            return [cnt, w]
        for i in range(len(graph[crt])):
            node = graph[crt][i][1]
            value = w + graph[crt][i][0]
            if dist[node] > value:
                dist[node] = value
                h.heappush(heap, (value, node))
            else:
                continue
    return [cnt, w]


for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [list() for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    cnt = 0
    ans = 0
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    answer = dijk(c, n)
    print(*answer)