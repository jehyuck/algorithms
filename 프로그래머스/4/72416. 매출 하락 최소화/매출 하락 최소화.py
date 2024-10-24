inf = 3000000001

def makeTree(s, l):
    rtn = dict()
    for i in range(len(l)):
        a, b = l[i]
        key = (a, s[a - 1])
        if key not in rtn:
            rtn[key] = []
        rtn[key].append((b, s[b - 1]))
    return rtn


# 제일 밑에 팀은 나 자신 아니면 최솟값을 고르겠지
# 그 반환값을 받은 팀은 그 팀장을 고를 때와 우리팀의 최솟값을 고를때를 선택해야함.
# 나를 고른 값(부하의 2, 3중 큰 값), 말단 부하를 고른 값(부하의 2, 3), 부하 팀장을 고른 값(부하의 한개만 1 선택 나머지는 2, 3중 작은 값), 
# 다른 최솟값을 어떻게 고려하냐

def dfs(tim, node):
    global inf 
    
    n, s = node
    minLeafChild = inf
    minBossChild = inf
    minDiffChild = inf
    childValue = 0
    rtn = [s, inf, inf]
    child = tim[node]
    # print(node, child)
    for i in range(len(child)):
        c_node = child[i]
        cn, cs = c_node
        
        if c_node in tim:
            # 나를선택, 부하선택, 부하팀장을 선택
            dfs_rtn = dfs(tim, child[i])
            childChoice = min(dfs_rtn)
            childValue += childChoice
            minDiffChild = min(minDiffChild, dfs_rtn[0] - childChoice)
        else:
            minLeafChild = min(minLeafChild, cs)

    rtn[0] += childValue
    if minLeafChild != inf:
        rtn[1] = minLeafChild + childValue
    if minDiffChild != inf:
        rtn[2] = minDiffChild + childValue
    # print(node, rtn)
    return rtn

def solution(sales, links):
    answer = 0
    tims = makeTree(sales, links)
    # print(tims)
    rtn = dfs(tims, (1, sales[0]))
    # print(rtn)
    return min(rtn)

"""
4번째 예시
1 - 4 - 3 - 2
"""