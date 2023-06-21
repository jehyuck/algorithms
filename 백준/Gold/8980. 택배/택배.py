from collections import deque as d

N, C = map(int, input().split())
M = int(input())


def solution(N, C, M):
    answer = 0
    boxes = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        boxes.append((a, b, c))
    boxes.sort(key=lambda x: [x[1], x[0], -x[2]])

    crt_box = 0
    crt_idx = 0
    crt_boxes = [0] * (N + 1)
    for i in range(M):
        a, b, c = boxes[i]
        if crt_box + c > C:
            for idx in range(crt_idx, a + 1):
                crt_box -= crt_boxes[idx]
                crt_boxes[idx] = 0
            crt_idx = a
            if crt_idx > a:
                continue
            temp_box = crt_box + c
            temp = 0
            if temp_box > C:
                temp = C - crt_box
                crt_boxes[b] += temp
                crt_box = C
            else:
                temp = c
                crt_box += c
                crt_boxes[b] += c
            answer += temp

        else:
            answer += c
            crt_box += c
            crt_boxes[b] += c

    return answer


print(solution(N, C, M))
