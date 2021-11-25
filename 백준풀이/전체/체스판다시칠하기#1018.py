#입력받기
n, m = list(map(int,input().split()))

#엇갈린 체스판을 입력받기
board = []
for i in range(n):
    board.append(input())

#왼쪽위에 뭐가 오느냐에 따라 2가지 패턴을 만듦
pattern1 = ['WBWBWBWB','BWBWBWBW']
pattern2 = ['BWBWBWBW','WBWBWBWB']

#모든 시작점에서 두가지 패턴을 전부 확인

#패턴 모든 시작점에 대해서 패턴 1과 2를 가지고 비교한 최솟값을 구함
def counting(x,y):
    i = x
    count1 = 0
    count2 = 0

    while i < x+8:
        j = y
        while j < y+8:
            if pattern1[(i-x)%2][j-y] != board[i][j]:
                count1 += 1
            if pattern2[(i-x)%2][j-y] != board[i][j]:
                count2 += 1
            j += 1
        i+= 1
    return min(count1,count2)

order = []

#모든 이용가능한 시작점을 구한다.
for i in range(n):
    if i > n - 8:
        break
    for j in range(m):
        if j <= m - 8:
            order.append((i,j))
        else:
            break

#최솟값을 구하고 출력한다.
countMin = float('inf')

for i in order:
    countMin = min(countMin,counting(*i))

print(countMin)

