import math
from decimal import Decimal as D
#입력
n, k = list(map(int,input().split()))

#입력2
dolls = list(map(int,input().split()))

#분산, 합과 평균 미리 구하기 그릇
V = [float('inf')]*n
sums = [0]
sSums = [0]

for i in range(n):
    sumNumbers = sums[i]+dolls[i]
    sumS = sSums[i] + dolls[i]**2
    sums.append(sumNumbers)
    sSums.append(sumS)

for i in range(0, n-k+1):
    crt = i+k

    while True:
        sumD = sums[crt] - sums[i]
        m = sumD/D(crt-i)
        sSum = sSums[crt] - sSums[i]

        vValue = sSum/D(crt-i) - m**2
        if vValue < V[i]:
            V[i] = vValue
        if crt == n:
            break
        crt += 1
print(math.sqrt(min(V)))
