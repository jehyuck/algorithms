#덱 사용
from collections import deque as d

#입력
puzzles = ""
puzzle = ""
direction = [(0,1),(1,0),(-1,0),(0,-1)]
for _ in range(3):
    temp = input()
    temp = temp.replace(" ", "").replace("0", "9")
    puzzles += temp

visit_dict = dict()
visit_dict[puzzles] = 0
que = d([puzzles])


#bfs를 이용한 전체 탐색
#1. 방문dict에 첫 상태를 key:value "퍼즐상태":옮긴횟수 로 저장하고 큐에 넣는다.
# (key:1차원형태의 문자열)
#2. 큐에서 popleft하고 target상태와 일치하면 value값을 리턴한다.
#3. 아니면 사방으로 교체가능한 위치를 교체하고 큐와 dict에 추가한다.
#4. 모든 경우를 방문하면 종료되고 None이 반환된다.
#5. 결과에 맞게 출력한다.

def bfs():
    table = None
    while que:
        #2
        crt = que.popleft()

        if crt == "123456789":
            return visit_dict[crt]
        crt_zero = crt.find("9")
        crt_r, crt_c = divmod(crt_zero,3)

        #3 4방을 확인
        for i in direction:
            y, x = i
            next_r, next_c = crt_r + y, crt_c + x
            #4방중 갈수 있는곳
            if 0 <= next_r < 3 and 0 <= next_c < 3:
                change_idx = next_r*3 + next_c
                change_value = crt[change_idx]
                table = str.maketrans("9"+change_value, change_value+"9")
                temp = crt.translate(table)
                #3 방문여부 확인
                if temp not in visit_dict:
                    que.append(temp)
                    visit_dict[temp] = visit_dict[crt] + 1
    return None

#출력
result = bfs()

print(-1 if result == None else result)


"""
bfs를 이용한 전체탐색 문제
"""