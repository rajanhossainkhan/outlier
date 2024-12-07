def common(str1, str2):
    m, n = len(str1), len(str2)

    # create a 2D DP array
    dp = [[0] * (n+1) for _ in range(m+1)]

    #fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    #reconsturct lcs
    lcs = []
    i,j =  m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse()
    return ''.join(lcs), dp[m][n]

    return dp

str1 = "abcd"
str2 = "asdhjasdhj"

print(common(str1, str2))