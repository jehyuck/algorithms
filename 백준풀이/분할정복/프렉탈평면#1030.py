import sys
sys.setrecursionlimit(10**9)
#입력
s, N, K, R1, R2, C1, C2 = map(int, input().split())

#가운데의 기준
first = (N-K)//2
last = first + K

#출력할 배열의 모든값을 0으로 초기화 해줌
rtn = [['0']*(C2-C1+1) for _ in range(R1, R2+1)]

#1.가운데면 1을 넣어줌
#   아니면 재귀
#       마지막 이면 first pat을 통해 1번을 재실행
#       아니면 return 으로 마무리
def find_black(R, C, r, c, subS):

    if subS == -1:
        return

    num = pow(N,subS)

    #몫을 현재값으로 설정, 나머지를 재귀문에 넣을 index
    #가운데가 아니라면 s-1의 경우의 프렉탈 평면에 머무르기 때문에
    #나머지가 s = S-1의 평면의 index가 된다.
    r, rr = divmod(r,num)
    c, cc = divmod(c,num)

    #만족한다면 그 값을 평행이동 해준 곳에 색칠
    if (r >= first and r < last) and (c >= first and c < last):
        rtn[R-R1][C-C1] = '1'
        return
    else:
        #s가 -1이 될 때까지 재귀
        find_black(R, C, rr, cc, subS - 1)
        return


#주어진 좌표에 대해 값을 구한다
for i in range(R1,R2 + 1):
    for j in range(C1, C2 + 1):
        find_black(i, j, i, j, s-1)

#출력
for i in rtn:
    print(''.join(i))


