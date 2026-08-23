class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stk.append(ch)
            else:
                if len(stk) < 1:
                    return False

                if ch == ')':
                    if stk[-1] == '(':
                        stk.pop()
                    else:
                        return False
                elif ch == ']':
                    if stk[-1] == '[':
                        stk.pop()
                    else:
                        return False
                elif ch == '}':
                    if stk[-1] == '{':
                        stk.pop()
                    else:
                        return False
        
        if len(stk) == 0:
            return True
        else:
            return False