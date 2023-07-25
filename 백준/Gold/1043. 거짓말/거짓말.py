def solution():
    answer = 0

    n, m = map(int, input().split())
    knowList = set(input().split()[1:])
    parties = []

    for _ in range(m):
        parties.append(set(list(input().split())[1:]))

    for _ in range(m):
        for party in parties:
            if party & knowList:
                # print(party, knowList)
                knowList = knowList.union(party)

    for party in parties:
        if party & knowList:
            continue
        answer += 1
    # print(knowList)
    return answer

print(solution())