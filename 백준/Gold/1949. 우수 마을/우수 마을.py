from collections import defaultdict as dd
import sys

sys.setrecursionlimit(10**5)
N = int(input())

people = [0]
people.extend(list(map(int, input().split())))
adj_dict = dd(list)

for i in range(N - 1):
    a, b = map(int, input().split())

    adj_dict[a].append(b)
    adj_dict[b].append(a)

answer = 0
visit = [False] * (N + 1)


def dfs(crt, prev, dic: dd, peo_value):
    rtn = [peo_value[crt], 0, 0]
    if len(dic[crt]) == 1 and dic[crt][0] == prev:
        return rtn

    all_out = True
    all_out_min = 1000000000
    for i in range(len(dic[crt])):
        if dic[crt][i] == prev: continue

        a, b, c = dfs(dic[crt][i], crt, dic, peo_value)
        rtn[0] += max(b, c)
        rtn[1] += max(b, c)
        rtn[2] += max(a, c)
    return rtn


# 현재노드, dict, visit, 현재 답
answer = dfs(1, 0, adj_dict, people)

print(max(answer))