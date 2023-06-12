G = int(input())
P = int(input())


def init(uf):
    for i in range(len(uf)):
        uf[i] = i


def union(uf, a):
    a = find(uf, a)
    b = find(uf, a - 1)
    uf[a] = b


def find(uf, n):
    p = uf[n]
    if n == p:
        return p
    uf[n] = find(uf, p)
    return uf[n]


def solution(g, p):
    uf = [0] * (g + 1)
    init(uf)

    for i in range(p):
        a = int(input())
        if find(uf, a) == 0:
            return i
        union(uf, a)
    return p


print(solution(G, P))
