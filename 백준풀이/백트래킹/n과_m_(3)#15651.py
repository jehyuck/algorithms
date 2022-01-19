#입력받기
n, m = list(map(int,input().split(' ')))

rtn = []
lili = list(range(1, n + 1))

#dfs를 통해 새로운 list객체를 생성해 갯수가 만족 될 때까지 값을 추가해 준다.
def dfs(li, depth):

    #값이 0이 되면 전역함수 rtn에 값을 추가
    if depth == 0:
        rtn.append(li)
        return

    #모든 값에 대해 dfs 함수 호출
    for i in lili:
        copyLi = li.copy()
        copyLi.append(i)
        dfs(copyLi, depth - 1)

dfs([] , m)

#출력규칙을 지키기 위한 방법
for i in rtn:
    print(' '.join(map(str,i)))

"""
시간초를 줄여보기
1. dfs이기 때문에 조건 충족시 바로 출력하도록 하여 함수 호출 횟수
2. str과 list간의 구조 변화 없이 풀기
"""