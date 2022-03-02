N, r, c = map(int, input().split())

#분할정복
#1. 지금 좌표가 4분할 z에서 몇 번째에 해당하는지 구한다.
#1-1. 2^(크기)의 반(half) 으로 좌표의 몫으로 현재 위치를 구함(row가 몫이 있으면 ++2, col이있으면 ++1)
#1-2. 위에서 구한 위치 * 반(half)의 제곱(block) 으로 그 칸의 시작지점 값을 결과값에 더해준다.
#1-3. 1-1에서 구할때의 몫의 유무에 따라 half값을 빼준다.
#2. 1의 과정을 크기가 0이 될 때까지 반복한다.

def find_sol(crt, pos):
    if pos == 0:
        return 0
    half = 2 ** (pos - 1)
    block = half ** 2
    rr, cc = crt
    pos_r, pos_c = rr // half, cc // half
    position = pos_r * 2 + pos_c
    return position * block + find_sol((rr - pos_r * half, cc - pos_c * half), pos - 1)


print(find_sol((r, c), N))
