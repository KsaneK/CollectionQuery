from parser import Parser
from tokenizer import Tokenizer

if __name__ == "__main__":
    expr = ''
    while expr != "!q":
        expr = input("query: ")
        if len(expr) == 0:
            continue
        try:
            tokenizer = Tokenizer(expr)
            parser = Parser(tokenizer)
            ast = parser.parse()
            print(ast.dumps())
        except SyntaxError as e:
            print(e.msg)

