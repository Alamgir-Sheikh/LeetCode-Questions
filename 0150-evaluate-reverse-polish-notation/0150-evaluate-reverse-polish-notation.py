class Solution:
    def evaluate(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        else:
            return num1 / num2
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operands = []
        ans = 0
        for el in tokens:
            if el not in "+-/*":
                operands.append(el)
            else:
                # print(operands)
                second = int(operands.pop())
                first = int(operands.pop())
                ans = self.evaluate(first, second, el)
                # print(f"First: {first}, Second: {second}, Ans: {ans}")
                operands.append(int(ans))
        # print(operands)
        return operands[0]