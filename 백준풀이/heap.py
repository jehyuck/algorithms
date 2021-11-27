
#힙을 초기화
def makeHeap(li):
    rtn = [0] + [float('inf')]*len(li)
    for i in li:
        insertH(rtn,i)

    return rtn

#힙에 요소 삽입
def insertH(li, e):

    li[0] += 1
    li[li[0]] = e
    e_index = li[0]

    while e_index != 1 and li[e_index] < li[int(e_index/2)]:
        p_index = int(e_index/2)
        temp = li[p_index]
        li[p_index] = e
        li[e_index] = temp
        e_index = p_index

#힙에서 요소를 빼기
def deleteH(li):
    rtn = li[1]; li[1] = li[li[0]]; li[li[0]] = float('inf')
    li[0] -= 1

    if li[0] == 1:
        return rtn

    elif li[0] == 2:
        if li[1] > li[2]:
            temp = li[1]
            li[1] = li[2]
            li[2] = temp
        return rtn
    parent = 1
    child = 2

    while child + 1 <= li[0]:
        print(child)

        if child < li[0] and li[child] > li[child + 1]:
            child += 1

        if li[child] > li[parent]:
            return rtn

        temp = li[child]
        li[child] = li[parent]
        li[parent] = temp
        parent = child
        child *= 2

    return rtn
