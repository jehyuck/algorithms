#문제입력
n = int(input())

#피보나치 초깃값 입력
fibo = [1,2]


#피보나치 동적계획법
for i in range(2,n):
    x = fibo[i-2]
    y = fibo[i-1]
    fibo.append((x+y)%15746)

#답 출력
print(fibo[n-1])