class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

        def convert(date):
            m = int(date[:2])
            d = int(date[3:])
            return sum(months[:m-1]) + d

        AA = convert(arriveAlice)
        LA = convert(leaveAlice)
        AB = convert(arriveBob)
        LB = convert(leaveBob)

        entry = max(AA, AB)
        exit_day = min(LA, LB)

        return max(0, exit_day - entry + 1)