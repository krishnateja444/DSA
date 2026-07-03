class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        def combine(l1,l2):
            if l1[1] >= l2[0]:
                return [l1[0], max(l1[1], l2[1])]
            return -1
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            temp = stack[-1]
            call = combine(temp,intervals[i])
            if call == -1 :
            
                stack.append(intervals[i])
            else :
                stack.pop()
                stack.append(call)
        return stack

            



        