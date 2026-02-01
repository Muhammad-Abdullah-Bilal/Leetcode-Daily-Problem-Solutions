from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
                continue

            k = 0
            temp = num
            while temp & 1:
                k += 1
                temp >>= 1

            x = num - (1 << k) + (1 << (k - 1))
            ans.append(x)

        return ans
