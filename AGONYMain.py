import sys
from antlr4 import *
from AGONYLexer import AGONYLexer
from AGONYParser import AGONYParser
from AGONYListener import AGONYListener

class AGONYPrintListener(AGONYListener):
    def enterCodeDIE(self, ctx):
        print("VALUE: %s" %ctx.ID())

def main(argv):
    input = FileStream(argv[1])
    lexer = AGONYLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AGONYParser(stream)
    tree = parser.start()
    printer = AGONYPrintListener()
    output = open("output.html","w")
    
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    
    print(tree.toStringTree(recog=parser))
    
    output.close()      
    
    
if __name__ == '__main__':
    main(sys.argv)