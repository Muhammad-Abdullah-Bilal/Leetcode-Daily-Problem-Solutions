class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        def area_difference(h):
            below = 0.0
            above = 0.0
            
            for x, y, l in squares:
                if h <= y:
                    above += l * l
                elif h >= y + l:
                    below += l * l
                else:
                    below += (h - y) * l
                    above += (y + l - h) * l
            
            return below - above
        
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)
        
        for _ in range(60): 
            mid = (low + high) / 2
            if area_difference(mid) < 0:
                low = mid
            else:
                high = mid
        
        return low