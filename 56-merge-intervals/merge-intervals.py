class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        def merge(l1,l2):
            if l1[1] > l2[1] :
                return l1
            elif l1[1] >= l2[0] :
                return [l1[0],l2[1]]
            return -1
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            temp = stack.pop()
            call = merge(temp,intervals[i])
            if call == -1 :
                stack.append(temp)
                stack.append(intervals[i])
            else :
                stack.append(call)
        return stack

            



        