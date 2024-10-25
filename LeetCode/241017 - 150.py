# Evaluate Reverse Polish Notation
# Medium

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                value = int(eval(f"{operand_1}{token}{operand_2}"))
                stack.append(value)
            else:
                stack.append(token)
            #print(stack)

        return int(stack[0])

