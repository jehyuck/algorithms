import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
disset = list(range(M + 1))
query = tuple(map(int, input().split()))


def union(a, b):
    a = find(a)
    b = find(b)
    disset[a] = b

def find(a):
    if a == disset[a]:
        return a
    else:
        disset[a] = find(disset[a])
        return disset[a]

for i in range(len(query)):
    start = 0
    last = M - 1
    while start <= last:
        mid = (start + last) // 2

        if query[i] >= card[mid]:
            start = mid + 1
        else:
            last = mid - 1
    # print(minsuCard, query[i], start, last + 1)?=
    idx = find(start)
    print(card[idx])
    union(idx, idx + 1)
