#입력
n = int(input())

m = int(input())

#목표값이 처음위치면 0번
if n == 100:
    print(0)
else:

    #입력값이 없을경우와 있을경우를 처리
    if m != 0:
        banished = set(map(int,input().split()))
    else:
        banished = set()

    #처음의 답을 +,- 버튼만 누를때로 설정
    answer = abs(n - 100)

    #모든 경우를 찾는다 그래서 100만까지 탐색
    for i in range(1000001):

        #채널을 분리해서 저장
        channel = set(map(int,str(i)))

        #채널과 고장난 버튼이 교집합이 존재하면 제외
        if channel & banished:
            continue
        else:
            # 존재하지 않으면 그 값을 현재의 값과 비교
            answer = min(answer, abs(n - i) + len(list(map(int,str(i)))))
    print(answer)


"""
1.반복문의 range 속의 값을 더 줄이는 방법을  찾아보기
2.다른 효율적인 방법 찾아보기
"""