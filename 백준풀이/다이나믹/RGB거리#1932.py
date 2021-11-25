#입력
n = int(input())

#가중치 입력받기
RGB_list = []
for i in range(n):
    RGB_list.append(list(map(int,input().split())))

#최솟값 동적계획법할 list
RGB_min = [RGB_list[0]]

#모든 집들에 대해서
for i in range(1,n):
    R, G, B = RGB_list[i]
    r,g,b = RGB_min[i-1]

    #집의 최소 색들에 대해 각각 최솟값이 되는 경우로 초기화 해준다.
    R = min(R+g, R+b)
    G = min(G+r, G+b)
    B = min(B+r, B+g)
    RGB_min.append([R,G,B])

print(min(RGB_min[-1]))