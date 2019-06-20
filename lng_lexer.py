from sly import Lexer


class IniLexer(Lexer):
    tokens = {PRINT, NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ}
    ignore = '\t '

    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    # Define tokens
    PRINT = r'P'
    IF = r'I'
    THEN = r'TH'
    ELSE = r'E'
    FUN = r'FN'
    FOR = r'F'
    TO = r'TO'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')


# Biar bisa di eksekusi
if __name__ == '__main__':
    lexer = IniLexer()
    env = {}
    while True:
        try:
            text = input('test > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
