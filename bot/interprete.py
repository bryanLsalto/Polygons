import sys
sys.path.append("../")
from antlr4 import *
from c1.ExprLexer import ExprLexer
from c1.ExprParser import ExprParser
from c1.ExprVisitorTree import TreeVisitor
from c1.ExprVisitorEval import EvalVisitor

class interprete():
    
    def lector(visitor, command):
        
        inputstream = InputStream(command)
        lexer = ExprLexer(inputstream)
        tokenstream = CommonTokenStream(lexer)
        parser = ExprParser(tokenstream)
        tree = parser.root()
        return visitor.visit(tree)
