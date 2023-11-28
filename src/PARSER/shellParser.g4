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
 : callCommand SEMI seqCommand   // Recursively allow more sequential commands
 | callCommand SEMI callCommand  // Base case for two sequential commands
 ;

pipeCommand
 : callCommand PIPE pipeCommand  // Recursively allow more piped commands
 | callCommand PIPE callCommand  // Base case for two piped commands
 ;

callCommand
 : (argument | redirection | commandSubstitution)+
 ;

argument
 : quoted
 | UNQUOTED
 ;

redirection
 : (LT | GT) argument
 ;

quoted
 : singleQuoted
 | doubleQuoted
 ;

singleQuoted
 : SINGLE_QUOTE .*? SINGLE_QUOTE
 ;

doubleQuoted
 : DOUBLE_QUOTE .*? DOUBLE_QUOTE
 ;

commandSubstitution
 : BACK_QUOTE innerCommand BACK_QUOTE
 ;

innerCommand
 : callCommand
 ;

