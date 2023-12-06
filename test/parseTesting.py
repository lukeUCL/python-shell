from antlr4 import InputStream, CommonTokenStream
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from src.PARSER.ShellLexer import shellLexer
from src.PARSER.ShellParser import ShellParser
import unittest

from src.PARSER.ShellParserVisitor import ShellParserVisitor

def parse_command(input_command):
    input_stream = InputStream(input_command)
    lexer = shellLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShellParser(token_stream)
    parse_tree = parser.command()
    return parse_tree.toStringTree(recog=parser).replace(" <EOF>", "")

#just get idea of parsing struct and see if we can flatten it
#some cases fail,, but expected not necessarily good/correct..
class TestShellGrammar(unittest.TestCase):
    # def test_command_with_input_redirection(self):
    #     input = "grep pattern < file.txt"
    #     expected = "(command (callCommand (argument grep) (argument pattern) (redirection < (argument (quoted (singleQuoted ' file with space.txt '))))))"
    #     self.assertEqual(parse_command(input), expected)

    # # Multiple args
    # def test_command_with_multiple_arguments(self):
    #     input = "grep pattern file.txt"
    #     expected = "(command (callCommand (argument grep) (argument pattern) (argument file.txt)))"
    #     self.assertEqual(parse_command(input), expected)

    # # Single arg
    # def test_command_with_single_argument(self):
    #     input = "echo hello"
    #     expected = "(command (callCommand (argument echo) (argument hello)))"
    #     self.assertEqual(parse_command(input), expected)
    
    # def test_redirection_with_quoted_filename(self):
    #     input = "grep pattern < 'file with space.txt'"
    #     expected = "(command (callCommand (argument grep) (argument pattern) (redirection < (argument (quoted (singleQuoted ' file with space.txt '))))))"
    #     self.assertEqual(parse_command(input), expected)

    # # Multiple pipelines
    # def test_multiple_pipelines(self):
    #     input = "cat file.txt | grep pattern | sort"
    #     expected ="(command (pipeCommand (callCommand (argument cat) (argument file.txt)) | (pipeCommand (callCommand (argument grep) (argument pattern)) | (callCommand (argument sort)))))"
    #     self.assertEqual(parse_command(input), expected)

    # # Sequence of commands
    # def test_sequence_of_commands(self):
    #     input = "cd folder; ls; pwd"
    #     expected = "(command (seqCommand (callCommand (argument cd) (argument folder)) ; (seqCommand (callCommand (argument ls)) ; (callCommand (argument pwd)))))"
    #     self.assertEqual(parse_command(input), expected)

    # # Nested quotes
    # def test_nested_quotes(self):
    #     input = 'echo "This is a `nested quote` example"'
    #     expected = "(command (callCommand (argument echo) (argument \"This is a `nested quote` example\")))"
    #     self.assertEqual(parse_command(input), expected)


    # def test_command_substitution(self):
    #     input = "echo `echo hello`"
    #     # The expected result after visiting the tree should be a string
    #     # that represents the structure after command substitution.
    #     expected = "(command (callCommand (argument echo) (commandSubstitution date)))"
    #     self.assertEqual(parse_command(input), expected)

    # def test_complex_command(self):
    #     input = "echo hello > output.txt; cat output.txt | sort"
    #     expected = "(command (seqCommand (callCommand (argument echo) (argument hello) (redirection > (argument output.txt))) (pipeCommand (callCommand (argument cat) (argument output.txt)) (callCommand (argument sort)))))"
    #     self.assertEqual(parse_command(input), expected)


    # def test_command_with_whitespace(self):
    #     # input = "ls    -la"
    #     input = "cd folder; ls; pwd"
    #     expected = "(command (callCommand (argument ls) (argument -la)))"
    #     self.assertEqual(parse_command(input), expected)

    # def test_b(self):
    #     # input = "ls    -la"
    #     input = "echo a\"b\"c"
    #     expected = "(command (callCommand (argument ls) (argument -la)))"
    #     self.assertEqual(parse_command(input), expected)

    def test_a(self):
        # input = "ls    -la"
        input = "< dir1/file2.txt cat"
        expected = "(command (callCommand (argument ls) (argument -la)))"
        self.assertEqual(parse_command(input), expected)


if __name__ == '__main__':
    unittest.main()
#- (command (callCommand (argument echo) (argument (quoted (singleQuoted ' hello world ')))))