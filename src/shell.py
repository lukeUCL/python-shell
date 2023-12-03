from antlr4 import InputStream, CommonTokenStream
from collections import deque
from PARSER.ShellLexer import shellLexer
from PARSER.ShellParser import ShellParser
from parseTreeFlattener import parseTreeFlattener
from Commands import SeqCommand, PipeCommand, CallCommand

def execute_command(input_command):
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

#piping not hanlded right now...... should we put optional parameter or just force 
# by appending args...?
def run_test(input_command, expected_output):
    output = execute_command(input_command)
    print(output)
    assert ''.join(output) == expected_output, f"Test failed for input: {input_command}"

# Run tests
run_test("echo Hello World | echo World", "Hello World\n")
run_test("echo Hello World | grep Bye", "")
run_test("echo Hello World | grep Hello | grep World", "Hello World\n")
run_test("echo First > tmpfile; echo Second >> tmpfile; cat tmpfile | grep Second", "Second\n")
run_test("echo Hello World > tmpfile; cat tmpfile | grep Hello", "Hello World\n")
