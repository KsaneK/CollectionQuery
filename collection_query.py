import sys

from dataset import sample_data, Record
from parser import Parser
from tokenizer import Tokenizer

dataset = []


def load_dataset():
    global dataset

    if len(sys.argv) == 2:
        file_dir = sys.argv[1]
        dataset = Record.from_csv(file_dir)
    else:
        dataset = sample_data

    print(f"Loaded {len(dataset)} records.\n")


def command_loop():
    while True:
        try:
            expr = input("query: ")
        except KeyboardInterrupt:
            exit(0)

        if expr == "!q":
            exit(0)

        if len(expr) == 0:
            continue

        try:
            ast = get_ast(expr)
            print_ast(ast)
            print_result(ast)
        except SyntaxError as e:
            print(e.msg)


def get_ast(expr):
    tokenizer = Tokenizer(expr)
    parser = Parser(tokenizer)
    return parser.parse()


def print_ast(ast):
    print("AST:")
    print(ast.dumps())
    print("Press enter to continue...", end='')
    input()


def print_result(ast):
    print("Result:")
    filtered_records = filter(lambda x: ast.evaluate(x), dataset)
    cnt = 0
    for i, record in enumerate(filtered_records, 1):
        print(record)
        cnt = i
    if cnt == 0:
        print("<Empty>")
    else:
        print(f"{cnt} record(s) returned")


if __name__ == "__main__":
    load_dataset()
    command_loop()
