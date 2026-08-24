class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num1 = stk.pop()
                num2 = stk.pop()
                if token == '+':
                    stk.append(num2 + num1)
                elif token == '-':
                    stk.append(num2 - num1)
                elif token == '*':
                    stk.append(num2 * num1)
                elif token == '/':
                    stk.append(int(num2 / num1))
            else:
                stk.append(int(token))

        return stk[0]
        