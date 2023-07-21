
def check_number(quest, answers):
    for i in range(len(answers)):
        q, s, b = answers[i]

        c_s, c_b = 0, 0
        for j in range(len(quest)):
            if quest[j] == q[j]:
                c_s += 1
            elif quest[j] in q:
                c_b += 1

        if c_s != s or c_b != b:
            return False

    return True


def dfs(f, crt_quest, visit, answers):
    if f == 3:
        if check_number(crt_quest, answers):
            return 1
        else:
            return 0

    rtn = 0
    for i in range(1, 10):
        if visit[i] : continue

        visit[i] = True
        crt_quest[f] = i
        rtn += dfs(f + 1, crt_quest, visit, answers)

        visit[i] = False

    return rtn

def solution():
    N = int(input())

    answers = []
    for _ in range(N):
        q, s, b = input().split()

        answers.append([list(map(int, list(q))), int(s), int(b)])

    answer = dfs(0, [0, 0, 0], [False] * 10, answers)
    return answer
print(solution())