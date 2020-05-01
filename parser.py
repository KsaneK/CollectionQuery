from abc import abstractmethod

from tokenizer import Tokenizer, Token
from tokens import TokenType, token_to_name


class AST:
    def __init__(self, token):
        self.token = token

    @abstractmethod
    def dumps(self, depth=0) -> str:
        ...

    @abstractmethod
    def evaluate(self, record):
        ...


class Operation(AST):
    def __init__(self, token, left_node: AST, right_node: AST):
        super().__init__(token)
        self.left_node = left_node
        self.right_node = right_node

    def dumps(self, depth=0):
        result = "\t" * depth + f"{token_to_name.get(self.token.value)} (\n"
        result += self.left_node.dumps(depth+1) + ",\n"
        result += self.right_node.dumps(depth+1) + "\n"
        result += "\t" * depth + ")"
        return result

    def evaluate(self, record):
        op = "==" if self.token.value == "=" else self.token.value.lower()
        return eval(f"{self.left_node.evaluate(record)} "
                    f"{op} "
                    f"{self.right_node.evaluate(record)}")


class Field(AST):
    def __init__(self, token):
        super().__init__(token)
        self.field = token.value

    def dumps(self, depth=0):
        out = "\t" * depth + self.field
        return out

    def evaluate(self, record):
        return getattr(record, self.field)


class Number(AST):
    def __init__(self, token):
        super().__init__(token)
        self.value = token.value

    def dumps(self, depth=0):
        return "\t" * depth + str(self.value)

    def evaluate(self, record):
        return self.value


class Parser:
    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer
        self.current_token = self.tokenizer.next_token()

    def parse(self) -> AST:
        ast = self._expr()
        if self.current_token.type_ != TokenType.EOF:
            raise SyntaxError(f"Unexpected token '{self.current_token.value}'")
        return ast

    def _expr(self):
        node = self._phrase()

        while self.current_token.type_ == TokenType.LOGICAL_OPERATOR \
                and self.current_token.value == 'OR':
            token = self.current_token
            self._next_token()
            node = Operation(token, node, self._phrase())

        return node

    def _phrase(self):
        node = self._term()

        while self.current_token.type_ == TokenType.LOGICAL_OPERATOR \
                and self.current_token.value == 'AND':
            token = self.current_token
            self._next_token()
            node = Operation(token, node, self._term())

        return node

    def _term(self):
        node = self._factor()

        while self.current_token.type_ == TokenType.COMPARISON_OPERATOR:
            token = self.current_token
            self._next_token()
            node = Operation(token, node, self._factor())

        return node

    def _factor(self):
        token = self.current_token
        if token.type_ == TokenType.BRACKET and token.value == '(':
            self._next_token()
            node = self._expr()
            self._next_token(expected=Token(type_=TokenType.BRACKET, value=')'))
            return node

        elif token.type_ == TokenType.INTEGER:
            self._next_token()
            return Number(token)

        elif token.type_ == TokenType.FIELD:
            self._next_token()
            return Field(token)

        raise SyntaxError("Logical and comparison operators require two operands.")

    def _next_token(self, expected=None):
        if expected and self.current_token != expected:
            raise SyntaxError(f"Error while parsing token {self.current_token.value}, "
                              f"expected {expected.value}")
        self.current_token = self.tokenizer.next_token()
