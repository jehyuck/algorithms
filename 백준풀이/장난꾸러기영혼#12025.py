#입력
num = list(input())
K = int(input())

#이진법을 이용한 순서 나열
#K-1을 이진법으로 바꿨을때 해당위치의 값이 0이면 작은수(1,2) 1이면 큰수(6,7)
#1. 1,2,6,7의 자리를 [1,2]의 리스트 형태로 바꿔준다. 만약 K가 2^(1267의 갯수) 보다 크면 01을 출력한다.
#2. K-1이 가리키는 이진수를 구한다.
#3. 이진수를 reversed하고 numlist의 뒤부터 0이면 1,2 1이면 6,7로 바꿔준다.

Kbin = list(bin(K-1)[2:])
numList = []
count = 0

for i in range(len(num)):
    if num[i] in ('1', '6'):
        count += 1
        numList.append(['1', '6'])
    elif num[i] in ('2', '7'):
        count += 1
        numList.append((['2', '7']))
    else:
        numList.append(num[i])

if 2**count < K or K <= 0:
    print(-1)
else:
    Kbin.reverse()
    crt = len(numList)-1
    for i in Kbin:
        while crt >= 0:
            if type(numList[crt]) == list:
                numList[crt] = numList[crt][int(i)]
                break
            else:
                crt -= 1
                continue
    for i in range(crt+1):
        if type(numList[i]) == list:
            numList[i] = numList[i][0]

    print(''.join(numList))

"""
순서를 나타내는 K를 비트마스킹 해서 K번째 수를 구하는 문제
기본적인 비트마스킹 문제
"""