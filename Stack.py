# Encapsulation: Information Hiding
class Stack:
    stack = None

    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def __getitem__(self, item):
        try:
            return self.stack[item]
        except:
            raise NameError('Stack Out of Range')

    def __setitem__(self, key, value):
        try:
            self.stack[key] = value
        except:
            raise NameError('Stack Out of Range')

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        else:
            raise NameError('Stack is Empty')

    # Readability
    def push(self, item):
        self.stack.append(item)

    def top(self):
        if not self.isempty():
            return self.stack[-1]
        else:
            raise NameError('Stack is Empty')

    def isempty(self):
        return not bool(len(self.stack))

    def remove(self, index):
        try:
            del self.stack[index]
            return True
        except:
            return False

    def count(self):
        return len(self.stack)
