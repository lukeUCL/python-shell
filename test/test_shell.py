import string
import unittest
from unittest import mock
from applications import *
from shell import run
from pathlib import Path
from time import sleep
import os
from hypothesis import given
from hypothesis import strategies as st
from unittest.mock import patch

# Inside your TestShell class, you'll modify or add a new method to use your run function

class property_based_testing(unittest.TestCase):
    @given(st.lists(st.text()))
    def test_pwd(self, random_args):
        pwd_app = Pwd()
        result = pwd_app.exec(random_args)
        self.assertEqual(result, os.getcwd())

    @given(st.sampled_from([d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]))
    def test_cd(self, existing_dir):
        cd_app = Cd()
        initial_dir = os.getcwd()

        try:
            # Change directory to the existing directory
            cd_app.exec([existing_dir])
            self.assertEqual(os.getcwd(), os.path.join(initial_dir, existing_dir))

            # Changing back to the initial directory
            cd_app.exec([initial_dir])
            self.assertEqual(os.getcwd(), initial_dir)

        except FileNotFoundError:
            self.fail(f"Failed to change to directory: {existing_dir}")

    @given(st.lists(st.text()))
    def test_echo(self, strings):
        echo_app = Echo()
        expected_output = ' '.join(strings) + '\n'
        result = echo_app.exec(strings)
        self.assertEqual(result, expected_output)


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat_app = Cat()

    @given(st.text(min_size = 1, max_size=10))
    def test_cat_one_arg(self, file_content):
        # Use the Cat application
        cat = Cat()
        # Invoke the method
        result = cat.exec([file_content])
        
        if not file_content.strip():
            self.assertIn(f"Error: Empty file '{file_content}' detected", result)
        else:
            self.assertNotIn("Error: File not found", result)

    @given(st.text(max_size=5))
    def test_cat_multiple_args(self, file_contents):
        # Generate file contents, ensuring non-empty strings
        file_contents = [text for text in file_contents if text.strip()]
        
        if not file_contents:
            return  # Skip if there are no valid contents
        
        expected_output = ''.join(file_contents) 
        with patch('builtins.open') as mock_open:
            mock_open.side_effect = [
                mock.mock_open(read_data=text).return_value for text in file_contents
            ]
            files_to_read = [f'test_file{i}.txt' for i in range(1, len(file_contents) + 1)]
            result = self.cat_app.exec(files_to_read)
            self.assertEqual(result, expected_output)


class TestLs(unittest.TestCase):
    def setUp(self):
        self.ls_app = Ls()

    @given(st.just([]))  # Empty list to simulate no arguments
    def test_ls_no_args(self, args):
        # Execute test
        result = self.ls_app.exec(args)
        
        # Validate the result
        expected_output = "\n".join([f for f in os.listdir(os.getcwd()) if not f.startswith(".")]) + "\n"
        self.assertEqual(result, expected_output)

    @given(st.text(min_size=1, max_size=10)) # Generate text strings as directory arguments
    def test_ls_with_dir(self, test_dir):
        # Make sure test_dir is a valid string path
        test_dir = test_dir.strip()  # Remove potential leading/trailing spaces
        os.mkdir(test_dir)
        expected_output = "\n".join([f for f in os.listdir(test_dir) if not f.startswith(".")]) + "\n"

        result = self.ls_app.exec([test_dir])
        self.assertEqual(result, expected_output)

        os.rmdir(test_dir)

    @given(st.lists(st.text(min_size=1, max_size=10), min_size=1, max_size=3))  
    def test_ls_wrong_args(self, args):
        # Skip empty string directory arguments
        if all(arg.strip() == '' for arg in args):
            assume(False)

        with self.assertRaises((ValueError, FileNotFoundError, NotADirectoryError)):
            self.ls_app.exec(args)

