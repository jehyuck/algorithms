#입력 최적화
import sys
import heapq as h
input = sys.stdin.readline

#입력
n, m = int(input()), int(input())

#입력2(버스의 연결)
#다익스트라를 사용한다.
#1.인접그래프를 dict를 이용해 만든다.
#2.인접그래프를 이용해 시작점 n에서 다익스트라를 사용한다.
#3.n에서 방문 가능한 곳을 초기화 하고 heap에 넣는다.
#4.heap에서 pop하고 방문이 가능하면 방문 한다.
#4-1다시 방문이 가능한 곳을 값을 비교시 더 우월하면 거리값을 바꿔준 뒤 heap에 넣는다.
#5.전부다 방문 했으면 종료한다.

#인접 그래프와, 거리list
node_dict = dict()
dist = [float("inf")]*(n+1)

#1.방향 그래프 만들기
for _ in range(m):
    s, e, v = map(int,input().split())
    if s not in node_dict:
        node_dict[s] = {e: v}
    else:
        if e in node_dict[s]:
            node_dict[s][e] = min(node_dict[s][e], v)
        else:
            node_dict[s][e] = v


start, end = map(int,input().split())
dist[start] = 0
heap = [[0,start]]
route = [start]*(n+1)

#3,4
while heap:
    crt = h.heappop(heap)
    #방문했으면 하지 않는다.
    if crt[0] > dist[crt[1]]:
        continue

    if crt[1] == end:
        break


    #현재 위치에서 더 가까워 지는 값은 update
    if crt[1] not in node_dict:
        continue
    for i in node_dict[crt[1]]:
        #방문하지 않은것에 한해
        distance = crt[0] + node_dict[crt[1]][i]

        #현재위치에서 거리가 기존에 값보다 가까운 경우에서만
        if distance < dist[i]:
            dist[i] = distance
            h.heappush(heap, [distance,i])

            #경로를 기억
            route[i] = crt[1]

#도착점에서 시작점까지 역으로 탐색
crt = end
answer_route = [crt]
while crt != start:
    crt = route[crt]
    answer_route.append(crt)

print(dist[end])
print(len(answer_route))
print(*reversed(answer_route))

"""
다익스트라를 이용한 최단거리를 구하는 문제
1.공간과 시간을 아끼기위해 딕셔너리를 사용함
--> list로 간선을 구성할 시 겹치는 간선이 많을 경우 연산을 조금 더 하게된다.
    이를 막기 위해서 dict로 접근해 최솟값을 갱신하기 쉽게 해준다.
2.공간을 아끼기 위해 path 자체를 각 노드에 연결하는게 아니라 각각 노드에 부모값만 명시했다.
--> 모든 노드에 path를 넣지 않고 node에 연결된 부모만 입력하여
    역추적하는 방식을 선택했다.
"""