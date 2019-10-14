from lng_lexer import IniLexer
from lng_parser import IniParser
from lng_interpreter import IniExecute
from sys import *

if __name__ == '__main__':
    lexer = IniLexer()
    parser = IniParser()
    env = {}
    if len(argv)>1:
        with open(argv[1], 'r') as file:
            text = file.readlines()
        for line in text:
            tree = parser.parse(lexer.tokenize(line))
            IniExecute(tree, env)
    else:
        while True:
            try:
                text = input('lng > ')
            except EOFError:
                break
            if text:
                tree = parser.parse(lexer.tokenize(text))
                IniExecute(tree, env)
