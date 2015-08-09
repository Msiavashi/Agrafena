from code import InteractiveConsole


class Console:
    def __init__(self, statements):
        self.console = InteractiveConsole()
        self.run(statements)

    def run(self, statements):
        self.push('from Interpreter import *')
        self.push('interpreter = Interpreter()')
        for statement in statements.split('\n'):
            if statement != '':
                self.push("interpreter.push('" + statement.strip() + "')")

    def push(self, statement):
        self.console.push(statement)