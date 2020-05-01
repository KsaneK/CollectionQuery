# Collection Query

#### Requirements:
- _python 3.6 or newer_

Simple expression interpreter, which allow to filter collection by 8 fields (a - h)

The expression can consist of:
 - logical operators (and, or)
 - comparison operators (=, <, <=, >=, >, !=)
 - parenthesis
 - fields (a-h)
 - integers
 
 
#### Context-free grammar - BNF:

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
         |   integer
         |   a
         |   b
         |   c
         |   d
         |   e
         |   f
         |   g
         |   h
```

#### Usage:
Program accepts csv files with data. File path can be passed as argument to the program.  
To run interpreter run `python collection_query path/to/dataset.csv`  
Let's assume we have following data, where next values in a tuple are next fields from a to h:  
```
1,2,3,4,5,6,7,8
8,7,6,5,4,3,2,1
5,5,5,1,2,3,4,5
```
Query example:
```
query: a > 1 and a = b = c
AST:
AND (
    GT (
        a,
        1
    ),
    EQ (
        EQ (
            a,
            b
        ),
        c
    )
)
Press enter to continue...
Result:
Record(a=5, b=5, c=5, d=1, e=2, f=3, g=4, h=5)
1 record(s) returned
```