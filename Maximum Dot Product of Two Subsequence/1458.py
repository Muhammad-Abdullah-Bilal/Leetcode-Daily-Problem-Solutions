class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**9
        
        dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = nums1[i] * nums2[j]
                dp[i][j] = max(
                    product,                     # start new subsequence
                    product + dp[i + 1][j + 1],  # extend subsequence
                    dp[i + 1][j],                # skip nums1[i]
                    dp[i][j + 1]                 # skip nums2[j]
                )
        
        return dp[0][0]