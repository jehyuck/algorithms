#입력받기
n = int(input())

#변수선언
relation = []
startList = []
answer = float('inf')
for i in range(n):
    relation.append(list(map(int,input().split())))

#dfs 함수
def dfs(start, sumV):
    minV = float('inf')

    #한팀은 추가될때마다 계속 더해준다.
    startV = sumV
    for i in startList:
        startV += relation[i][start] + relation[start][i]

    #만약 10:10으로 나눠지면 값을 return 해준다
    if len(startList) == int(n/2):
        #link팀도 구함
        link = [i for i in range(n) if i not in startList]
        linkV = 0
        for i in link:
            for j in link:
                linkV += relation[i][j]
        #차이 값을 리턴
        return abs(startV - linkV)

    #조합이기 때문에 들어온 값부터 n까지
    for i in range(start+1, n):
        startList.append(i)
        minV = min(minV,dfs(i, startV))
        startList.pop()
    #끝에 구한 최솟값을 리턴
    return minV

#모든 첫번째 값에서
for i in range(0,int(n/2)+1):
    startList.append(i)
    answer = min(answer,dfs(i,0))
    startList.pop()

print(answer)