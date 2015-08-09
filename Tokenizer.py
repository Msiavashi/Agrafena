class Tokenizer:
    tokens = []

    def __init__(self, line, delimiter):
        self.tokens = line.split(delimiter)

    def next(self):
        token = self.tokens[0]
        del self.tokens[0]
        return token

    def has_next(self):
        return bool(len(self.tokens))