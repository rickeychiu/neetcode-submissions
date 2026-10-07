class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        final = [0] * len(temperatures)
        stk = []
        # put into stk (temp, day)

        for i in range(len(temperatures)):

            while len(stk) > 0 and temperatures[i] > stk[-1][0]:
                final[stk[-1][1]] = i - stk[-1][1]
                stk.pop() 

            stk.append((temperatures[i], i))
        return final

