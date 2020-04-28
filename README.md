# **Collection Query**

Simple expression interpreter, which allow to filter collection by 8 fields (a - h)

The expression can consist of:
 - logical operators (and, or)
 - comparison operators (=, <, <=, >=, >, !=)
 - parenthesis
 
 
Context-free grammar - BNF:

```
<expr>   ::= <expr> OR <phrase>
         |   <phrase>

<phrase> ::= <phrase> AND <term>
         |   <term>

<term>   ::= <term> = <factor>
         |   <term> < <factor>
         |   <term> <= <factor>
         |   <term> >= <factor>
         |   <term> > <factor>
         |   <term> != <factor>
         |   <factor>

<factor> ::= ( <expression> )
         |   a
         |   b
         |   c
         |   d
         |   e
         |   f
         |   g
         |   h
```

Usage:  
let's assume we have following data, where next values in a tuple are next fields from a to h:  
```
data = [
    (1, 2, 3, 4, 5, 6, 7, 8),
    (8, 7, 6, 5, 4, 3, 2, 1),
    (5, 5, 5, 1, 2, 3, 4, 5)
]
```
Query example:
```
query: a > 1 and a = b = c
AST:
AND(
    GT(
        a,
        1
    ),
    EQ(
        a,
        EQ(
            B,
            C
        )
    )
)
Press any key to continue...

Output:
[
    (5, 5, 5, 1, 2, 3, 4, 5)
]
```