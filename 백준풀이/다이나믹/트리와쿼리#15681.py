#입력 최적화
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
#입력
n, r, q = map(int,input().split())

#입력2
# 연결관계를 표현
childs = [[] for _ in range(n+1)]
count = [0]*(n+1)

for i in range(n-1):
    a, b = map(int,input().split())
    childs[a].append(b)
    childs[b].append(a)

#dfs를 통해 자식노드들의 갯수 합을 기록

def dfs(p):
    count[p] = 1
    #방문안된 노드(부모노드)에 들어가 정점의 갯수를 센다.
    for i in childs[p]:
        if not count[i]:
            dfs(i)
            count[p] += count[i]

dfs(r)

#입력3
#문제를 입력
#문제에 해당하는 답을 출력
for i in range(q):
    que = int(input())
    print(count[que])