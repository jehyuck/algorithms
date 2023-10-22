import sys
from collections import defaultdict as dd

def pre_order(crt, tree, answer):
    answer.append(crt)

    if tree[crt][0] != '.':
        pre_order(tree[crt][0], tree, answer)
    if tree[crt][1] != '.':
        pre_order(tree[crt][1], tree, answer)


def mid_order(crt, tree, answer):

    if tree[crt][0] != '.':
        mid_order(tree[crt][0], tree, answer)
    answer.append(crt)

    if tree[crt][1] != '.':
        mid_order(tree[crt][1], tree, answer)

def post_order(crt, tree, answer):

    if tree[crt][0] != '.':
        post_order(tree[crt][0], tree, answer)
    if tree[crt][1] != '.':
        post_order(tree[crt][1], tree, answer)
    answer.append(crt)

def solution(N, tree):
    answer = [[], [], []]

    pre_order('A', tree, answer[0])
    mid_order('A', tree, answer[1])
    post_order('A', tree, answer[2])
    return answer


N = int(input())
tree = dd(lambda : {0 : '.', 1 : '.'})

for i in range(N):
    a, b, c = input().split()
    tree[a][0] = b
    tree[a][1] = c


arr = solution(N, tree)
arr_str = list(map(lambda x: ''.join(x), arr))
answer = '\n'.join(arr_str)
print(answer)