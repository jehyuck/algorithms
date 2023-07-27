def solution():
    s = input()
    N = int(input())

    dp = [[0] * (len(s) + 1) for _ in range(26)]

    for target in range(26):
        for i in range(len(s)):
            # print(chr(target + 97), end=' ')
            alp = ord(s[i]) - 97
            if alp == target:
                # print(i, s[i], alp, target)
                dp[target][i + 1] = dp[target][i] + 1
            else:
                # print(i, s[i], alp, target)
                dp[target][i + 1] = dp[target][i]
    for i in range(N):
        a, l, r = input().split()

        l = int(l)
        r = int(r)

        alp_index = ord(a) - 97
        print(dp[alp_index][r + 1] - dp[alp_index][l])
    # print(*dp, sep='\n')

solution()
