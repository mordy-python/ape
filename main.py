from lexer import Lexer
from interpreter import Interpreter

with open("test.whsky", "r") as f:
    l = Lexer(f.readlines())
    i = Interpreter(l.tokens, {'name': 'momo'}, {'print': lambda x: [print(i) for i in x]})
    l.lex()
    tokens = l.tokens
    i.evaluate()