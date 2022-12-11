# Generated from AGONY.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AGONYParser import AGONYParser
else:
    from AGONYParser import AGONYParser

# This class defines a complete listener for a parse tree produced by AGONYParser.
class AGONYListener(ParseTreeListener):

    # Enter a parse tree produced by AGONYParser#start.
    def enterStart(self, ctx:AGONYParser.StartContext):
        pass

    # Exit a parse tree produced by AGONYParser#start.
    def exitStart(self, ctx:AGONYParser.StartContext):
        pass


    # Enter a parse tree produced by AGONYParser#line.
    def enterLine(self, ctx:AGONYParser.LineContext):
        pass

    # Exit a parse tree produced by AGONYParser#line.
    def exitLine(self, ctx:AGONYParser.LineContext):
        pass


    # Enter a parse tree produced by AGONYParser#assignment.
    def enterAssignment(self, ctx:AGONYParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AGONYParser#assignment.
    def exitAssignment(self, ctx:AGONYParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AGONYParser#operation.
    def enterOperation(self, ctx:AGONYParser.OperationContext):
        pass

    # Exit a parse tree produced by AGONYParser#operation.
    def exitOperation(self, ctx:AGONYParser.OperationContext):
        pass


    # Enter a parse tree produced by AGONYParser#functiondef.
    def enterFunctiondef(self, ctx:AGONYParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by AGONYParser#functiondef.
    def exitFunctiondef(self, ctx:AGONYParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by AGONYParser#functioncall.
    def enterFunctioncall(self, ctx:AGONYParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by AGONYParser#functioncall.
    def exitFunctioncall(self, ctx:AGONYParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by AGONYParser#value.
    def enterValue(self, ctx:AGONYParser.ValueContext):
        pass

    # Exit a parse tree produced by AGONYParser#value.
    def exitValue(self, ctx:AGONYParser.ValueContext):
        pass


    # Enter a parse tree produced by AGONYParser#boolexpression.
    def enterBoolexpression(self, ctx:AGONYParser.BoolexpressionContext):
        pass

    # Exit a parse tree produced by AGONYParser#boolexpression.
    def exitBoolexpression(self, ctx:AGONYParser.BoolexpressionContext):
        pass


    # Enter a parse tree produced by AGONYParser#bool.
    def enterBool(self, ctx:AGONYParser.BoolContext):
        pass

    # Exit a parse tree produced by AGONYParser#bool.
    def exitBool(self, ctx:AGONYParser.BoolContext):
        pass


    # Enter a parse tree produced by AGONYParser#if.
    def enterIf(self, ctx:AGONYParser.IfContext):
        pass

    # Exit a parse tree produced by AGONYParser#if.
    def exitIf(self, ctx:AGONYParser.IfContext):
        pass


    # Enter a parse tree produced by AGONYParser#while.
    def enterWhile(self, ctx:AGONYParser.WhileContext):
        pass

    # Exit a parse tree produced by AGONYParser#while.
    def exitWhile(self, ctx:AGONYParser.WhileContext):
        pass


    # Enter a parse tree produced by AGONYParser#for.
    def enterFor(self, ctx:AGONYParser.ForContext):
        pass

    # Exit a parse tree produced by AGONYParser#for.
    def exitFor(self, ctx:AGONYParser.ForContext):
        pass



del AGONYParser