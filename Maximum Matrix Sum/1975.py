class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_val = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                min_val = min(min_val, abs(val))
                if val < 0:
                    negative_count += 1

        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_val