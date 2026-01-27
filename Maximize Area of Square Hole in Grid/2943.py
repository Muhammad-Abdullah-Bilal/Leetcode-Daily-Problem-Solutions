class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        
        def longest_consecutive(arr):
            arr.sort()
            longest = curr = 1
            
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    curr += 1
                    longest = max(longest, curr)
                else:
                    curr = 1
            return longest
        
        max_h = longest_consecutive(hBars)
        max_v = longest_consecutive(vBars)
        
        side = min(max_h, max_v) + 1
        return side * side