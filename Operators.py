class Operators:
    @staticmethod
    def ADD(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str(operand_1 + operand_2))

    @staticmethod
    def SUB(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str(operand_1 - operand_2))

    @staticmethod
    def MUL(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str(operand_1 * operand_2))

    @staticmethod
    def DIV(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str(operand_1 / operand_2))

    @staticmethod
    def MOD(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str(operand_1 % operand_2))

    @staticmethod
    def DROP(stack):
        stack.pop()

    @staticmethod
    def DUP(stack):
        stack.push(stack.top())

    @staticmethod  # does not need self (static method) python decorate feature
    def SWAP(stack):
        stack[-1], stack[-2] = stack[-2], stack[-1]

    @staticmethod
    def ADD(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str(operand_1 + operand_2))

    @staticmethod
    def GT(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str((operand_1 > operand_2) and 1 or 0))

    @staticmethod
    def LT(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str((operand_1 < operand_2) and 1 or 0))

    @staticmethod
    def GE(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str((operand_1 >= operand_2) and 1 or 0))

    @staticmethod
    def LE(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str((operand_1 <= operand_2) and 1 or 0))

    @staticmethod
    def EQU(stack):
        operand_2 = int(stack.pop())
        operand_1 = int(stack.pop())
        stack.push(str((operand_1 == operand_2) and 1 or 0))

    @staticmethod
    def PICK(stack):
        operand_1 = int(stack.pop())
        stack.push(stack[operand_1])  # Take a look at the pick implementation in the class 'Stack'
        stack.remove(operand_1)

    @staticmethod
    def ROLL(stack):
        operand_1 = int(stack.pop())
        stack.push(stack[operand_1])

    @staticmethod
    def DEPTH(stack):
        stack.push(str(stack.count()))

    @staticmethod
    def KEY(stack):
        operand_1 = stack.pop()
        stack.push(str(ord(operand_1)))

    @staticmethod
    def EMIT(stack):
        operand_1 = int(stack.pop())
        stack.push(chr(operand_1))


Op = {
    'DROP': Operators.DROP,
    'SWAP': Operators.SWAP,
    'KEY': Operators.KEY,
    'EMIT': Operators.EMIT,
    'DUP': Operators.DUP,
    'EMIT': Operators.EMIT,
    'KEY': Operators.KEY,
    '+': Operators.ADD,
    '-': Operators.SUB,
    '*': Operators.MUL,
    '/': Operators.DIV,
    'MOD': Operators.MOD,
    '=': Operators.EQU,
    '<': Operators.LT,
    '>': Operators.GT,
    '<=': Operators.LE,
    '>=': Operators.GE,
    'DEPTH': Operators.DEPTH,
    'ROLL': Operators.ROLL,
    'PICK': Operators.PICK
}