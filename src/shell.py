# Let's define a function that will take the input command as a string,
# parse it, flatten the parse tree, and then execute the corresponding apps.

from antlr4 import InputStream, CommonTokenStream
from collections import deque

# Assuming ShellLexer and ShellParser are the ANTLR generated classes for your language
from PARSER.ShellLexer import ShellLexer
from PARSER.ShellParser import ShellParser
# Assuming parseTreeFlattener is your custom class that extends ShellParserVisitor
from parseTreeFlattener import parseTreeFlattener

# The apps functions are assumed to be defined in a separate file named 'apps.py'
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

    # Execute the command structure using your apps
    output = deque()

    # Determine if it's a pipe command and handle it accordingly
    if isinstance(command_structure[0], list) and command_structure[0][0] == 'pipe':
        pass
        # Extract the commands from the structure
        commands = command_structure[1:]
        # Execute the pipeline
        for cmd in commands:
            app_name = cmd[0]
            app_args = cmd[1]
            apps(app_name, app_args, output)
    elif isinstance(command_structure[0], list) and command_structure[0][0] == 'seq':
        pass
        # Execute a sequence of commands
        commands = command_structure[1:]
        for cmd in commands:
            app_name = cmd[0]
            app_args = cmd[1]
            apps(app_name, app_args, output)
    else:
        # It's a single command
        app_name = command_structure[0]
        app_args = command_structure[1:]
        apps(app_name, app_args, output)

    # Return the output from the command execution
    return list(output)

# Example usage
user_input = "ls | grep py"
execution_output = execute_command(user_input)
print(execution_output)

