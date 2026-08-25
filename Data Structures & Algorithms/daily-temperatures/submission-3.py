class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):

            while len(stk) > 0 and (stk[-1])[0] < temperatures[i]:

                beforeTemp, beforeIndex = stk.pop()
                answer[beforeIndex] = i - beforeIndex
            
            stk.append( (temperatures[i], i) )
        
        return answer
            
