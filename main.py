from lexer import Lexer

with open('test.whsky', 'r') as f:
    l = Lexer(f.readlines())
    l.lex()
    print('\n'.join(map(str, l.tokens)))