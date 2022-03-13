# Generated from Expr.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\2\3\2\3\3\3\3\3\3\5\3\23\n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3\61\n\3\r\3\16\3")
        buf.write("\62\3\3\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4H\n\4\3\4\3\4\3\4\7\4M\n")
        buf.write("\4\f\4\16\4P\13\4\3\4\2\3\6\5\2\4\6\2\3\3\2\26\27\2`\2")
        buf.write("\t\3\2\2\2\49\3\2\2\2\6G\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2")
        buf.write("\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\r\3\2\2\2")
        buf.write("\r\16\7\2\2\3\16\3\3\2\2\2\17\22\7\r\2\2\20\23\7\31\2")
        buf.write("\2\21\23\5\6\4\2\22\20\3\2\2\2\22\21\3\2\2\2\23:\3\2\2")
        buf.write("\2\24\25\7\16\2\2\25\26\7\32\2\2\26\27\7\3\2\2\27\30\7")
        buf.write("\4\2\2\30\31\7\f\2\2\31:\7\5\2\2\32\33\7\17\2\2\33:\5")
        buf.write("\6\4\2\34\35\7\20\2\2\35:\5\6\4\2\36\37\7\21\2\2\37:\5")
        buf.write("\6\4\2 !\7\22\2\2!:\5\6\4\2\"#\7\23\2\2#$\5\6\4\2$%\7")
        buf.write("\3\2\2%&\5\6\4\2&:\3\2\2\2\'(\7\24\2\2()\5\6\4\2)*\7\3")
        buf.write("\2\2*+\5\6\4\2+:\3\2\2\2,-\7\25\2\2-\60\7\31\2\2./\7\3")
        buf.write("\2\2/\61\7\32\2\2\60.\3\2\2\2\61\62\3\2\2\2\62\60\3\2")
        buf.write("\2\2\62\63\3\2\2\2\63:\3\2\2\2\64\65\7\30\2\2\65:\7\2")
        buf.write("\2\3\66\67\7\32\2\2\678\7\6\2\28:\5\6\4\29\17\3\2\2\2")
        buf.write("9\24\3\2\2\29\32\3\2\2\29\34\3\2\2\29\36\3\2\2\29 \3\2")
        buf.write("\2\29\"\3\2\2\29\'\3\2\2\29,\3\2\2\29\64\3\2\2\29\66\3")
        buf.write("\2\2\2:\5\3\2\2\2;<\b\4\1\2<=\7\7\2\2=H\5\6\4\b>?\7\b")
        buf.write("\2\2?@\5\6\4\2@A\7\t\2\2AH\3\2\2\2BC\7\n\2\2CH\7\33\2")
        buf.write("\2DH\7\32\2\2EF\7\13\2\2FH\7\35\2\2G;\3\2\2\2G>\3\2\2")
        buf.write("\2GB\3\2\2\2GD\3\2\2\2GE\3\2\2\2HN\3\2\2\2IJ\f\7\2\2J")
        buf.write("K\t\2\2\2KM\5\6\4\bLI\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3")
        buf.write("\2\2\2O\7\3\2\2\2PN\3\2\2\2\b\13\22\629GN")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'{'", "'}'", "':='", "'#'", "'('", 
                     "')'", "'['", "'!'", "<INVALID>", "'print'", "'color'", 
                     "'area'", "'perimeter'", "'vertices'", "'centroid'", 
                     "'equal'", "'inside'", "'draw'", "'*'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COLORES", "PRINT", "COLOR", 
                      "AREA", "PERIMETER", "VERTICES", "CENTROID", "EQUAL", 
                      "INSIDE", "DRAW", "INTERSECT", "UNION", "LINE_COMMENT", 
                      "STRING", "ID", "NUMEROS", "POINT", "NUM", "FLOAT", 
                      "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_oper = 2

    ruleNames =  [ "root", "expr", "oper" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    COLORES=10
    PRINT=11
    COLOR=12
    AREA=13
    PERIMETER=14
    VERTICES=15
    CENTROID=16
    EQUAL=17
    INSIDE=18
    DRAW=19
    INTERSECT=20
    UNION=21
    LINE_COMMENT=22
    STRING=23
    ID=24
    NUMEROS=25
    POINT=26
    NUM=27
    FLOAT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.expr()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.PRINT) | (1 << ExprParser.COLOR) | (1 << ExprParser.AREA) | (1 << ExprParser.PERIMETER) | (1 << ExprParser.VERTICES) | (1 << ExprParser.CENTROID) | (1 << ExprParser.EQUAL) | (1 << ExprParser.INSIDE) | (1 << ExprParser.DRAW) | (1 << ExprParser.LINE_COMMENT) | (1 << ExprParser.ID))) != 0)):
                    break

            self.state = 11
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def oper(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.OperContext)
            else:
                return self.getTypedRuleContext(ExprParser.OperContext,i)


        def COLOR(self):
            return self.getToken(ExprParser.COLOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def COLORES(self):
            return self.getToken(ExprParser.COLORES, 0)

        def AREA(self):
            return self.getToken(ExprParser.AREA, 0)

        def PERIMETER(self):
            return self.getToken(ExprParser.PERIMETER, 0)

        def VERTICES(self):
            return self.getToken(ExprParser.VERTICES, 0)

        def CENTROID(self):
            return self.getToken(ExprParser.CENTROID, 0)

        def EQUAL(self):
            return self.getToken(ExprParser.EQUAL, 0)

        def INSIDE(self):
            return self.getToken(ExprParser.INSIDE, 0)

        def DRAW(self):
            return self.getToken(ExprParser.DRAW, 0)

        def LINE_COMMENT(self):
            return self.getToken(ExprParser.LINE_COMMENT, 0)

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.PRINT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(ExprParser.PRINT)
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ExprParser.STRING]:
                    self.state = 14
                    self.match(ExprParser.STRING)
                    pass
                elif token in [ExprParser.T__4, ExprParser.T__5, ExprParser.T__7, ExprParser.T__8, ExprParser.ID]:
                    self.state = 15
                    self.oper(0)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [ExprParser.COLOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(ExprParser.COLOR)
                self.state = 19
                self.match(ExprParser.ID)
                self.state = 20
                self.match(ExprParser.T__0)
                self.state = 21
                self.match(ExprParser.T__1)
                self.state = 22
                self.match(ExprParser.COLORES)
                self.state = 23
                self.match(ExprParser.T__2)
                pass
            elif token in [ExprParser.AREA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(ExprParser.AREA)
                self.state = 25
                self.oper(0)
                pass
            elif token in [ExprParser.PERIMETER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(ExprParser.PERIMETER)
                self.state = 27
                self.oper(0)
                pass
            elif token in [ExprParser.VERTICES]:
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.match(ExprParser.VERTICES)
                self.state = 29
                self.oper(0)
                pass
            elif token in [ExprParser.CENTROID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.match(ExprParser.CENTROID)
                self.state = 31
                self.oper(0)
                pass
            elif token in [ExprParser.EQUAL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 32
                self.match(ExprParser.EQUAL)
                self.state = 33
                self.oper(0)
                self.state = 34
                self.match(ExprParser.T__0)
                self.state = 35
                self.oper(0)
                pass
            elif token in [ExprParser.INSIDE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 37
                self.match(ExprParser.INSIDE)
                self.state = 38
                self.oper(0)
                self.state = 39
                self.match(ExprParser.T__0)
                self.state = 40
                self.oper(0)
                pass
            elif token in [ExprParser.DRAW]:
                self.enterOuterAlt(localctx, 9)
                self.state = 42
                self.match(ExprParser.DRAW)
                self.state = 43
                self.match(ExprParser.STRING)
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 44
                    self.match(ExprParser.T__0)
                    self.state = 45
                    self.match(ExprParser.ID)
                    self.state = 48 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ExprParser.T__0):
                        break

                pass
            elif token in [ExprParser.LINE_COMMENT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 50
                self.match(ExprParser.LINE_COMMENT)
                self.state = 51
                self.match(ExprParser.EOF)
                pass
            elif token in [ExprParser.ID]:
                self.enterOuterAlt(localctx, 11)
                self.state = 52
                self.match(ExprParser.ID)
                self.state = 53
                self.match(ExprParser.T__3)
                self.state = 54
                self.oper(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oper(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.OperContext)
            else:
                return self.getTypedRuleContext(ExprParser.OperContext,i)


        def NUMEROS(self):
            return self.getToken(ExprParser.NUMEROS, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def INTERSECT(self):
            return self.getToken(ExprParser.INTERSECT, 0)

        def UNION(self):
            return self.getToken(ExprParser.UNION, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_oper

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOper" ):
                return visitor.visitOper(self)
            else:
                return visitor.visitChildren(self)



    def oper(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.OperContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_oper, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.T__4]:
                self.state = 58
                self.match(ExprParser.T__4)
                self.state = 59
                self.oper(6)
                pass
            elif token in [ExprParser.T__5]:
                self.state = 60
                self.match(ExprParser.T__5)
                self.state = 61
                self.oper(0)
                self.state = 62
                self.match(ExprParser.T__6)
                pass
            elif token in [ExprParser.T__7]:
                self.state = 64
                self.match(ExprParser.T__7)
                self.state = 65
                self.match(ExprParser.NUMEROS)
                pass
            elif token in [ExprParser.ID]:
                self.state = 66
                self.match(ExprParser.ID)
                pass
            elif token in [ExprParser.T__8]:
                self.state = 67
                self.match(ExprParser.T__8)
                self.state = 68
                self.match(ExprParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.OperContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_oper)
                    self.state = 71
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 72
                    _la = self._input.LA(1)
                    if not(_la==ExprParser.INTERSECT or _la==ExprParser.UNION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 73
                    self.oper(6) 
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.oper_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def oper_sempred(self, localctx:OperContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




