class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort() 
        merged = []

        for start, end in intervals:
            if len(merged) == 0:
                merged.append([start, end])
            else:
                lastStart = merged[-1][0]
                lastEnd = merged[-1][1]

                # overlap
                if start <= lastEnd:
                    merged[-1][1] = max(lastEnd, end)
                    merged[-1][0] = min(lastStart, start)
                else:
                    merged.append([start, end])
        
        return merged