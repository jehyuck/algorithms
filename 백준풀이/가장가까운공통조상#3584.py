#입력 최적화
import sys
input = sys.stdin.readline

#입력
t = int(input())

#NCA구하는 함수
def find_NCA():
    #노드의 갯수입력과 트리 선언
    n = int(input())
    tree = [0]*(n+1)

    #입력에 대해 모든 노드에 부모값을 입력함
    for _ in range(n-1):
        a, b = map(int,input().split())
        tree[b] = a

    #공통조상을 찾을 노드를 입력
    node1, node2 = map(int,input().split())
    #노드의 조상을 본인을 포함해 넣는다(list)
    node1_parents = []
    crt = node1
    while crt != 0:
        node1_parents.append(crt)
        crt = tree[crt]

    #노드2의 부모를 본인을 포함해 넣는다(set)
    #set인 이유: set의 in 연산자가 list 보다 빠르기 때문에
    node2_parents = set()
    crt = node2
    while crt != 0:
        node2_parents.add(crt)
        crt = tree[crt]


    for i in node1_parents:
        if i in node2_parents:
            return i

for i in range(t):
    print(find_NCA())
