import heapq as h


def init(N):
    return list(map(lambda x: x, range(N + 1)))


def union(p, a):
    a = find(p, a)
    b = find(p, a - 1)
    p[a] = b


def find(p, a):
    pa = p[a]
    if a == pa:
        return a
    p[a] = find(p, pa)
    return p[a]


def solution():
    answer = 0
    N = int(input())

    max_n = 0
    heap = []
    for i in range(N):
        a, b = map(int, input().split())
        max_n = max(max_n, b)
        h.heappush(heap, (-a, b))

    p = init(max_n)
    for _ in range(N):
        a, b = h.heappop(heap)
        if find(p, b) == 0:
            continue
        union(p, b)
        answer -= a

    return answer
print((solution()))