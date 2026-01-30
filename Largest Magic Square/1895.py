from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        rowSum = [[0] * (n + 1) for _ in range(m)]
        colSum = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j]
                colSum[i + 1][j] = colSum[i][j] + grid[i][j]
        
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = rowSum[i][j + k] - rowSum[i][j]
                    valid = True
                    
                    for r in range(i, i + k):
                        if rowSum[r][j + k] - rowSum[r][j] != target:
                            valid = False
                            break
                    
                    if not valid:
                        continue
                    
                    for c in range(j, j + k):
                        if colSum[i + k][c] - colSum[i][c] != target:
                            valid = False
                            break
                    
                    if not valid:
                        continue
                    
                    diag1 = sum(grid[i + d][j + d] for d in range(k))
                    diag2 = sum(grid[i + d][j + k - 1 - d] for d in range(k))
                    
                    if diag1 == target and diag2 == target:
                        return k
        
        return 1
