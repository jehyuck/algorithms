#입력 최적화
import sys
import heapq as h

input = sys.stdin.readline

#입력
#프림 알고리즘과 힙을 이용한 최소 신장 트리
#1. 시작노드를 정하고 힙에 넣는다.
#2. 힙에서 노드 한개를 꺼낸다.
#2. 그 노드가 방문한 노드이면 넘어간다.
#2. 방문안했으면 방문표시하고, 총합에서 값을 빼주고 이어진 길중 방문 안한 곳을 넣는다.
#N과 M이 0이 들어올때까지 알고리즘을 반복한다.


M, N = map(int, input().split())
while not(N==0 and M==0):
    prim_dict = dict()
    # 1. 시작노드를 정하고 힙에 넣는다.
    heap = [[0,0]]
    visit = [False]*(M+1)
    answer = 0

    #연결리스트 만들기
    for _ in range(N):
        a,b,w = map(int, input().split())
        answer += w
        if a not in prim_dict:
            prim_dict[a] = {b:w}
        else:
            prim_dict[a][b] = w

        if b not in prim_dict:
            prim_dict[b] = {a:w}
        else:
            prim_dict[b][a] = w

    while heap:
        # 2. 힙에서 노드 한개를 꺼낸다.
        crt = h.heappop(heap)
        # 2. 그 노드가 방문한 노드이면 넘어간다.
        if visit[crt[1]]:
            continue

        # 2. 방문안했으면 방문표시하고, 총합에서 값을 빼주고 이어진 길중
        # 방문 안한 곳을 넣는다.
        visit[crt[1]] = True
        answer -= crt[0]
        for i in prim_dict[crt[1]].keys():
            if visit[i]:
                continue
            else:
                h.heappush(heap, [prim_dict[crt[1]][i], i])

    print(answer)
    M, N = map(int, input().split())

"""
프림알고리즘과 힙을 이용한 최소스패닝트리 
1. 크루스칼을 이용해 값을 구해보고 시간 비교해보기
"""