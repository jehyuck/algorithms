#입력
n, m = list(map(int, input().split()))

#행렬 곱 함수
def matx2(m1, m2):
    rtn = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rtn[i][j] += m1[i][k] * m2[k][j]

    return rtn

#행렬 입력 단위행렬 , 본행렬, 본행렬 제곱
mat = [list(map(int,input().split())) for i in range(n)]
matM= [mat]
matM.append(matx2(matM[-1], mat));

#단위행렬
I = [[1 if i == j else 0 for j in range(n)]for i in range(n)]

# 값의 반을 구해 제곱해 주는 형태로
# 분할정복으로(a^(2*n) = (미리구한 값)a^n * (복사)a^n) 재귀를 이용한다.
# m = 50인 경우 50번의 횟수가 9번으로 줄어든다.
def dfs(m):
    if m == 0:
        return I
    if m == 1:
        return matM[0]
    if m == 2:
        return matM[1]

    a, b = divmod(m, 2)
    aa = dfs(a)
    
    #값이 너무 커지는 것을 방지해서 매 곱마다 1000으로 나머지 연산을 해준다.
    #1000보다 자리수가 더 커도 뒤의 세자리 곱은 항상 동일하다.
    #값이 커져서 실행시간이 길어지는 것을 방지
    #(23123'123' * 8849564'654') % 1000 == (123*654) % 1000
    for i in range(len(aa)):
        aa[i] = list(map(lambda x: x%1000,aa[i]))
    if b == 0:
        return matx2(aa,aa)
    else:
        return matx2(matx2(aa,aa), dfs(b))

answer = dfs(m)

#라인 별로 띄어쓰기를 해서 출력
for i in answer:
    print(*list(map(lambda x: x%1000,i)))
