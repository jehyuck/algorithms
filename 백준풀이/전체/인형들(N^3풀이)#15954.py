#입력
n, k = list(map(int,input().split()))

#입력2
dolls = list(map(int,input().split()))

#분산 그릇
V = [float('inf')]*n

for i in range(n-k+1):
    dollList = dolls[i:i+k]
    crt = i+k
    sumD = sum(dollList)

    while True:
        m = sumD/(crt-i)
        vValue = sum(map(lambda x: (x-m)**2, dollList))/(crt-i)

        if vValue < V[i]:
            V[i] = vValue
        if crt == n:
            break
        sumD += dolls[crt]
        dollList.append(dolls[crt])
        crt += 1
print((min(V))**(1/2))