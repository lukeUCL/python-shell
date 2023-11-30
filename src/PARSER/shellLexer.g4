lexer grammar shellLexer;

CONCAT_ARG : UNQUOTED DOUBLE_QUOTED_TEXT UNQUOTED 
           | UNQUOTED DOUBLE_QUOTED_TEXT 
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

SINGLE_QUOTED_TEXT : '\'' (~['\n\r])* '\'' ;
//DOUBLE_QUOTED_TEXT : '"' ( ~["\r\n] | BACK_QUOTE ~[`]* BACK_QUOTE )* '"';
DOUBLE_QUOTED_TEXT : '"' ( ESCAPE_SEQUENCE | ~["\r\n\\] )* '"';
fragment ESCAPE_SEQUENCE : '\\' . ;  // Handles escaped characters
