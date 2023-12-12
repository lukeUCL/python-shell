from antlr4 import InputStream, CommonTokenStream
from collections import deque
from PARSER.ShellLexer import ShellLexer
from PARSER.ShellParser import ShellParser
from parseTreeFlattener import parseTreeFlattener
from Commands import evalCommand
import sys
import os
from glob import glob


def expandGlob(commandLine):
    flat = not isinstance(commandLine[0], list)

    if not flat:
        for i, sub_command in enumerate(commandLine):
            for j, arg in enumerate(sub_command):
                if commandLine[i][0] != 'find' and ('*' in arg or '?' in arg):
                    rep = glob(arg)
                    commandLine[i][j] = '\n'.join(rep).strip('\n')
    else:
        for i, arg in enumerate(commandLine):
            if commandLine[0] != 'find' and ('*' in arg or '?' in arg):
                rep = glob(arg)
                commandLine[i] = '\n'.join(rep).strip('\n')
                
    return commandLine


def run(input_command):
    # lex, parse, convert tree
    # glob (not edge cases)
    # call commands
    input_stream = InputStream(input_command)
    lexer = ShellLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShellParser(token_stream)
    parse_tree = parser.command()
    visitor = parseTreeFlattener()
    flattened = visitor.visit(parse_tree)
    flattened = expandGlob(flattened)

    output = deque()
    evalCommand(flattened, output)
    return output

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "-c":
        for output in run(sys.argv[2]):
            print(output, end="")
    else:
        while True:
            try:
                cmdline = input(os.getcwd() + "> ").strip()
                if cmdline == 'exit':
                    break
                for output in run(cmdline):
                    print(output, end="")
            except KeyboardInterrupt:
                print()  # Handle Ctrl+C gracefully
            except EOFError:
                break  # Handle EOF (Ctrl+D) gracefully
            except Exception as e:
                print(f"An error occurred: {e}")
