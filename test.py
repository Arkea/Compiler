import test_lexer
import test_parser
import test_interpreter

if __name__ == '__main__':
    lexer = test_lexer.IniLexer()
    parser = test_parser.IniParser()
    env = {}
    while True:
        try:
            text = input('test > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            test_interpreter.IniExecute(tree, env)
