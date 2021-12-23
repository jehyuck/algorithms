# 우선순위 큐
import heapq as h
import sys
INF = sys.maxsize
input = sys.stdin.readline

# 입력
V, E = list(map(int, input().split()))
K = int(input())

dist[K] = 0
#간선들을 전부 탐색 시 끝낸다.
dist = [INF] * (V+1)
edges = [[] for i in range(V + 1)]
heap = []

for i in range(E):
    s, d, w = list(map(int, input().split()))
    # 우선순위 큐모듈이 0번째 값을 기준으로 정렬하므로 0에 가중치를 둔다.
    edges[s].append([w, d])

h.heappush(heap,[0,K])
while heap:
    w, crt = h.heappop(heap)

    #방문했을 시 안한다.
    if dist[crt] < w:
        continue
    #존재하는 간선을 전부 확인
    for i in edges[crt]:
        #간선을 선택하는게 더 짧은 값인지 확인
        new_w = dist[crt] + i[0]

        #더 짧으면 값을 초기화하고 그 값을 힙에 추가
        if dist[i[1]] > new_w:
            dist[i[1]] = new_w
            h.heappush(heap,[new_w, i[1]])

for i in dist[1:]:
    print('INF' if i == INF else i)