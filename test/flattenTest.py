

import sys
#forcing paths...
sys.path.append('/Users/lukemciver/softwareEng')  
sys.path.append('/Users/lukemciver/softwareEng/src')  
sys.path.append('/Users/lukemciver/softwareEng/src/PARSER')  
sys.path.append('/Users/lukemciver/softwareEng/src/parserTreeFlattener')  

from antlr4 import InputStream, CommonTokenStream

from src.PARSER.ShellLexer import shellLexer
from src.PARSER.ShellParser import ShellParser
from src.PARSER.ShellParserVisitor import ShellParserVisitor
from src.parseTreeFlattener import parseTreeFlattener
import unittest

def parse_command(input_command):
    input_stream = InputStream(input_command)
    lexer = shellLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShellParser(token_stream)
    parse_tree = parser.command()
    return parse_tree  # not in string form- for traversing


class TestShellVisitor(unittest.TestCase):
    # teste case should adjust
    # def test_flatten_seq_commands(self):
    #     input_command = "cd folder; ls; pwd"
    #     parse_tree = parse_command(input_command) 
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['seq', ['cd', ['folder']], ['ls', []], ['pwd', []]]
    #     self.assertEqual(result, expected)

    # #flag for commands?? maybe not effective 
    # def test_flatten_pipe_commands(self):
    #     input_command = "cat file.txt | grep pattern | sort"
    #     parse_tree = parse_command(input_command)  
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)  
    #     expected = ['pipe', ['cat', ['file.txt']], ['grep', ['pattern']], ['sort', []]]
    #     self.assertEqual(result, expected)

    # def test_command_with_arguments(self):
    #     input_command = "grep 'pattern' file.txt"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     # command_name = result[0][0]
    #     # arguments = result[0][1:]
    #     expected=['grep' ,['pattern', 'file.txt']]
    #     self.assertEqual(result,expected)
    
    # def test_single_quoted_argument(self):
    #     input_command = "echo 'Hello World'"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['Hello World']] 
    #     self.assertEqual(result, expected)

    # def test_double_quoted_argument_with_command_substitution(self):
    #     input_command = "echo 'echo a'"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['a']]  
    #     self.assertEqual(result, expected)
    
    # def test_flatten_grep_command(self):
    #     input_command = "grep 'myPattern' anotherfile.txt"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['grep', ['myPattern', 'anotherfile.txt']]
    #     self.assertEqual(result, expected)
    
    # def test_flatten_grep_command(self):
    #     input_command = "grep 'myPattern' anotherfile.txt"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['grep', ['myPattern', 'anotherfile.txt']]
    #     self.assertEqual(result, expected)

    # def nested_quotes(self):
    #     input_command = "echo 'nested \"test\" testing' "
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['nested \"test\" testing' ]]
    #     self.assertEqual(result, expected)


    # def test_flatten_nested_doublequotes(self):
    #     input_command = 'echo "a `echo "b"`"'
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['a `echo "b"`']] 
    #     self.assertEqual(result, expected)

    # def test_flatten_disabled_doublequotes(self):
    #     input_command = "echo '\"\"'"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['\"\"']]  
    #     self.assertEqual(result, expected)

    # def test_flatten_input_redirection_infront(self):
    #     input_command = "< dir1/file2.txt cat"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['<', ['dir1/file2.txt', 'cat']] 
    #     self.assertEqual(result, expected)

    # def test_flatten_splitting(self):
    #     input_command = 'echo a"b"c'
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['abc']]  
    #     self.assertEqual(result, expected)
    
    # def test_flatten_output_redirection(self):
    #     input_command ="cat dir1/file1.txt dir1/file2.txt | sort | uniq"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['foo', '>', 'newfile.txt']] 
    #     self.assertEqual(result, expected)

    # def test_idk(self):
    #     input_command = 'echo \"\'test\'\"'
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     expected = ['echo', ['foo', '>', 'newfile.txt']] 
    #     self.assertEqual(result, expected)

    # def test_nested_doublequotes(self):
    #     input_command = "echo aaa > dir1/file2.txt; cat dir1/file1.txt dir1/file2.txt | uniq -i"
    #     parse_tree = parse_command(input_command)
    #     visitor = parseTreeFlattener()
    #     result = visitor.visit(parse_tree)
    #     print(result)
    #     expected = ['echo', ["a"]] 
    #     self.assertEqual(result, expected)

    def test_pseq(self):
        input_command ='echo a\"a\"a'
        parse_tree = parse_command(input_command)
        visitor = parseTreeFlattener()
        result = visitor.visit(parse_tree)
        print(result)
        expected = ['echo', ["a"]]  
        self.assertEqual(result, expected)




input_command = 'echo a\"a\"a'

parse_tree = parse_command(input_command)
# (command (callCommand (argument echo) (argument (quoted (singleQuoted ' hello world ')))))

# visitor = parseTreeFlattener()
# result = visitor.visit(parse_tree)

lexer = shellLexer(InputStream(input_command))
for token in lexer.getAllTokens():
    token_type = lexer.symbolicNames[token.type] 
    print(token_type)
    print(token)
lexer.reset()  


if __name__ == '__main__':
    unittest.main()
