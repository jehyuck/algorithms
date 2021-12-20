#입력 최적화
import sys

#입력
n = int(sys.stdin.readline())

#정답과 라인 입력받기
lines = []

#line들 입력
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    lines.append((x,y))

#lines를 정렬해 준다.
lines.sort(key= lambda x:x[0])

#lines를 한바퀴를 돈다.
#1. line 한개가 현재까지 라인과 겹치지 않으면 linelimit를 재설정 해준다.
#1-1. 현재까지의 길이를 answer에 더해준다.
#1-2. linelimit를 재설정 해준다.
#2.겹치면 limit를 update해주고 1을 반복한다.
answer = 0
s, e = lines[0]

for i in range(1,n):
    tx = lines[i][0]
    ty = lines[i][1]
    #2의 과정
    if e > tx:
        e = max(e, ty)
    #1의 과정
    else:
        answer += e - s
        s = tx
        e = ty
#마지막에 결정된 것은 합이 안된다 그래서 마지막에 해줘야한다.
print(answer + e - s)

"""
맞추기 위해 노력한것
1.처음에 변수e인 끝 값을 무조건 교체했다.
--> max를 사용해 더 교체가 필요한 경우만 교체함
시간 줄이려고 노력한것
1.입력식에서의 입력을 여러번 바꿔줌
--> append(list(map(int,sys.stdin.readline().split())))에서
-->  이것으로 바꿈 x,y = map(int,sys.stdin.readline().split())
                append((x,y)) list말고 tuple형식으로
2.정렬의 제약을 조금 더 줄여줌
--> sort()에서 --> sort(key)설정해줌
"""