from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    filename = "test.ape"
    with open(filename, "r") as file:
        lexer = Lexer(file)
        parser = Parser(lexer.tokens)
        interpreter = Interpreter(parser.AST)

        lexer.tokenizer()
        print(f"Tokens:\n{lexer.tokens}")
        
        parser.build_AST()
        print(f"AST:{parser.AST}")

        print("OUTPUT:")
        interpreter.run(parser.AST)


if __name__ == "__main__":
    main()