# test commands, redirections, and echo cases, (quotes)
class CommandTesting(unittest.TestCase):

    @classmethod
    def eval(cls, cmdline):
        # Use your run function here, make sure it returns the output as a string
        output_deque = run(cmdline)
        # Convert deque to string if necessary  
        return ''.join(output_deque)
    
    def test_substitution(self):
        cmdline = "echo `echo nested`"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'nested')

    def test_sub_first(self):
        cmdline = 'echo hello'
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'hello')
    
    def test_sub_echo(self):
        cmdline = '`echo echo` hello'
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'hello')
    
    def test_echo_double_quotes(self):
        cmdline = 'echo "hello world"'
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'hello world')

    def test_nested_dquotes(self):
        cmdline = 'echo \'\"hello world\"\''
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, "hello world")
    
    def test_nested_squotes(self):
        cmdline = 'echo \"\'hello world\'\"'
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'hello world')
    
    def test_echo_single_quotes(self):
        cmdline = "echo 'hello world'"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'hello world')

    def test_cat_redirection(self):
        cmdline = "echo sample text > temp.txt; cat < temp.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'sample text')
        Path('temp.txt').unlink()  # Cleanup
    
    def test_command_sequences(self):
        cmdline = "echo first; echo second; echo third"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ['first', 'second', 'third'])

    def test_pipe_sequence(self):
        cmdline = "echo first | echo second | echo third"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ['third second first'])

    def test_grep_file(self):
        # Create a temporary file
        with open('temp_grep.txt', 'w') as file:
            file.write('line1\nmatch\nline2\nmatch\nline3')

        # Run grep command on the file
        cmdline = "grep match temp_grep.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")

        # Assert the output
        self.assertEqual(result, ['match', 'match'])

        # Clean up the file
        Path('temp_grep.txt').unlink()

    def test_head_file(self):
        # Create a temporary file
        with open('temp_head.txt', 'w') as file:
            file.write('line1\nline2\nline3\nline4')

        # Run head command on the file
        cmdline = "head -n 2 temp_head.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")

        # Assert the output
        self.assertEqual(result, ['line1', 'line2'])

        # Clean up the file
        Path('temp_head.txt').unlink()
    
    def test_tail_file(self):
        # Create a temporary file
        with open('temp_tail.txt', 'w') as file:
            file.write('line1\nline2\nline3\nline4')

        # Run tail command on the file
        cmdline = "tail -n 2 temp_tail.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")

        # Assert the output
        self.assertEqual(result, ['line3', 'line4'])

        # Clean up the file
        Path('temp_tail.txt').unlink()
    
    def test_find_with_globbing(self):
        Path('temp_dir').mkdir()
        Path('temp_dir/fileA.txt').touch()
        Path('temp_dir/fileB.txt').touch()

        cmdline = "find temp_dir -name '*.txt'"
        stdout = self.eval(cmdline)
        result = set(stdout.strip().split("\n"))

        self.assertEqual(result, {'temp_dir/fileA.txt', 'temp_dir/fileB.txt'})

        Path('temp_dir/fileA.txt').unlink()
        Path('temp_dir/fileB.txt').unlink()
        Path('temp_dir').rmdir()

    def test_echo_with_splitting(self):
        cmdline = "echo he\'llo\'"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, 'hello')
    
    def test_unsafe_command(self):
        cmdline = "rm nonexistentfile.txt"
        try:
            stdout = self.eval(cmdline)
        except Exception as e:
            self.assertIsInstance(e, FileNotFoundError)
        else:
            self.fail("Expected an exception but none was raised.")

        #test_tail, test unsafe, test_grep, test_nested,squotes
        #cat sequence piped, splitting
    
    def test_tail(self):
        cmdline = "tail test/text.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ['line2', 'line3'])
    
    def test_head(self):
        cmdline = "head test/text.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ['hello world', 'corgito ergo sum', 'i think therefore i am'])
    
    def test_pipeSeq(self):
        cmdline = "echo aaa > writeIn.txt; cat writeIn.txt unittest1.txt| uniq -i"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ["aaa", "aaa aaa aaa", "bbb"])
  
    def test_cut_specific_bytes_in_string(self):
        cut_instance = Cut()
        result = cut_instance.exec(['-b', '1', 'abcdefgh'])
        self.assertEqual(result, 'a\n')

    def test_uniq_duplicate_line(self):
        uniq_instance = Uniq()
        result = uniq_instance.exec(['aaa\naaa\nbbb\naaa'])
        self.assertEqual(result, 'aaa\nbbb\naaa\n')

if __name__ == '__main__':
    unittest.main()
