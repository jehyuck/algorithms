#트리, bfs
#입력
n = int(input())

#입력2
parents = list(map(int, input().split(' ')))
cutTarget = int(input())

#노드 제거 함수
def cutNode(node):
    parents[node] = None
    for i in range(len(parents)):

        if parents[i] == node:
            cutNode(i)

#적용하기
answer = 0
if parents[cutTarget] != -1:
    cutNode(cutTarget)
    for i in range(n):
        if parents[i] != None and i not in parents:
            answer += 1
print(answer)