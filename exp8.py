def longest_common_subsequence_length(str1, str2):
    # Length of the input strings
    m, n = len(str1), len(str2)
    
    # Initialize a table to store the length of LCS for substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Length of LCS is stored at the bottom-right cell of the dp table
    return dp[m][n]

# Example usage:
str1 = "ABCBDAB"
str2 = "BDCAB"
print("Length of Longest Common Subsequence:", longest_common_subsequence_length(str1, str2))
