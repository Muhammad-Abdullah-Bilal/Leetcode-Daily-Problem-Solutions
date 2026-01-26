class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # start
            events.append((y + l, -1, x, x + l)) # end
        
        events.sort()
        
        def union_length(intervals):
            if not intervals:
                return 0
            intervals.sort()
            total = 0
            cur_start, cur_end = intervals[0]
            
            for s, e in intervals[1:]:
                if s > cur_end:
                    total += cur_end - cur_start
                    cur_start, cur_end = s, e
                else:
                    cur_end = max(cur_end, e)
            
            total += cur_end - cur_start
            return total
        
        active = []
        prev_y = events[0][0]
        area = 0
        slabs = []
        
        i = 0
        while i < len(events):
            y = events[i][0]
            height = y - prev_y
            
            width = union_length(active)
            if height > 0 and width > 0:
                slabs.append((prev_y, y, area, width))
                area += height * width
            
            while i < len(events) and events[i][0] == y:
                _, typ, xs, xe = events[i]
                if typ == 1:
                    active.append((xs, xe))
                else:
                    active.remove((xs, xe))
                i += 1
            
            prev_y = y
        
        target = area / 2
        
        for start_y, end_y, prev_area, width in slabs:
            slab_area = (end_y - start_y) * width
            if prev_area + slab_area >= target:
                return start_y + (target - prev_area) / width
        
        return 0.0