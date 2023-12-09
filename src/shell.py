from antlr4 import InputStream, CommonTokenStream
from collections import deque
from PARSER.ShellLexer import shellLexer
from PARSER.ShellParser import ShellParser
from parseTreeFlattener import parseTreeFlattener
from Commands import SeqCommand, PipeCommand, CallCommand
import sys
import os
from collections import deque
from glob import glob

def expandGlob(commandLine):
    flat = not isinstance(commandLine[0], list)

    if not flat:
        pass
    else:
        for i, arg in enumerate(commandLine):
            if '*' in arg or '?' in arg:
                rep = glob(arg)
                commandLine[i]='\n'.join(rep).strip('\n')

    return commandLine


def run(input_command):
    input_stream = InputStream(input_command)
    lexer = shellLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShellParser(token_stream)
    parse_tree = parser.command()

    visitor = parseTreeFlattener()

    flattened = visitor.visit(parse_tree)
    flattened = expandGlob(flattened)

    output = deque()
    #['seq', ['_ls', 'dir3'], ['echo', 'AAA', {...}]]
    #seq
    #['_ls', 'dir3']
    #['echo', 'AAA', {'in': None, 'out': 'newfile.txt'}]
    #[['pipe', ['seq', ['echo', 'aaa', {'in': None, 'out': 'dir1/file2.txt'}], ['cat', 'dir1/file1.txt', 'dir1/file2.txt']]], ['pipe', ['uniq', '-i']]]
    if isinstance(flattened[0], list):
        # only need, seq, followed by pipe, other way around is jsut a seq..?
        intermediate = []
        for part in flattened:
            if part[0] == 'seq':
                intermediate.extend(SeqCommand().execute(part[1:], output,store=True))
            elif part[0] == 'pipe':
                part[1].extend(intermediate)
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
