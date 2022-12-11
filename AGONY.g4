grammar AGONY;
/*
 * Parser Rules
 */
 
//open source tool for handling indentation in antlr4
//https://github.com/yshavit/antlr-denter


 tokens { INDENT, DEDENT }


@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from AGONYParser import AGONYParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: AGONYLexer = lexer

    def pull_token(self):
        return super(AGONYLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NL, AGONYParser.INDENT, AGONYParser.DEDENT, "Should Ignore EOF")
    return self.denter.next_token()

}

NL: ('\r'? '\n' ('\t')*);

//end the open source thing
//past here is all junk I (isabel) made

start: line+;
line : (functiondef | ((assignment | COMMENT | functioncall) (NL | EOF)) | if | while | for);


assignment : VARNAME EQUALS (value | bool) ;
operation : (NUMBER OPERATOR value | VARNAME OPERATOR value) ;

functiondef: 'def ' VARNAME '(' (|VARNAME (',' VARNAME)*) ')' ':' INDENT line+ (DEDENT | <EOF>);
functioncall: VARNAME '(' (|(value (',' value)*)) ')';

value : (VARNAME | NUMBER | operation | '(' value ')' | functioncall) ;

boolexpression: (bool (BOOLOPERATOR bool)* | '(' bool (BOOLOPERATOR bool)* ')');
bool: ('true' | 'false' | value COMPARISON value | 'not' bool | '(' bool ')');

if : ('if' boolexpression ':' INDENT line+ (DEDENT | <EOF>) ( | 'else' (|boolexpression) ':' INDENT line+ (DEDENT | <EOF>)));
while: ('while' boolexpression ':' INDENT line+ (DEDENT | <EOF>) );
for: ('for' VARNAME 'in' value ':' INDENT line+ (DEDENT | <EOF>) );




//VARTYPE	: ('var'|'int'|'string') ; MY RAGE IS UNENDING YOU WILL NOT HEAR THE END OF THIS I DESPISE PYTHON GRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

VARNAME : LETTERS (LETTERS|DIGIT)* ;

LETTERS	: [a-zA-Z] ;

BOOLOPERATOR		: ('and' | 'or');
COMPARISON			: ('=='|'>'|'>='|'<'|'<='|'!=');
EQUALS				: ('='|'*='|'+='|'-='|'/=') ;
OPERATOR			: ('+'|'-'|'/'|'*'|'%') ;

fragment DIGIT : [0-9] ;
fragment INT : (DIGIT)+ ;
fragment FLOAT : INT '.' INT ;
NUMBER : (INT | FLOAT);
fragment ANYTHING : ([!-~] | ' ');
COMMENT : COMMENTSTART ANYTHING*;
fragment COMMENTSTART : '#';

WHITESPACE          : (' '|'\t')+ -> skip ;

