class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        new = [intervals[0]]
        for i in range(1,len(intervals)):
            if new[-1][1] >= intervals[i][0]:
                if new[-1][1] >= intervals[i][1] :
                    continue
                else :
                    new[-1][1] = intervals[i][1]
                    continue
            new.append(intervals[i])
        return new



            

        