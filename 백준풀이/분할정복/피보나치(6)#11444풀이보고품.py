##풀이 보고품
#입력
n = int(input())

#행렬곱
#매번 1000000007을 나눠준다.
def matx2(m1, m2):
    rtn = [[0]*2 for i in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                rtn[i][j] += m1[i][k] * m2[k][j]

    for i in range(2):
        for j in range(2):
            rtn[i][j] = rtn[i][j]%1000000007
    return rtn

#특별 알고리즘을 이용해서 푼다.
#[[fn+1,fn], [fn,fn-1]] = [[1,1],[1,0]]^n 이식을 통해 풀어서
##10830 행렬제곱을 응용해서 푼다
#n을 반복해서 나누어주면서 답에 접근한다.
def dfs(m):

    if m == 1:
        return [[1,1],[1,0]]

    a,b = divmod(m, 2)
    aa = dfs(a)
    if b == 0:
        return matx2(aa, aa)

    return matx2(matx2(aa,aa), [[1,1],[1,0]])

#출력
print(dfs(n)[0][1])
