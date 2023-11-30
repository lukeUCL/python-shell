parser grammar ShellParser;

options {
  tokenVocab=ShellLexer;
}
command
 : seqCommand
 | pipeCommand
 | callCommand
 ;

seqCommand
 : callCommand SEMI seqCommand   
 | callCommand SEMI callCommand           

pipeCommand
 : callCommand PIPE pipeCommand 
 | callCommand PIPE callCommand  
 ;

callCommand
 : (argument | redirection | commandSubstitution)+
 ;

argument
 : CONCAT_ARG
 | quoted
 | UNQUOTED
 ;

  concatArg
 : CONCAT_ARG
 ;

redirection
 : (LT | GT) argument
 ;

quoted
 : singleQuoted
 | doubleQuoted
 ;

singleQuoted
 : SINGLE_QUOTED_TEXT
 ;

doubleQuoted
 : DOUBLE_QUOTED_TEXT
 ;

commandSubstitution
 : BACK_QUOTE innerCommand BACK_QUOTE
 ;

innerCommand
 : callCommand
 ;