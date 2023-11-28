

import sys
#forcing paths...
sys.path.append('/Users/lukemciver/softwareEng')  
sys.path.append('/Users/lukemciver/softwareEng/src')  
sys.path.append('/Users/lukemciver/softwareEng/src/PARSER')  
sys.path.append('/Users/lukemciver/softwareEng/src/parserTreeFlattener')  

from antlr4 import InputStream, CommonTokenStream

from src.PARSER.ShellLexer import ShellLexer
from src.PARSER.ShellParser import ShellParser
from src.PARSER.ShellParserVisitor import ShellParserVisitor
from src.parseTreeFlattener import parseTreeFlattener
import unittest

def parse_command(input_command):
    input_stream = InputStream(input_command)
    lexer = ShellLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShellParser(token_stream)
    parse_tree = parser.command()
    return parse_tree  # not in string form- for traversing


class TestShellVisitor(unittest.TestCase):
    #teste case should adjust
    def test_flatten_seq_commands(self):
        input_command = "cd folder; ls; pwd"
        parse_tree = parse_command(input_command) 
        visitor = parseTreeFlattener()
        result = visitor.visit(parse_tree)
        expected = [['cd', 'folder'], ['ls'], ['pwd']]
        self.assertEqual(result, expected)

    #flag for commands?? maybe not effective 
    def test_flatten_pipe_commands(self):
        input_command = "cat file.txt | grep pattern | sort"
        parse_tree = parse_command(input_command)  
        visitor = parseTreeFlattener()
        result = visitor.visit(parse_tree)  
        expected = [['cat', 'file.txt'], ['grep', 'pattern'], ['sort']]
        self.assertEqual(result, expected)

    def test_command_with_arguments(self):
        input_command = "grep 'pattern' file.txt"
        parse_tree = parse_command(input_command)
        visitor = parseTreeFlattener()
        result = visitor.visit(parse_tree)
        # command_name = result[0][0]
        # arguments = result[0][1:]
        self.assertEqual(result, ['grep' ['pattern', 'file.txt']])
    
    def test_single_quoted_argument(self):
        input_command = "echo 'Hello World'"
        parse_tree = parse_command(input_command)
        visitor = parseTreeFlattener()
        result = visitor.visit(parse_tree)
        expected = ['echo', ['Hello',  'World']] 
        self.assertEqual(result, expected)

    def test_double_quoted_argument_with_command_substitution(self):
        input_command = "echo 'echo a'"
        parse_tree = parse_command(input_command)
        visitor = parseTreeFlattener()
        result = visitor.visit(parse_tree)
        expected = ['echo', ['a']]  
        self.assertEqual(result, expected)


# Run the tests
if __name__ == '__main__':
    unittest.main()
