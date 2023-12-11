lexer grammar ShellLexer;

CONCAT_ARG : UNQUOTED DOUBLE_QUOTED_TEXT UNQUOTED 
           | UNQUOTED DOUBLE_QUOTED_TEXT 
           | DOUBLE_QUOTED_TEXT UNQUOTED 
           | UNQUOTED BACK_QUOTED_TEXT UNQUOTED
           | UNQUOTED SINGLE_QUOTED_TEXT UNQUOTED 
           | UNQUOTED SINGLE_QUOTED_TEXT
           | DOUBLE_QUOTED_TEXT UNQUOTED 
           ;

LT              : '<' ;
GT              : '>' ;
SINGLE_QUOTE    : '\'' ;
DOUBLE_QUOTE    : '"' ;
BACK_QUOTE      : '`' ;
UNQUOTED        : ~[ \t\r\n'";|<>`]+ ; 
WS              : [ \t]+ -> skip ;
NEWLINE         : [\r\n]+ -> skip ;
PIPE            : '|' ;
SEMI            : ';' ;

SINGLE_QUOTED_TEXT : SINGLE_QUOTE (~['\n\r])* SINGLE_QUOTE ;
BACK_QUOTED_TEXT   : BACK_QUOTE (~[`\\])* BACK_QUOTE;
DOUBLE_QUOTED_TEXT : DOUBLE_QUOTE ( BACK_QUOTED_TEXT | ~["\r\n\\`])* DOUBLE_QUOTE;
