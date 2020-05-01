import unittest

from dataset import Record
from parser import Parser
from tokenizer import Tokenizer


class TestParser(unittest.TestCase):
    def test_ast(self):
        expr = "a and b or c and d > 5"
        tokenizer = Tokenizer(expr)
        parser = Parser(tokenizer)
        ast = parser.parse()
        self.assertEqual('OR', ast.token.value)
        self.assertEqual('AND', ast.left_node.token.value)
        self.assertEqual('AND', ast.right_node.token.value)

        self.assertEqual('a', ast.left_node.left_node.token.value)
        self.assertEqual('b', ast.left_node.right_node.token.value)

        self.assertEqual('c', ast.right_node.left_node.token.value)

        self.assertEqual('>', ast.right_node.right_node.token.value)

        self.assertEqual('d', ast.right_node.right_node.left_node.token.value)
        self.assertEqual(5, ast.right_node.right_node.right_node.token.value)

    def test_unexpected_token(self):
        expr = "a > 3 and b = 5 ("
        tokenizer = Tokenizer(expr)
        parser = Parser(tokenizer)
        self.assertRaises(SyntaxError, parser.parse)

    def test_evaluate(self):
        dataset = [
            Record(1, 2, 3, 4, 5, 6, 7, 8),
            Record(8, 7, 6, 5, 4, 3, 2, 1),
            Record(5, 5, 5, 1, 2, 3, 9, 8)
        ]
        expr = "a > 3 and b=c or h=8"
        tokenizer = Tokenizer(expr)
        parser = Parser(tokenizer)
        ast = parser.parse()
        self.assertEqual(True, ast.evaluate(dataset[0]))
        self.assertEqual(False, ast.evaluate(dataset[1]))
        self.assertEqual(True, ast.evaluate(dataset[2]))
