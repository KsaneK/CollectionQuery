import unittest

from tokens import TokenType
from tokenizer import Tokenizer, Token


class TestTokenizer(unittest.TestCase):
    def test_logical(self):
        expr = "a and b or c and d"
        tokenizer = Tokenizer(expr)
        self.assertEqual(Token(TokenType.FIELD, 'a'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.LOGICAL_OPERATOR, 'AND'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'b'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.LOGICAL_OPERATOR, 'OR'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'c'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.LOGICAL_OPERATOR, 'AND'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'd'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.EOF, 'EOF'), tokenizer.next_token())

    def test_mixed(self):
        expr = "a > 3 or b > c and (d > e or f > g)"
        tokenizer = Tokenizer(expr)
        self.assertEqual(Token(TokenType.FIELD, 'a'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.COMPARISON_OPERATOR, '>'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.INTEGER, 3), tokenizer.next_token())
        self.assertEqual(Token(TokenType.LOGICAL_OPERATOR, 'OR'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'b'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.COMPARISON_OPERATOR, '>'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'c'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.LOGICAL_OPERATOR, 'AND'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.BRACKET, '('), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'd'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.COMPARISON_OPERATOR, '>'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'e'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.LOGICAL_OPERATOR, 'OR'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'f'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.COMPARISON_OPERATOR, '>'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.FIELD, 'g'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.BRACKET, ')'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.EOF, 'EOF'), tokenizer.next_token())

    def test_exception(self):
        expr = "a > 3and3>5"
        tokenizer = Tokenizer(expr)
        self.assertEqual(Token(TokenType.FIELD, 'a'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.COMPARISON_OPERATOR, '>'), tokenizer.next_token())
        self.assertEqual(Token(TokenType.INTEGER, 3), tokenizer.next_token())
        self.assertRaises(SyntaxError, tokenizer.next_token)
