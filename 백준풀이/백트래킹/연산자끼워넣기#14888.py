#입력
n = int(input())
num = list(map(int,input().split()))
oper = list(map(int,input().split()))
def plus(a,b):
    return a+b
def dev(a,b):
    if a < 0 or b < 0:
        a, b = abs(a),abs(b)
        if a < 0 and b < 0:
            return a//b
        return -(a//b)
    return a//b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b

operOder = ['+', '-', '*', '/']
expression = []

def makeEx(temp):
    if sum(oper) == 0:
        expression.append(temp.copy())
    for i in range(4):
        if oper[i] != 0:
            oper[i] -= 1
            temp.append(i)
            makeEx(temp)
            temp.pop()
            oper[i] += 1

makeEx([])
minV = float('inf')
maxV = -float('inf')
num.reverse()
for i in expression:
    numT = num.copy()
    for j in i:
        a = numT.pop()
        b = numT.pop()
        # print(numT,a,b,"-->",end=" ")
        if j == 0:
            numT.append(plus(a, b))
        elif j == 1:
            numT.append(sub(a, b))
        elif j == 2:
            numT.append(mult(a, b))
        elif j == 3:
            numT.append(dev(a, b))
        # print(numT)
    if minV > numT[0]:
        minV = numT[0]
    if maxV < numT[0]:
        maxV = numT[0]

print(maxV, minV, sep="\n")