import sys
from collections import deque as d
from collections import defaultdict as dd

input = sys.stdin.readline

INF = 10001
def first(w, K):
    rtn1 = INF
    rtn2 = 0
    alp_map = dd(d)

    for i in range(len(w)):
        if len(alp_map[w[i]]) < K:
            alp_map[w[i]].append(i)
        else:
            # print(w[i], alp_map[w[i]], i)
            rtn1 = min(rtn1, alp_map[w[i]][-1] - alp_map[w[i]][0] + 1)
            rtn2 = max(rtn2, alp_map[w[i]][-1] - alp_map[w[i]][0] + 1)
            alp_map[w[i]].append(i)
            alp_map[w[i]].popleft()

    for i in alp_map:
        if len(alp_map[i]) == K:
            rtn1 = min(rtn1, alp_map[i][-1] - alp_map[i][0] + 1)
            rtn2 = max(rtn2, alp_map[i][-1] - alp_map[i][0] + 1)

    # print(rtn1, rtn2)
    return rtn1, rtn2

def solution():
    T = int(input())
    answer = []

    for t in range(T):
        w = list(input().rstrip())
        K = int(input())
        answer1, answer2 = first(w, K)

        if answer1 == INF or answer2 == 0:
            answer.append("-1")
        else:
            answer.append(str(answer1) + " " + str(answer2))
        answer.append('\n')

    return ''.join(answer)
print(solution())