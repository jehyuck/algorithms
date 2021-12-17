#입력
n, selects = map(int, input().split())

#입력2
rects = []
rects_area = []
#사각형 입력의 4개의 좌표를 구한다.
for i in range(n):
    rects.append(list(map(int,input().split())))
    rects_area.append((rects[-1][2] - rects[-1][0])*(rects[-1][3] - rects[-1][1]))
#두 사각형이 겹치면 넓이를 안겹치면 0을 반환하는 함수
def intersect_calculator(r1,r2):
    #r2을 기준으로
    #왼쪽으로 벗어남
    rtn = [0,0,0,0]

    if r1[0] > r2[2]:
        return rtn
    #위로 벗어남
    if r1[3] < r2[1]:
        return rtn
    #오른쪽으로 벗어남
    if r1[2] < r2[0]:
        return rtn
    #아래로 벗어남
    if r1[1] > r2[3]:
        return rtn
    #결과의 밑변과 높이를 구한다.
    rtn[0] = max(r1[0],r2[0])
    rtn[1] = max(r1[1],r2[1])
    rtn[2] = min(r1[2],r2[2])
    rtn[3] = min(r1[3],r2[3])
    #겹친 부분의 넓이를 반환한다.
    return rtn

#넓이 구하기 위한 과정
#1. 모든 겹치는 부분을 원본 사각형 기준으로 구해준다.
#2. 구한 사각형들을 전부 빼는데 이 과정에서
#3. 모든 겹치는 사각형들끼리 겹치는 부분을 더해준다.(빼야하는 부분이 중복되서 빼지기 때문에)
#4. 그 다음에 겹치는 사각형의 넓이들을 빼준다.
inter_rect = [[] for _ in range(n)]
for i in range(n):
    for j in range(0,i):
        #겹치는 부분을 다 구해준다.
        inter_rect[j].append(intersect_calculator(rects[i],rects[j]))

#3번과정
print(inter_rect)
for i in range(len(inter_rect)):
    for j in range(len(inter_rect[i])):
        for k in range(j):
            inter_inter_rect = intersect_calculator(inter_rect[i][j],inter_rect[i][k])
            print(i, inter_inter_rect)
            rects_area[i] += (inter_inter_rect[2] - inter_inter_rect[0]) * (inter_inter_rect[3] - inter_inter_rect[1])
#4번과정
for i in range(len(inter_rect)):
    for j in range(len(inter_rect[i])):
        rects_area[i] -= (inter_rect[i][j][2] - inter_rect[i][j][0]) * (inter_rect[i][j][3] - inter_rect[i][j][1])

#번호를 매겨주고 넓이와 번호순으로 정렬한다.
for i in range(n):
    rects_area[i] = [rects_area[i],i+1]
print(rects_area)
#넓이는 큰것을 기준으로 index는 작은것을 기준으로 정렬한다.
rects_area.sort(key=lambda x: [x[0],-x[1]], reverse=True)

#출력
#k값 많큼의 큰것을 기준으로 가져온 것을 index만 가져와 그 값을 정렬해 준다.
print_index = sorted(list(map(lambda x: x[1], rects_area[:selects])))

print(*print_index)

"""
아직 실패함
1. 겹치는 부분을 손봐야한다.
2. 3번과정에서 덧셈이 잘못됨
"""