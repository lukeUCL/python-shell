import unittest
from unittest import mock
from collections import deque
from applications import Uniq
from shell import run
from pathlib import Path
import os
from hypothesis import given
from hypothesis import strategies as st
from unittest.mock import patch


# Inside your TestShell class, you'll modify
# or add a new method to use your run function
class TestPwd(unittest.TestCase):
    @given(st.none())
    def test_pwd_with_run(self, _):
        cmdline = 'pwd'
        expected_result = deque([os.getcwd()])

        result = run(cmdline)

        self.assertEqual(result, expected_result)


class TestCd(unittest.TestCase):
    @given(st.sampled_from([d for d in os.listdir(os.getcwd())
                            if os.path.isdir(d)]))
    def test_cd_with_run(self, existing_dir):
        initial_dir = os.getcwd()

        # change directory to the existing directory
        run(f"cd {existing_dir}")
        self.assertEqual(os.getcwd(), os.path.join(initial_dir, existing_dir))

        # changing back to the initial directory
        run(f"cd {initial_dir}")
        self.assertEqual(os.getcwd(), initial_dir)


class TestEcho(unittest.TestCase):
    @given(st.text(alphabet=st.characters
                   (whitelist_categories=('L', 'N', 'Z')),
                    min_size=0, max_size=7))
    def test_echo_with_run(self, strings):
        input_string = ' '.join(strings)
        input_string = input_string.strip()
        expected_output = input_string + '\n' if input_string else '\n'
        result = run(f"echo {input_string}")
        result_str = ''.join(result)
        self.assertEqual(result_str, expected_output)


class TestCat(unittest.TestCase):
    @given(st.text(st.characters
                   (whitelist_categories=('Ll', 'Lu')),
                    min_size = 1))
    def test_cat_one_arg(self, file_content):
        # Invoke the method
        result = run(f"cat {file_content}")

        self.assertNotIn("Error: File not found", result)

    @given(st.text(st.characters(min_codepoint=65, max_codepoint=90) |
                   st.characters(min_codepoint=97, max_codepoint=122),
                   min_size=1, max_size = 5))
    def test_cat_multiple_args_with_run(self, file_contents):
        # Generate file contents, ensuring non-empty strings
        file_contents = [text for text in file_contents if text.strip()]

        with patch('builtins.open') as mock_open:
            mock_open.side_effect = [
                mock.mock_open(read_data=text).\
                    return_value for text in file_contents
            ]
            command = f"cat {' '.join(file_contents)}"
            result = run(command)

            # Convert deque to a string for comparison
            result_str = ''.join(result)

            # Your assertions
            self.assertEqual(result_str, ''.join(file_contents))


class TestLs(unittest.TestCase):
    @given(st.sampled_from([d for d in os.listdir(os.getcwd())
                            if os.path.isdir(d)]))
    def test_ls(self, directory):
        ls_dir = os.path.abspath(directory)
        files_in_dir = [f for f in os.listdir(ls_dir) if not f.startswith(".")]
        expected_output = "\n".join(files_in_dir) + "\n"

        result = run(f"ls {directory}")

        result_str = ''.join(result)

        expected_output = '\n'.join([f for f in os.listdir(directory)\
                                     if not f.startswith(".")]) + "\n"
        self.assertEqual(result_str, expected_output)


# test commands, redirections, and echo cases, (quotes)
class CommandTesting(unittest.TestCase):

    @classmethod
    def eval(cls, cmdline):
        # Use your run function here,
        # make sure it returns the output as a string
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
        cmdline = 'echo '"hello world"''
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, "hello world")

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

        cmdline = "grep match temp_grep.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")

        self.assertEqual(result, ['match', 'match'])
        Path('temp_grep.txt').unlink()

    def test_head_file(self):
        with open('temp_head.txt', 'w') as file:
            file.write('line1\nline2\nline3\nline4')

        cmdline = "head -n 2 temp_head.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")

        self.assertEqual(result, ['line1', 'line2'])
        Path('temp_head.txt').unlink()

    def test_tail_file(self):

        with open('temp_tail.txt', 'w') as file:
            file.write('line1\nline2\nline3\nline4')

        cmdline = "tail -n 2 temp_tail.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")

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

    # no flags
    def test_tail(self):
        cmdline = "tail test/text.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, 
                         ['hello world', 'corgito ergo sum',
                         'i think therefore i am'])

    def test_head(self):
        cmdline = "head test/text.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, 
                         ['hello world', 'corgito ergo sum',
                         'i think therefore i am'])

    def test_pipeSeq(self):
        cmdline = "echo aaa > writeIn.txt;\
                    cat writeIn.txt unittest1.txt| uniq -i"
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ["aaa", "aaa aaa aaa", "bbb"])

    def test_cut_specific_bytes_in_string(self):
        cmdline = "echo abcdef | cut -b 1"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, "a")

    def test_uniq_duplicate_line(self):
        uniq_instance = Uniq()
        result = uniq_instance.exec(['aaa\naaa\nbbb\naaa'])
        self.assertEqual(result, 'aaa\nbbb\naaa\n')

    def test_globbing(self):
        cmdline = "echo test/*.txt"
        stdout = self.eval(cmdline)
        result = set(stdout.strip().split())
        self.assertEqual(result, {"test/text.txt", "test/texti.txt"})

    def test_unsafe(self):
        cmdline = "_echo aaa"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, "aaa")


if __name__ == '__main__':
    unittest.main()
