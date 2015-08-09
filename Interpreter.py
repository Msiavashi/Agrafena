from Stack import *
from Preprocessor import *
from Tokenizer import *
import sys
# works like turing machine - or - pushdown automata

class Interpreter:
    stack = None
    preprocessor = None
    memory = None

    Keywords = [';', ':', 'DO', 'LOOP', 'BEGIN', 'UNTIL', 'EXPECT', 'LEAVE','DUP', 'SWAP', 'DROP', 'EMIT', 'MOD', 'KEY', 'DEPTH', 'ROLL', 'PICK']

    def __init__(self):
        self.stack = Stack()
        self.preprocessor = Preprocessor()
        self.memory = {}
        self.usedWrite = False

    def interact(self):
        while True:
            try:
                line = raw_input('>>> ')
                line = self.preprocessor.preprocess(line)
                self.process(line)
                if self.usedWrite:
                    sys.stdout.write('\n')
                    self.usedWrite = False
            except Exception as e:
                print e.message

    def push(self, statement):
        try:
            print '>>>', statement
            statement = self.preprocessor.preprocess(statement)
            self.process(statement)
            if self.usedWrite:
                    sys.stdout.write('\n')
                    self.usedWrite = False
        except Exception as e:
            print e.message

    def process(self, line, is_inside_until=False):
        statement = Tokenizer(line.strip(' ').strip('\n'), ' ')
        while statement.has_next():
            token = statement.next()
            if token in ['.', '.s', 'CR']:
                if token == '.':
                    sys.stdout.write(self.stack.pop())
                    self.usedWrite = True
                elif token == 'CR':
                    print
                else:
                    print self.stack
            elif token in self.memory:
                self.process(self.memory[token])
            elif token in ['DUP', '+', '-', '*', '/', 'SWAP', 'DROP', '<', '>', '<=', '>=', '=', 'EMIT', 'MOD', 'KEY',
                           'DEPTH', 'ROLL', 'PICK']:
                import Operators
                Operators.Op[token](self.stack)
            elif token == ':':
                self.function_definition(statement)
            elif token == 'IF':
                self.handle_if(statement)
            elif token == 'DO':
                self.do_loop(statement)
            elif token == 'BEGIN':
                self.until_loop(statement)
            elif token == 'LEAVE':
                if is_inside_until and self.stack.pop() != '0':
                    return False
            elif token == 'EXPECT':
                self.expect()
            elif token.startswith('."'):
                self.print_string(token, statement)
            elif token.isdigit():
                self.stack.push(token)
            elif token.strip() == '':
                pass
            else:
                raise NameError('Invalid Input: ' + token)
        return True

    def print_string(self, current_token, statement):
        if current_token.endswith('"'):
            print current_token[2:-1]
        else:
            # If the string contains white space then we need to connect its parts.
            string = current_token
            while statement.has_next():
                token = statement.next()
                string = string + ' ' + token
                if string.endswith('"'):
                    break
            print string[2:-1]

    def expect(self):
        count = int(self.stack.pop())
        string = ''
        while len(string) < count:
            string = string + raw_input('... ')
        for index in xrange(count):
            self.stack.push(string[index])

    def until_loop(self, statement):
        loop_body = ''
        pair = 1
        while statement.has_next():
            token = statement.next()
            if token == 'UNTIL' and pair == 1:
                pair -= 1
                break
            elif token == 'BEGIN':
                pair += 1
            elif token == 'UNTIL' and pair > 1:
                pair -= 1
            loop_body = loop_body + ' ' + token
        if pair != 0:
            raise NameError('Unmatched UNTIL Block')
        while True:
            # If not means if LEAVE occurred
            if not self.process(loop_body, is_inside_until=True):
                break
            elif self.stack.top() == '0':
                break

    def do_loop(self, statement):
        loop_body = ''
        pair = 1
        while statement.has_next():
            token = statement.next()
            if token == 'DO':
                pair += 1
            elif token == 'LOOP' and pair > 1:
                pair -= 1
            elif token == 'LOOP' and pair == 1:
                pair -= 1
                break
            loop_body = loop_body + ' ' + token
        if pair != 0:
            raise NameError('Unmatched DO Block')
        start = int(self.stack.pop())
        end = int(self.stack.pop())
        for i in xrange(start, end):
            self.process(loop_body)

    def handle_if(self, statement):
        condition = bool(int(self.stack.pop()))  #if the top was !=0 its True otherwise its False
        if_body = ''
        pair = 1
        if condition:
            while statement.has_next():
                token = statement.next()
                if token == 'IF':
                    pair += 1
                elif token == 'ELSE' and pair == 1:  # if pair was one ELSE is for the current if
                    break
                elif token == 'THEN' and pair > 1:  # means that the THEN is not for the currect if but in its body
                    pair -= 1
                elif token == 'THEN' and pair == 1:  # THEN is for the current if
                    pair -= 1
                    break
                if_body = if_body + ' ' + token
            if pair != 0:
                while statement.has_next():
                    token = statement.next()
                    if token == 'IF':  #if it was breaked with else it will ignore everything till THEN of the current if
                        pair += 1
                    elif token == 'THEN':
                        pair -= 1
                    elif token == 'THEN' and pair == 1:
                        pair -= 1
                        break
        else:
            collect = False
            while statement.has_next():
                token = statement.next()
                if token == 'IF':
                    pair += 1
                elif token == 'ELSE' and pair == 1:
                    collect = True
                    continue
                elif token == 'THEN' and pair > 1:
                    pair -= 1
                elif token == 'THEN' and pair == 1:
                    pair -= 1
                    break
                if collect:
                    if_body = if_body + ' ' + token
        if pair != 0:
            raise NameError('Unmatched IF Block')
        self.process(if_body)

    def function_definition(self, statement):
        name = statement.next()
        self.memory[name] = ''
        while statement.has_next():
            token = statement.next()
            # Return when we reach end of the function definition.
            if token == ';':
                return
            self.memory[name] = self.memory[name] + ' ' + token
        raise NameError('Syntax Error')
