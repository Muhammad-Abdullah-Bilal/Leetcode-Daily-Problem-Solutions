from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        INF = 10**15
        n = 26

        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]

        return total_cost
