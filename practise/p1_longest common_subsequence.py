def lcs(s1,s2,m,n,dp):
    if m==0 or n==0:
        return 0
    
    if dp[m][n]!=-1:
        return dp[m][n]
    
    if s1[m]==s2[n]:
    
     dp[m][n]= 1+lcs(s1,s2,m-1,n-1,dp)
     return dp[m][n]
    else:
        dp[m][n]=max(lcs(s1,s2,m-1,n,dp),lcs(s1,s2,m,n-1,dp))
        return dp[m][n]
    

# Example usage:
s1 = "ABCBDAB"
s2 = "BDCAB"
m=len(s1)
n=len(s2)
dp=[[-1 for i in range(n+1)] for j in range(m+1)]
print("Length of Longest Common Subsequence:", lcs(s1,s2,m-1,n-1,dp))
# Output: 4

# def lcs(s1, s2, m, n, dp):
#     if m == 0 or n == 0:
#         return 0
    
#     if dp[m][n] != -1:
#         return dp[m][n]
    
#     if s1[m - 1] == s2[n - 1]:
#         dp[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, dp)
#     else:
#         dp[m][n] = max(lcs(s1, s2, m - 1, n, dp), lcs(s1, s2, m, n - 1, dp))
    
#     return dp[m][n]

# # Example usage:
# s1 = "ABCBDAB"
# s2 = "BDCAB"
# m = len(s1)
# n = len(s2)
# dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
# print("Length of Longest Common Subsequence:", lcs(s1, s2, m, n, dp))
# # Output: 4
