class Calculator:
    """
    how to come up with this solution in 30 minutes
    """
    def get_priority(self, sign):
        if sign in '*/':
            return 2
        else:
            return 1

    def to_number(self, s):
        res = 0
        for d in s:
            res = int(d) + res*10
        return res

    def operate(self, a, b, sign):
        if sign == "+":
            return a+b
        elif sign == "-":
            return a-b
        elif sign == "*":
            return a*b
        elif sign == "/":
            return a//b


    def calculate(self, s):
        operator_stack = []
        operand_stack = []
        value = ''
        for char in s:
            if char == ' ':
                continue
            if char in '0123456789':
                value += char
            else:
                if value:
                    operand_stack.append(
                        self.to_number(value)
                    )
                    value = ''
                if char in '+-*/':
                    while operator_stack and self.get_priority(operator_stack[-1]) > self.get_priority(char):
                        a = operand_stack.pop()
                        b = operand_stack.pop()
                        operand_stack.append(
                            self.operate(a, b, char)
                        )
                    operator_stack.append(char)
                elif char == '(':
                    operator_stack.append(char)
                elif char == ')':
                    while operator_stack and operator_stack[-1] not in '()':
                        a = operand_stack.pop()
                        b = operand_stack.pop()
                        sign = operator_stack.pop()
                        operand_stack.append(
                            self.operate(a, b, sign)
                        )
                    operator_stack.pop()

        if value:
            operand_stack.append(int(value))

        while operator_stack:
            sign = operator_stack.pop()
            a= operand_stack.pop()
            b=operand_stack.pop()
            operand_stack.append(
                self.operate(a,b,sign)
            )
        return operand_stack[-1]

c = Calculator()
r = c.calculate('(11+2)*33')
print(r)



