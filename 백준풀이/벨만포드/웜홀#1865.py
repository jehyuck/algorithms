import sys

input = sys.stdin.readline
T = int(input())
INF = 10e9


def bellman(node_num):
    dist[1] = 0
    for i in range(1, N + 1):
        for j in range(node_num):
            crt, rear, cost = edges[j]
            if dist[rear] > dist[crt] + cost:
                dist[rear] = dist[crt] + cost

                if i == N:
                    return 1
    return 0


for i in range(T):
    N, M, W = map(int, input().split())
    edges = []
    dist = [INF] * (N + 1)
    for j in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for j in range(W):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    is_infinity = bellman(2 * M + W)
    print("YES" if is_infinity else "NO")
