#입력 최적화
import sys
input = sys.stdin.readline

#입력
T = int(input())

#1. 전위회에서 한개씩 뽑는다.
#2. 그 값을 기준으로 중위순회에서 왼쪽 오른쪽의 subtree를 갈라낸다.
#3. 왼쪽 오른쪽 순서로 재귀방법으로 순회를 돌고 본인을 출력한다.
def makeTree(preorder, inorder):
    #아무값도 안들어오면 아무것도 하지 않는다.
    if len(preorder) == 0:
        return

    #leaf노드이면 ==  sub트리의 갯수가 단 1개이면 본인을 출력
    elif len(preorder) == 1:
        print(preorder[0], end=" ")
        return
    #sub트리의 갯수가 2개이면 중위 순회의 순서를 따라 출력한다.
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=" ")
        return

    fivot = preorder[0]
    fivotIdx = inorder.index(fivot)

    makeTree(preorder[1:fivotIdx+1], inorder[:fivotIdx])
    makeTree(preorder[fivotIdx+1:], inorder[fivotIdx+1:])
    #끝 sub트리들의 출력이 마무리되면 본인 노드를 출력
    print(fivot,end=" ")

for _ in range(T):
    N = int(input())
    makeTree(tuple(map(int, input().split())), tuple(map(int, input().split())))
    print()

"""
재귀를 이용한 분할정복
"""