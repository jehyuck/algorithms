import sys

input = sys.stdin.readline
N, M = map(int, input().split())

edges = []
dist = [float('inf')] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
def bellman_ford(start):
    dist[start] = 0

    for i in range(1, N + 1):
        for j in range(M):
            crt, rear, cost = edges[j]
            if dist[crt] != float('inf') and dist[rear] > dist[crt] + cost:
                dist[rear] = dist[crt] + cost

                if i == N:
                    return 1
    return 0

is_cycle = bellman_ford(1)
if is_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])
