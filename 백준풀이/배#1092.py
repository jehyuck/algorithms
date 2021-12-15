#입력
n = int(input())
cranes = sorted(list(map(int,input().split())),reverse=True)

m = int(input())
boxes = sorted(map(int,input().split()), reverse=True)

#초별로 기록을한다.
#1. 무거운거부터 한개씩 옮긴다(불가능 하는 순간 break)
#2. 전부다 했다면 시간을 1초 늘려준다.
if boxes[0] > cranes[0]:
    print(-1)
else:
    count = 0
    while boxes:
        count += 1
        for i in cranes:
            for j in range(len(boxes)):
                if i >= boxes[j]:
                    del boxes[j]
                    break

    print(count)

"""
시간 더 단축 하는 방법 생각해 보기
"""