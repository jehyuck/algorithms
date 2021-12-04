# 효율적인 입력을 위해
import sys
input = sys.stdin.readline

#입력
V, E = list(map(int,input().split()))

#입력2 간선들
edges = []
for i in range(E):
    a, b, w = list(map(int,input().split()))
    edges.append([w,a,b])

edges.sort()
#작은 것부터 조건을 따지며 추가한다.
#조건
#1. 가장작고
#2. 그래프를 만들지 않는다.
#   (union 리스트의 값이 같지 않다 == 부모가 다르다)
#3. 간선갯수가 n-1이 되면 탈출

edges_Num = 0
sums = 0
union = [i for i in range(V+1)]

def unionSet(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        union[a] = b
    else:
        union[b] = a

def find(a):
    if a == union[a]:
        return a
    union[a] = find(union[a])
    return union[a]

for i in edges:
    w, a, b = i

    #set에 a,b를 추가해도 집합 길이가 변하지 않는다면 추가하지 않음
    if find(a) != find(b):
        unionSet(a,b)
        sums += w

print(sums)
