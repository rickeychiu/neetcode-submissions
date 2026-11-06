class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:

            if ch == '(':
                stk.append('(')
            if ch == '{':
                stk.append('{')
            if ch == '[':
                stk.append('[')
            

            if ch == ')':
                if len(stk) >= 1 and stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            if ch == '}':
                if len(stk) >= 1 and stk[-1] == '{':
                    stk.pop()
                else:
                    return False
            if ch == ']':
                if len(stk) >= 1 and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
        
        if len(stk) == 0: 
            return True
        else:
            return False
            
                