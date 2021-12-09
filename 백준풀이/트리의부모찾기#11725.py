#입력 최적화
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

#입력
n = int(input())



#부모노드 list
parents = [0]*(n+1)
parents[1] = 1
#방문여부와 연결 상태 list
link = [[] for _ in range(n+1)]


#입력2
#연결상태를 입력
for i in range(n-1):
    a, b = map(int, input().split())

    link[a].append(b)
    link[b].append(a)

#트리만들기dfs
def dfs(n):

    #방문 안했다면 부모노드를 기록하고 들어간다
    for i in link[n]:
        if parents[i] == 0:
            parents[i] = n
            dfs(i)

#1을 루트로 하는 트리 생성
dfs(1)

#출력
for i in parents[2:]:
    print(i)

"""
메모리가 많이 쓰임 bfs해보길
"""