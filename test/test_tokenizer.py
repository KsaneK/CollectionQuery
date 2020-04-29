import unittest

from tokens import TokenType
from tokenizer import Tokenizer, Token


class TestTokenizer(unittest.TestCase):
    def test_logical(self):
        expr = "a and b or c and d"
        tokenizer = Tokenizer(expr)
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'a'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.LOGICAL_OPERATOR, 'AND'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'b'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.LOGICAL_OPERATOR, 'OR'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'c'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.LOGICAL_OPERATOR, 'AND'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'd'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.EOF, 'EOF'))

    def test_mixed(self):
        expr = "a > 3 or b > c and (d > e or f > g)"
        tokenizer = Tokenizer(expr)
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'a'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.COMPARISON_OPERATOR, '>'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.INTEGER, 3))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.LOGICAL_OPERATOR, 'OR'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'b'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.COMPARISON_OPERATOR, '>'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'c'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.LOGICAL_OPERATOR, 'AND'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.BRACKET, '('))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'd'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.COMPARISON_OPERATOR, '>'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'e'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.LOGICAL_OPERATOR, 'OR'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'f'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.COMPARISON_OPERATOR, '>'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.FIELD, 'g'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.BRACKET, ')'))
        self.assertEqual(tokenizer.next_token(), Token(TokenType.EOF, 'EOF'))
