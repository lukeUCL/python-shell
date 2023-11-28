
from antlr4 import InputStream, CommonTokenStream
from collections import deque

from PARSER.ShellLexer import ShellLexer
from PARSER.ShellParser import ShellParser
from parseTreeFlattener import parseTreeFlattener

from src.applications import *

def execute_command(input_command):
    # Parse the command
    input_stream = InputStream(input_command)
    lexer = ShellLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShellParser(token_stream)
    parse_tree = parser.command()

    # Flatten the parse tree
    visitor = parseTreeFlattener()
    command_structure = visitor.visit(parse_tree)

    #pass flattened to commands where we will pass args to apps..?

    output = deque()


