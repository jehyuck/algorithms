import sys
input = sys.stdin.readline

N = int(input())

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

points = []
for _ in range(N):
    points.append(tuple(map(float, input().split())))

for i in range(N):
    x, y = points[i]
    for j in range(i + 1, N):
        xx, yy = points[j]
        edges.append((((x - xx) ** 2 + (y - yy) ** 2) ** (1 / 2), i, j))
edges.sort(key=lambda x: -x[0])

count = 1
answer = 0

while count < N:
    w, a, b = edges.pop()

    if find(a) == find(b):
        continue
    else:
        union(a, b)
        answer += w
        count += 1

print(answer)
