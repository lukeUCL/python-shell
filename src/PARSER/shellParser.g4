parser grammar ShellParser;

options {
  tokenVocab=ShellLexer;
}

command
 : seqPipeCommand
 | seqCommand
 | pipeCommand
 | callCommand
 ;

seqCommand
 : callCommand SEMI seqCommand
 | callCommand SEMI callCommand
 ;

pipeCommand
 : callCommand PIPE pipeCommand
 | callCommand PIPE callCommand
 ;

seqPipeCommand
 : seqCommand PIPE seqCommand
 | pipeCommand SEMI pipeCommand
 | seqCommand PIPE callCommand
 | callCommand PIPE seqCommand
 | pipeCommand SEMI callCommand
 | callCommand SEMI pipeCommand
 ;

callCommand
 : (argument | redirection | commandSubstitution)+
 ;
 
redirection
 : (LT | GT) argument
 ;

argument
 : CONCAT_ARG
 | quoted
 | UNQUOTED
 ;

concatArg
 : CONCAT_ARG
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