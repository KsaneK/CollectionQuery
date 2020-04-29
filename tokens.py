from enum import Enum


class TokenType(Enum):
    INTEGER = 1
    FIELD = 2
    LOGICAL_OPERATOR = 3
    COMPARISON_OPERATOR = 4
    BRACKET = 5
    EOF = 6


LogicalTokens = ['OR', 'AND']
ComparisonTokens = ['=', '<', '<=', '>', '>=', '!=']
FieldTokens = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
BracketTokens = ['(', ')']
