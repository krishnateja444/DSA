class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            break_c = True
            while stack and stack[-1] > 0 and asteroids[i] < 0 :
                if abs(asteroids[i]) > stack[-1] :
                    stack.pop()
                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    break_c = False
                    break
                elif abs(asteroids[i]) < stack[-1] :
                    break_c = False
                    break
            if break_c :
                stack.append(asteroids[i])

        return stack

