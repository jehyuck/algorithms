import sys

input = sys.stdin.readline

def devide(paper, start, end, answer):
    r1, c1= start
    r2, c2 = end

    target = paper[r1][c1]
    escape = True
    for i in range(r1, r2):
        for j in range(c1, c2):
            if target != paper[i][j]:
                escape = False
                break
        if not escape:
            break

    if escape:
        answer[target] += 1
        return

    d = (end[0] - start[0]) // 3
    for i in range(r1, r2, d):
        for j in range(c1, c2, d):
            devide(paper, (i, j), (i + d, j + d), answer)





def solution(N, paper):
    answer = [0, 0, 0]
    temp = devide(paper, (0, 0), (N, N), answer)
    return answer

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

answer = solution(N, paper)

print(answer[-1])
print(answer[0])
print(answer[1])