from tokens import TokenType, FieldTokens, BracketTokens, LogicalTokens, ComparisonTokens


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __str__(self):
        return f"Token({self.type_}, {self.value})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.type_ == other.type_ and self.value == other.value


class Tokenizer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
        self.char = self.text[self.pos]

    def next_token(self) -> Token:
        while self.char is not None and self.char.isspace():
            self._next_char()

        if self.char is None:
            return Token(TokenType.EOF, 'EOF')

        if self.char.isdigit():
            return Token(TokenType.INTEGER, self._get_int())

        if self.char in BracketTokens:
            token = Token(TokenType.BRACKET, self.char)
            self._next_char()
            return token

        token_value = self._get_value()

        if token_value in FieldTokens:
            return Token(TokenType.FIELD, token_value)

        if token_value in ComparisonTokens:
            return Token(TokenType.COMPARISON_OPERATOR, token_value)

        token_value = token_value.upper()

        if token_value in LogicalTokens:
            return Token(TokenType.LOGICAL_OPERATOR, token_value)

        raise SyntaxError(f"Syntax error, invalid token {token_value}")

    def _next_char(self) -> None:
        self.pos += 1
        self.char = self.text[self.pos] if self.pos < len(self.text) else None

    def _get_int(self) -> int:
        value = ''
        while self.char is not None and self.char.isdigit():
            value += self.char
            self._next_char()
        return int(value)

    def _get_value(self) -> str:
        value = ''
        while self.char is not None \
                and not self.char.isspace() \
                and not self.char.isdigit() \
                and self.char not in BracketTokens:
            value += self.char
            self._next_char()
        return value
