#문제입력
n = int(input())

question = []
for i in range(n):
    question.append(int(input()))

S = [1, 1, 1]
#3개이전과 2개이전의 합을 i로 초기화
for i in range(3, max(question) + 1):
    x = S[i - 3]
    y = S[i - 2]
    S.append(x + y)

#출력
for i in question:
    print(S[i - 1])
