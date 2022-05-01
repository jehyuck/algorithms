import sys
import heapq as hq

input = sys.stdin.readline
T = int(input())


def dijk(ss, nn, targett):
    dist = [float('inf')] * (nn + 1)
    dist[ss] = 0
    heap = [(0, ss)]
    while heap:
        w, crt = hq.heappop(heap)
        if dist[crt] < w:
            continue

        for i in range(len(graph[crt])):
            node = graph[crt][i][1]
            value = w + graph[crt][i][0]
            if dist[node] > value:
                dist[node] = value
                hq.heappush(heap, (value, node))
            else:
                continue
    return [(dist[i], i) for i in targett]


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [list() for _ in range(n + 1)]
    cnt = 0
    ans = 0
    waypointD = 0
    for i in range(m):
        a, b, d = map(int, input().split())
        graph[b].append((2 * d, a))
        graph[a].append((2 * d, b))
    for i in range(len(graph[g])):
        if graph[g][i][1] == h:
            waypointD = graph[g][i][0]
            graph[g].pop(i)
            graph[g].append((waypointD - 1, h))
            break
    for i in range(len(graph[h])):
        if graph[h][i][1] == g:
            graph[h].pop(i)
            graph[h].append((waypointD - 1, g))
            break
    target = [int(input()) for i in range(t)]

    answer = []
    for i in dijk(s, n, target):
        if i[0] % 2 == 1:
            answer.append(i[1])
    print(*sorted(answer))
