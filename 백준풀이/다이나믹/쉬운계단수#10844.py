#입력
n = int(input())

#자릿수의 갯수
n_count = [0,1,1,1,1,1,1,1,1,1]
tempCount = [0]*10
#0과 1은 1개씩 있고 나머지는 2배씩 늘어난다.
for i in range(2,n+1):
    tempCount = [0,0,0,0,0,0,0,0,0,0]

    tempCount[0] = n_count[1]
    tempCount[9] = n_count[8]
    for i in range(1,9):
        tempCount[i] = n_count[i-1] + n_count[i + 1]

    n_count = tempCount
#출력
print(sum(n_count)%1000000000)