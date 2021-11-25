#입력받기
n, m = list(map(int,input().split(' ')))

rtn = []
lili = list(range(1, n + 1))

#dfs를 통해 곂치는 수가 없다면 새로운 list객체를 생성해 갯수가 만족 될 때까지 값을 추가해 준다.
def dfs(li, depth):

    #값이 0이 되면 전역함수 rtn에 값을 추가
    if depth == 0:
        rtn.append(li)
        return

    #값 추가가 가능할 때마다 바로 dfs 함수 호출
    for i in lili:
    #
        if i > li[-1] and i not in li:
            copyLi = li.copy()
            copyLi.append(i)
            dfs(copyLi, depth - 1)

#
dfs([0] , m)

#출력규칙을 지키기 위한 방법
#
for i in rtn:
    print(' '.join(map(str,i[1:])))

(1과 달라진점)dfs함수에 크기 비교 조건문을 추가해주었고
크기 비교를 위해 기본 리스트에 0을 넣어주었다. 
이로인해 출력문에도 1이후를 출력하는 슬라이싱을 추가하였다.