#문제 수 입력받기
n = int(input())

#문제 입력받기
question = []
for i in range(n):
    question.append(int(input()))

#피보나치 호출수 담는 list
fiboR = [(1,0),(0,1)]

#문제 중 최댓값까지 피보나치 호출 수를 구한다.
for i in range(2,max(question) + 1):
    x1, y1 = fiboR[i-2]
    x2, y2 = fiboR[i-1]
    fiboR.append((x1+x2, y1+y2))

#출력
for i in question:
    print(*fiboR[i])