#입력
#n노드갯수, m간선갯수, v시작점
n, m, v = list(map(int,input().split()))

#방문을 한곳을 체크해 준다.(안하면 인접행렬을 다 탐색해야 하는 번거러움이 생김=O(N) visited = O(1))
visitedDfs = [0] + [False] * n
visitedDfs[v] = True

visitedBfs = [0] + [False] * n
visitedBfs[v] = True

#간선을 만들기
#인접행렬이 없는 노드에서 시작할 경우 에러가 날 수 있으므로 모든 노드를 생성해준다.
node_dict = {i : [] for i in range(1,n+1)}
for i in range(m):
    a,b = map(int,input().split())
    node_dict[a].append(b)
    node_dict[b].append(a)

for i in node_dict:
    node_dict[i] = sorted(node_dict[i])

#dfs먼저 실행
printOrder1 = []

#dfs본문
def dfs(crt):
    printOrder1.append(crt)
    #방문 가능하면 바로 방문하고 출력순서 기록
    for i in node_dict[crt]:

        if not visitedDfs[i]:
            visitedDfs[i] = True
            dfs(i)
dfs(v)
print(*printOrder1)

#bfs
bfs_queue = [v]
printOrder2 = []

#큐가 빌 때까지 반복
while bfs_queue:

    #계속 큐의 0에 위치한 값을 가져오고 가져올 때 마다 출력순서 기록
    crt = bfs_queue.pop(0)
    printOrder2.append(crt)

    #바로바로 방문여부를 기록해준다.
    for i in node_dict[crt]:

        if not visitedBfs[i]:
            visitedBfs[i] = True
            bfs_queue.append(i)

print(*printOrder2)