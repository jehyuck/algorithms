import sys
input = sys.stdin.readline


def init(s, e, node):
    if s == e:
        tree[node] = ele[s]
    else:
        new_node = node * 2
        mid = (s + e) // 2
        init(s, mid, new_node)
        init(mid + 1, e, new_node + 1)
        tree[node] = (tree[new_node + 1] * tree[new_node]) % 1000000007


def update(s, e, node, idx, target):
    if idx < s or idx > e:
        return 1
    mid = (s + e) // 2

    if s != e:
        new_node = node * 2
        update(s, mid, new_node, idx, target)
        update(mid + 1, e, new_node + 1, idx, target)
        tree[node] = (tree[new_node + 1] * tree[new_node]) % 1000000007
    elif s == idx:
        tree[node] = target

def subMul(s, e, node, l, r):
    if l > e or s > r:
        return 1

    if l <= s and e <= r:
        return tree[node]

    new_node = node * 2
    mid = (s + e) // 2
    c = subMul(s, mid, new_node, l, r) * subMul(mid + 1, e, new_node + 1, l, r)

    return c % 1000000007


N, M, K = map(int,input().split())
ele = [0] * N
tree = [1] * N * 4
for i in range(N):
    ele[i] = int(input())

init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        update(0, N - 1, 1, b, c)
        ele[b] = c
    else:
        print(subMul(0, N - 1, 1, b - 1, c - 1))

# print(ele, tree, sep='\n')