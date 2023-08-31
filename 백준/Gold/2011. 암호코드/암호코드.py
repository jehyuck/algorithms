import sys


def solution():
    str = input().rstrip()
    if str[0] == "0":
        return 0
    if len(str) == 1:
        return 1 if str != '0' else 0

    possible_tenth = "12"
    dp = [0] * (len(str) + 1)
    dp[0] = 1; dp[1] = 1;
    i = 2
    while i < len(dp):
        # print(i, str[i - 1], str[i - 2: i])
        if str[i - 1] == '0':
            if str[i - 2] not in possible_tenth:
                return 0
            dp[i] = dp[i - 2]
            if i + 1 < len(dp):
                dp[i + 1] = dp[i]
            i += 1
        else:
            dp[i] = (dp[i - 1] + (dp[i - 2] if int(str[i - 2 :  i]) <= 26 else 0)) % 1000000
        i += 1

    # print(dp)
    return dp[-1]


print(solution())