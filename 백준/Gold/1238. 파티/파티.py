import sys
import heapq as h
from collections import defaultdict as dd


input = sys.stdin.readline
INF = 10000 * 1000 + 1

def dij(dp, adj, start, N):
    dp[start] = 0

    que = []

    h.heappush(que, (0, start))
    while que:
        value, node = h.heappop(que)

        for next_node, edge_length in adj[node]:
            temp = value + edge_length

            if temp < dp[next_node]:
                dp[next_node] = temp
                h.heappush(que, (temp, next_node))



def solution():
    answer = 0

    N, M, X = map(int, input().split())

    adj = dd(list)
    reversed_adj = dd(list)
    for i in range(M):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        reversed_adj[b].append((a, c))

    target_dp = [INF] * (N + 1)
    dij(target_dp, adj, X, N)
    reversed_target_dp = [INF] * (N + 1)
    dij(reversed_target_dp, reversed_adj, X, N)
    # print("target dp: ", target_dp)
    for i in range(1, N + 1):
        # dp = [INF] * (N + 1)
        # if i == X:
        #     continue
        # dij(dp, adj, i, N)
        # # print(dp)
        # print(reversed_target_dp, target_dp)
        answer = max(reversed_target_dp[i] + target_dp[i], answer)

    return answer

print(solution())
