import sys

input = sys.stdin.readline


def init(N):
    return [i for i in range(N + 1)]


def union(p, a, b):
    pa = find(p, a)
    pb = find(p, b)

    if pa == pb:
        return True
    if pa < pb:
        p[pb] = pa
    else:
        p[pa] = pb
    return False


def find(p, a):
    if p[a] == a:
        return a

    p[a] = find(p, p[a])
    return find(p, p[a])


def solution(N, M):
    lines = [list(map(int, input().split())) for _ in range(M)]
    p = init(N)

    for i in range(M):
        a, b = lines[i]
        if union(p, a, b):
            return i + 1

    return 0

N, M = map(int, input().split())
print(solution(N, M))