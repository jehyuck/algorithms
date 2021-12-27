#입력
n = int(input())

#입력을 정렬하고, 그리디를 이용해 풀이
#1.정렬된 배열에서 i번째 요소를 고른다.
#2.합의 초기값을 1로 설정하고, i를 합에 더하고 다음 i+1과 크기 비교를 한다.
#2-1. 합이 다음 배열보다 크면 answer = sorted[i+1] + sum 하고 i를 1더한다.
#2-2. 합이 다음배열보다 작으면 answer를 출력 반복을 종료
#3. 1과 2를 반복

#입력을 정렬 sum을 1로 설정
weights = sorted(list(map(int,input().split())))
answer = 1

#2
for i in range(n):
    #2-1
    if weights[i] <= answer:
        answer += weights[i]
    #2-2
    else:
        break

#출력
print(answer)

"""
#정렬한 후 그리디한 방법을 생각하는 문제
1.그리디는 따로 연습을 해야겠다는 생각을함.
--> 우선 다른 알고리즘을 많이 하고 시간이 나면 따로 해야겠다.
"""