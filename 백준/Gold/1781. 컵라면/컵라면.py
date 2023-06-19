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

    p = init(N)

    heap = []
    for i in range(N):
        a, b = map(int, input().split())
        h.heappush(heap, (-b, a))

    for _ in range(N):
        b, a = h.heappop(heap)
        if find(p, a) == 0:
            continue
        union(p, a)
        answer -= b

    return answer
print((solution()))