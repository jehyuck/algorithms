from itertools import combinations as c
#입력
n, k = map(int, input().split())

#예외처리
if k < 5:
    print(0)
else:
    #입력 2
    appear_letter = set()

    words_list = []
    antatica = set(list("antatica"))
    #주어진 단어들을 set으로 기억하고
    #등장한 글자의 갯수가 글자갯수제한인 k를 넘어가면 미리 제외한다.
    #antatica는 무조건 들어가므로 미리 빼주어서 단어 list에 넣어준다.
    #등장한 단어들을 appear_letter 구해준다.
    for _ in range(n):
        wordset = set(list(input()))
        appear_letter |= wordset
        if len(wordset) > k:
            continue
        else:
            words_list.append(wordset - antatica)

    #등장한 글자들들 중에서 기본단어인 antstica의 글자들을 빼준다.
    #이 글자들로 만들 수 있는 배열의 크기가(k-5)인 모든 조합을 구한다.
    #k-5인 이유 배울수 있는 글자의 갯수 - 꼭 배워야 하는 글자 수(antatica)
    appear_letter -= antatica

    #배운 글자 조합들을 전부다 배울 수 있는 단어들과 비교한다.
    #1. 글자 조합을 하나 고른다.
    #2. 모든 배울 수 있는 단어에 대해 배울 수 있으면 count += 1
    #3. 모든 글자 조합에 대해 1,2를 반복하고 가장 큰 count를 찾는다.
    empty_set = set()
    max_count = 0
    #min을 사용해야 k-5가 appear_letter 보다 큰 예외를 처리할 수 있다.
    letter_combi = map(set,c(appear_letter,min(k-5,len(appear_letter))))
    for i in letter_combi:
        count = 0
        for j in words_list:
            if j-i == empty_set:
                count += 1

        if count > max_count:
            max_count = count

    #가장 큰 count 출력
    print(max_count)

"""
1.등장할 수 있는 모든 글자의 수(최대 21)에서 글자수 제한이 10인 경우
  length가 10인 집합이 3백5십만개가 생긴다. 여기서 단어가 50개인 경우
  1천개가 훨씬 넘는 반복횟수를 견뎌야하므로 다른 방법도 생각해보기.

2.https://www.acmicpc.net/source/36304201 참고 
"""