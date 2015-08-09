# Regular Expression


class Preprocessor:

    def __init__(self):
        pass

    def comment_remover(self, line):
        comments = []
        pair = 0
        comment = ''
        for c in line:
            if c == '(':
                pair += 1
            elif c == ')' and pair > 1:
                pair -= 1
            elif c == ')' and pair == 1:
                pair -= 1
                comment += c
                comments.append(comment)
                comment = ''
            if pair > 0:
                comment += c
        if pair != 0:
            raise NameError('Unmatched Parentheses')
        for comment in comments:
            line = ''.join(line.split(comment.strip())).strip()
        return line

    def preprocess(self, line):
        line = self.comment_remover(line)
        return line