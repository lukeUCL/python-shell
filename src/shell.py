from antlr4 import InputStream, CommonTokenStream
from collections import deque
from PARSER.ShellLexer import shellLexer
from PARSER.ShellParser import ShellParser
from parseTreeFlattener import parseTreeFlattener
from Commands import SeqCommand, PipeCommand, CallCommand
import sys
import os
from os import listdir
from collections import deque
from glob import glob

def run(input_command):
    input_stream = InputStream(input_command)
    lexer = shellLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShellParser(token_stream)
    parse_tree = parser.command()

    visitor = parseTreeFlattener()

    flattened = visitor.visit(parse_tree)

    output = deque()

    if isinstance(flattened[0], list):
        # Handle complex structures like pipeSeq
        for part in flattened:
            if part[0] == 'pipe':
                PipeCommand().execute(part[1:], output)
            elif part[0] == 'seq':
                SeqCommand().execute(part[1:], output)
    elif flattened[0] == 'pipe':
        PipeCommand().execute(flattened[1:], output)
    elif flattened[0] == 'seq':
        SeqCommand().execute(flattened[1:], output)
    else:
        CallCommand().execute(flattened, output)

    return output

if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        output = run(sys.argv[2])
        while len(output) > 0:
            print(output.popleft(), end="")
    else:
        while True:
            try:
                cmdline = input(os.getcwd() + "> ")
                if cmdline.strip() == 'exit':
                    break
                output = run(cmdline)
                while len(output) > 0:
                    print(output.popleft(), end="")
            except KeyboardInterrupt:
                print()  # Print a newline character
                continue  # Go back to the beginning of the loop
            except EOFError:
                break  # Exit the loop on EOF
            except Exception as e:
                print(f"An error occurred: {e}")
