lexer grammar ShellLexer;

LT              : '<' ;
GT              : '>' ;
SINGLE_QUOTE    : '\'' ;
DOUBLE_QUOTE    : '"' ;
BACK_QUOTE      : '`' ;
UNQUOTED        : ~[ \t\r\n'";|<>`]+ ;
WS              : [ \t]+ -> skip ;
NEWLINE         : [\r\n]+ -> skip ;
PIPE : '|';
SEMI : ';';