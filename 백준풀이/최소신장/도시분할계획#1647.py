import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
p = [i for i in range(N + 1)]
def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        p[x] = p[y]

for _ in range(M):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: -x[2])

count = 1
answer = 0
maxx = 0

while count < N:
    a, b, w = edges.pop()

    if find(a) == find(b):
        continue
    else:
        union(a, b)
        answer += w
        maxx = max(w, maxx)
        count += 1

print(answer - maxx)
#
# edges = {i: {} for i in range(1, N + 1)}
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     if b not in edges[a] or c < edges[a][b] :
#             edges[a][b] = c
#     if a not in edges[b] or c < edges[b][a]:
#             edges[b][a] = c
#
# h_edges = []
# visit = [0] * (N + 1)
# crt = 1
# visit[crt] = 1
# for i in edges[crt]:
#     h.heappush(h_edges, [edges[crt][i], i])
# answer = 0
# count = 1
# maxx = 0
#
# while count < N:
#     w, next_ = h.heappop(h_edges)
#     if visit[next_] == 1:
#         continue
#     maxx = max(maxx, w)
#     answer += w
#     visit[next_] = 1
#     count += 1
#     for i in edges[next_]:
#         if visit[i] == 1:
#             continue
#         h.heappush(h_edges, [edges[next_][i], i])
#
# print(answer - maxx)