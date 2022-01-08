#사용할 자료구조 queue가져오기
from collections import deque as d

#입력

N = int(input())
nums = sorted(list(map(int,input().split())))
X = int(input())

#정렬된 list에 투포인터를 이용한 정답 쌍 찾기
#1.start(0) end(length-1)로 2개의 포인터 설정
#2.두 포인터의 합이 target과 같으면 둘다 위치를 변경해준다.
#  위치변경이란 start의 경우 +1 end의 경우 -1
#3. target보다 작으면 start의 위치 변경
#4. target보다 크면 end의 위치 변경
#5. 두개의 위치가 같아지지면 종료

start = 0
end = len(nums)-1
answer = 0

#2--5
while start < end:

    temp = nums[start] + nums[end]

    #2
    if temp == X:
        answer += 1
        start += 1
        end -= 1
    # 3. target보다 작으면 start의 위치 변경
    elif temp < X:
        start += 1
    # 4. target보다 크면 end의 위치 변경
    else:
        end -= 1

print(answer)