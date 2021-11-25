#풀이 보고 품 다시 생각해보기

#입력
n = int(input())

#입력2 (와인의 양)
wineVolume = []
d = [0]*n
for i in range(n):
    wineVolume.append(int(input()))


#dp를 이용한다.
d[0] = wineVolume[0]

#3 이하일 때에 조건문을 통해 예외 처리를 해준다.
if n > 1:
    d[1] = wineVolume[0] + wineVolume[1]
if n > 2:
    d[2] = max(d[1], wineVolume[0] + wineVolume[2], wineVolume[1] + wineVolume[2])

#앞의 3가지 경우와 자신과 대비 했을 때의 조건들로 max를 정해준다.
for i in range(3, n):
    d[i] = max(d[i-1], d[i-2] + wineVolume[i], d[i-3] + wineVolume[i] + wineVolume[i-1])

print(d[-1])