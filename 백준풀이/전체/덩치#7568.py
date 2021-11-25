#입력받기
n = int(input())

#사람의 정보를 입력받을 list그릇
people = []

#입력받은 사람수 n을 가지고 그 수 만큼 입력 받는 반복문
for i in range(n):
    people.append([list(map(int,input().split(' '))),1])

#자신보다 체급이 높다면 등수를 1등 낮추는 모든 모든경우(n*n)를 탐색하는 반복문
for i in people:
    for j in people:
        if (i[0][0] < j[0][0]) and (i[0][1] < j[0][1]):
            i[1] += 1

#답안제출
print(' '.join(list(map(lambda x:str(x[1]),people))))

