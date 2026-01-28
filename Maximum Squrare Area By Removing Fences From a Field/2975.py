class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7
        
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])
        
        v_dist = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_dist.add(v[j] - v[i])
        
        common = h_dist & v_dist
        if not common:
            return -1
        
        side = max(common)
        return (side * side) % MOD
