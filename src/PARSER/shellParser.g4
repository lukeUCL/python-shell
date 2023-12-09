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
 : (argument | redirection | backQuoted)+
 ;
 
redirection
 : (LT | GT)
 ;

argument
 : CONCAT_ARG
 | quoted
 | UNQUOTED
 | backQuoted
 ;

quoted
 : singleQuoted
 | doubleQuoted
 | backQuoted
 ;

singleQuoted
 : SINGLE_QUOTED_TEXT
 ;

doubleQuoted
 : DOUBLE_QUOTED_TEXT 
 ;

backQuoted
 : BACK_QUOTED_TEXT 
 ;