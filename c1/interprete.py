import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitorTree import TreeVisitor
from ExprVisitorEval import EvalVisitor

visitorEval = EvalVisitor()
while True:
    input_stream = InputStream(input('>> '))
    lexer = ExprLexer(input_stream)

    token_stream = CommonTokenStream(lexer)
    parser = ExprParser(token_stream)
    tree = parser.root()

    a = visitorEval.visit(tree)
    if a is not None:
        print(a)
