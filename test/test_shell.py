import string
import unittest
from unittest import mock
from applications import *
from shell import run
from pathlib import Path
from time import sleep
import os
from hypothesis import example, given
from hypothesis import strategies as st
from unittest.mock import patch

# Inside your TestShell class, you'll modify or add a new method to use your run function
class TestShell(unittest.TestCase):

    @classmethod
    def eval(cls, cmdline):
        # Use your run function here, make sure it returns the output as a string
        output_deque = run(cmdline)
        # Convert deque to string if necessary  
        return ''.join(output_deque)

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

    # Unit testing for, WC, TOUCH, DIFF
    # unittesting wc
    # words
    # def test_wc_word_count(self):
    #     cmdline = "wc -w 'one two three'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, '3')
    
    # # lines
    # def test_wc_line_count(self):
    #     cmdline = "wc -l 'one two three'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, '1')
    
    # # chars
    # def test_wc_char_count(self):
    #     cmdline = "wc -c 'one two three'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, '13')

    # # file
    # def test_wc_word_count(self):
    #     cmdline = "wc -w unittest1.txt"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, '4')

    # # property based testing
    # def test_wc_word_property(self):
    #     input_str = 'one two three'
    #     cmdline = f"wc -w '{input_str}'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     # only count the words in the input string
    #     word_count = len(input_str.split())
    #     self.assertEqual(result, str(word_count))

    # # mutation testing
    # def test_wc_word_count_mutation(self):
    #     cmdline = "wc -w 'one two three'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     mutated_result = int(result) + 1
    #     self.assertNotEqual(mutated_result, '3')
    
    # # integration testing

    # def test_wc_pipe_file_to_string(self):
    #     cmdline = "cat unittest1.txt | wc -w"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, '4')
    
    # def test_wc_pipe_string_to_file(self):
    #     cmdline = "echo foo nam > newfile.txt| wc -w newfile.txt"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, '2')

    # # testing touch, property based
    # def test_touch_update_access_time(self):
    #     filename = 'unittest1.txt'
    #     old_access_time = os.path.getatime(filename)
    #     sleep(1) # Sleep for 1 second to ensure the access time is different
    #     cmdline = f"touch {filename}"
    #     self.eval(cmdline)  
    #     new_access_time = os.path.getatime(filename)
    #     self.assertGreater(
    #         new_access_time, old_access_time, "The access time was not updated."
    #         )
    
    # def test_touch_create_file(self):
    #     filename = "testfile.txt"
    #     cmdline = f"touch {filename}"
    #     self.eval(cmdline)
    #     self.assertTrue(Path(filename).exists(), "The file was not created.")
    #     Path(filename).unlink()

    # # testing diff
    # def test_diff_files(self):
    #     cmdline = "diff unittest1.txt unittest2.txt"
    #     result = self.eval(cmdline).strip()

    #     expected_line1 = "-aaa aaa aaa"
    #     expected_line2 = "-bbb"
    #     expected_line3 = "+zzz zzz"
    #     expected_line4 = "+ccc"
    #     expected_line5 = "+ddd"

    #     self.assertIn(expected_line1, result)
    #     self.assertIn(expected_line2, result)
    #     self.assertIn(expected_line3, result)
    #     self.assertIn(expected_line4, result)
    #     self.assertIn(expected_line5, result)
    
    # def test_diff_strings(self):
    #     cmdline = "diff 'hello' 'hi'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     expected_line1 = "-hello"
    #     expected_line2 = "+hi"
    #     self.assertIn(expected_line1, result)
    #     self.assertIn(expected_line2, result)

    # def test_pipe_diff_files(self):
    #     cmdline = "cat unittest1.txt | diff unittest2.txt"
    #     result = self.eval(cmdline).strip()

    #     expected_line1 = "-zzz zzz"
    #     expected_line2 = "-ccc"
    #     expected_line3 = "-ddd"
    #     expected_line4 = "+aaa aaa aaa"
    #     expected_line5 = "+bbb"

    #     self.assertIn(expected_line1, result)
    #     self.assertIn(expected_line2, result)
    #     self.assertIn(expected_line3, result)
    #     self.assertIn(expected_line4, result)
    #     self.assertIn(expected_line5, result)

    # def test_pipe_diff_strings(self):
    #     cmdline = "echo hello | diff 'hi'"
    #     result = self.eval(cmdline).strip()
        
    #     expected_line1 = "-hi"
    #     expected_line2 = "+hello"
    #     self.assertIn(expected_line1,result)
    #     self.assertIn(expected_line2,result)
    

if __name__ == '__main__':
    unittest.main()
