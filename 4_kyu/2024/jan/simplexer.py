"""
The Challenge

You'll need to implement a simple lexer type.
It should take in an input string through the constructor, and break it up into typed-tokens
(in python, C# and Java, you'll have to manage null/None input too, resulting in the same behavior than an empty string).

You'll need to implement the necessary methods (according to your language) to make the Simplexer object behave like an iterator.
Meaning that it returns a token (assuming one is available) object each time it a next (Current field in C#) method would be called.

If no tokens are available, an exception should be thrown (idealy: StopIteration in python, InvalidOperationException in C# and NoSuchElementException in Java).

Tokens are represented by Token objects, which define two properties as strings: text, and type. Constructor is Token(text, type).

C# Notes:

`Iterator` is an extension of `IEnumerator` with default implementations for `Reset()`,
`Dispose()` and `IEnumerator.Current` as these are not need to pass the challenge.
You only need to override `MoveNext()` and `Current { get; }`.

Token Types

There are 7 tokens types that your lexer will need to produce: identifier, string, integer, boolean, keyword, operator, and whitespace.
To create the token, you'd need to pass in the token value (the text) and the token type as strings,
so for example, a simple integer token could be created with new Token("1", "integer")
(Note: no default values or default constructor are provided, so use new Token("","") if you want a default Token object).

Token Grammar

Here's a table of the grammars for the various token types:

integer : Any sequence of one or more digits.

boolean : true or false.

string : Any sequence of characters surrounded by "double quotes".

operator : The characters +, -, *, /, %, (, ), and =.

keyword : The following are keywords: if, else, for, while, return, func, and break.

whitespace : Matches standard whitespace characters (space, newline, tab, etc.)
Consecutive whitespace characters should be matched together.

identifier : Any sequence of alphanumber characters, as well as underscore and dollar sign,
and which doesn't start with a digit. Make sure that keywords aren't matched as identifiers!
"""

class Simplexer:

    def __init__(self, expression):
        self.idx = 0
        token_types = {
            "true": "boolean", "false": "boolean", '"': "string",
            "0": "integer", "1": "integer", "2": "integer", "3": "integer",
            "4": "integer", "5": "integer", "6": "integer",
            "7": "integer", "8": "integer", "9": "integer",
            "+": "operator", "-": "operator", "*": "operator",
            "/": "operator", "%": "operator", "(": "operator",
            ")": "operator", "=": "operator",
            "if": "keyword", "else": "keyword", "for": "keyword", "while": "keyword",
            "return": "keyword", "func": "keyword", "break": "keyword",
            " ": "whitespace",
            "|alpha|": "identifier"
        }
        self.tokens = []
        while expression:
            for token_val, token_type in token_types.items():
                if token_type == "integer" and expression.isdigit():
                    self.tokens.append(Token(expression, token_type))
                    expression = None
                    break
                if token_type == "string" and expression.startswith('"') and expression.endswith('"'):
                    self.tokens.append(Token(expression, token_type))
                    expression = None
                    break
                if token_type == "whitespace" and expression.isspace():
                    self.tokens.append(Token(expression, token_type))
                    expression = None
                    break
                if expression.startswith(token_val):
                    self.tokens.append(Token(token_val, token_type))
                    expression = expression.replace(token_val, "", 1)
                    break
                if token_type == "identifier":
                    parts = expression.split()
                    if len(parts) > 1:
                        expression = " " + " ".join(parts[1:])
                    else:
                        expression = None
                    self.tokens.append(Token(parts[0], token_type))
                    break
    
    def __iter__(self):
        return self
                
    def __next__(self):
        try:
            item = self.tokens[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1
        return item
        
