# import string
# import unittest
# from unittest import mock
# from applications import *
# from shell import run
# from pathlib import Path
# from time import sleep
# import os
# from hypothesis import given
# from hypothesis import strategies as st
# from unittest.mock import patch

# # Inside your TestShell class, you'll modify or add a new method to use your run function

# class property_based_testing(unittest.TestCase):
#     @given(st.lists(st.text()))
#     def test_pwd(self, random_args):
#         pwd_app = Pwd()
#         result = pwd_app.exec(random_args)
#         self.assertEqual(result, os.getcwd())

#     @given(st.sampled_from([d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]))
#     def test_cd(self, existing_dir):
#         cd_app = Cd()
#         initial_dir = os.getcwd()

#         try:
#             # Change directory to the existing directory
#             cd_app.exec([existing_dir])
#             self.assertEqual(os.getcwd(), os.path.join(initial_dir, existing_dir))

#             # Changing back to the initial directory
#             cd_app.exec([initial_dir])
#             self.assertEqual(os.getcwd(), initial_dir)

#         except FileNotFoundError:
#             self.fail(f"Failed to change to directory: {existing_dir}")

#     @given(st.lists(st.text()))
#     def test_echo(self, strings):
#         echo_app = Echo()
#         expected_output = ' '.join(strings) + '\n'
#         result = echo_app.exec(strings)
#         self.assertEqual(result, expected_output)


# class TestCat(unittest.TestCase):
#     def setUp(self):
#         self.cat_app = Cat()

#     @given(st.text(min_size = 1, max_size=10))
#     def test_cat_one_arg(self, file_content):
#         # Use the Cat application
#         cat = Cat()
#         # Invoke the method
#         result = cat.exec([file_content])
        
#         if not file_content.strip():
#             self.assertIn(f"Error: Empty file '{file_content}' detected", result)
#         else:
#             self.assertNotIn("Error: File not found", result)

#     @given(st.text(max_size=5))
#     def test_cat_multiple_args(self, file_contents):
#         # Generate file contents, ensuring non-empty strings
#         file_contents = [text for text in file_contents if text.strip()]
        
#         if not file_contents:
#             return  # Skip if there are no valid contents
        
#         expected_output = ''.join(file_contents) 
#         with patch('builtins.open') as mock_open:
#             mock_open.side_effect = [
#                 mock.mock_open(read_data=text).return_value for text in file_contents
#             ]
#             files_to_read = [f'test_file{i}.txt' for i in range(1, len(file_contents) + 1)]
#             result = self.cat_app.exec(files_to_read)
#             self.assertEqual(result, expected_output)


# class TestLs(unittest.TestCase):
#     def setUp(self):
#         self.ls_app = Ls()

#     @given(st.just([]))  # Empty list to simulate no arguments
#     def test_ls_no_args(self, args):
#         # Execute test
#         result = self.ls_app.exec(args)
        
#         # Validate the result
#         expected_output = "\n".join([f for f in os.listdir(os.getcwd()) if not f.startswith(".")]) + "\n"
#         self.assertEqual(result, expected_output)

#     @given(st.text(min_size=1, max_size=10)) # Generate text strings as directory arguments
#     def test_ls_with_dir(self, test_dir):
#         # Make sure test_dir is a valid string path
#         test_dir = test_dir.strip()  # Remove potential leading/trailing spaces
#         os.mkdir(test_dir)
#         expected_output = "\n".join([f for f in os.listdir(test_dir) if not f.startswith(".")]) + "\n"

#         result = self.ls_app.exec([test_dir])
#         self.assertEqual(result, expected_output)

#         os.rmdir(test_dir)

#     @given(st.lists(st.text(min_size=1, max_size=10), min_size=1, max_size=3))  
#     def test_ls_wrong_args(self, args):
#         # Skip empty string directory arguments
#         if all(arg.strip() == '' for arg in args):
#             assume(False)

#         with self.assertRaises((ValueError, FileNotFoundError, NotADirectoryError)):
#             self.ls_app.exec(args)

# # test commands, redirections, and echo cases, (quotes)
# class CommandTesting(unittest.TestCase):

#     @classmethod
#     def eval(cls, cmdline):
#         # Use your run function here, make sure it returns the output as a string
#         output_deque = run(cmdline)
#         # Convert deque to string if necessary  
#         return ''.join(output_deque)
    
#     def test_substitution(self):
#         cmdline = "echo `echo nested`"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'nested')

#     def test_sub_first(self):
#         cmdline = 'echo hello'
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'hello')
    
#     def test_echo_double_quotes(self):
#         cmdline = 'echo "hello world"'
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'hello world')

#     def test_nested_dquotes(self):
#         cmdline = 'echo '"hello world"''
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, "hello world")
    
#     def test_nested_squotes(self):
#         cmdline = 'echo "\'hello world\'"'
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'hello world')
    
#     def test_echo_single_quotes(self):
#         cmdline = "echo 'hello world'"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'hello world')

#     def test_cat_redirection(self):
#         cmdline = "echo sample text > temp.txt; cat < temp.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'sample text')
#         Path('temp.txt').unlink()  # Cleanup
    
#     def test_command_sequences(self):
#         cmdline = "echo first; echo second; echo third"
#         stdout = self.eval(cmdline)
#         result = stdout.strip().split("\n")
#         self.assertEqual(result, ['first', 'second', 'third'])

#     def test_grep(self):
#         cmdline = "echo 'line1\nline2\nmatch\nline3' | grep match"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'match')

#     def test_grep_file(self):
#         # Create a temporary file
#         with open('temp_grep.txt', 'w') as file:
#             file.write('line1\nmatch\nline2\nmatch\nline3')

#         # Run grep command on the file
#         cmdline = "grep match temp_grep.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip().split("\n")

#         # Assert the output
#         self.assertEqual(result, ['match', 'match'])

#         # Clean up the file
#         Path('temp_grep.txt').unlink()

#     def test_head_file(self):
#         # Create a temporary file
#         with open('temp_head.txt', 'w') as file:
#             file.write('line1\nline2\nline3\nline4')

#         # Run head command on the file
#         cmdline = "head -n 2 temp_head.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip().split("\n")

#         # Assert the output
#         self.assertEqual(result, ['line1', 'line2'])

#         # Clean up the file
#         Path('temp_head.txt').unlink()
    
#     def test_tail_file(self):
#         # Create a temporary file
#         with open('temp_tail.txt', 'w') as file:
#             file.write('line1\nline2\nline3\nline4')

#         # Run tail command on the file
#         cmdline = "tail -n 2 temp_tail.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip().split("\n")

#         # Assert the output
#         self.assertEqual(result, ['line3', 'line4'])

#         # Clean up the file
#         Path('temp_tail.txt').unlink()

#     # def test_cat_sequence_piped(self):
#         # with open('temp_file1.txt', 'w') as file:
#         #     file.write('apple\nbanana')
#         # with open('temp_file2.txt', 'w') as file:
#         #     file.write('orange\ngrape')

#         # cmdline = "cat temp_file1.txt; cat temp_file2.txt | sort"
#         # stdout = self.eval(cmdline)
#         # result = stdout.strip().split("\n")

#         # self.assertEqual(result, ['apple', 'banana', 'grape', 'orange'])

#         # Path('temp_file1.txt').unlink()
#         # Path('temp_file2.txt').unlink()
    
#     def test_find_with_globbing(self):
#         Path('temp_dir').mkdir()
#         Path('temp_dir/fileA.txt').touch()
#         Path('temp_dir/fileB.txt').touch()

#         cmdline = "find temp_dir -name '*.txt'"
#         stdout = self.eval(cmdline)
#         result = set(stdout.strip().split("\n"))

#         self.assertEqual(result, {'temp_dir/fileA.txt', 'temp_dir/fileB.txt'})

#         Path('temp_dir/fileA.txt').unlink()
#         Path('temp_dir/fileB.txt').unlink()
#         Path('temp_dir').rmdir()

#     def test_echo_with_splitting(self):
#         cmdline = "echo he\'llo\'"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, 'hello')
    
#     def test_mkdir_and_rmdir(self):
#         # Create directory
#         cmdline = "mkdir temp_test_dir"
#         self.eval(cmdline)
#         self.assertTrue(Path('temp_test_dir').exists())

#         # Remove directory
#         cmdline = "rmdir temp_test_dir"
#         self.eval(cmdline)
#         self.assertFalse(Path('temp_test_dir').exists())
    
#     def test_unsafe_command(self):
#         cmdline = "rm nonexistentfile.txt"
#         try:
#             stdout = self.eval(cmdline)
#         except Exception as e:
#             self.assertIsInstance(e, FileNotFoundError)
#         else:
#             self.fail("Expected an exception but none was raised.")

#         #test_tail, test unsafe, test_grep, test_nested,squotes
#         #cat sequence piped, splitting
    
#     def test_tail(self):
#         cmdline = "tail test/text.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip().split("\n")
#         self.assertEqual(result, ['line2', 'line3'])
    
#     def test_heda(self):
#         cmdline = "head test/text.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip().split("\n")
#         self.assertEqual(result, ['line2', 'line3'])
    
#     def test_pipeSeq(self):
#         cmdline = "echo aaa > writeIn.txt; cat writeIn.txt  | uniq -i"
#         stdout = self.eval(cmdline)
#         result = stdout.strip().split("\n")
#         self.assertEqual(result, ["aaa", "aaa aaa aaa", "bbb"])

# class errorTesting(unittest.TestCase):

#     def test_cd_wrong_number_of_arguments(self):
#         cd_instance = Cd()
#         with self.assertRaises(ValueError) as context:
#             cd_instance.exec([])
#         self.assertEqual(str(context.exception), "wrong number of command line arguments")
    
#     def test_ls_file_not_found(self):
#         ls_instance = Ls()
#         with self.assertRaises(FileNotFoundError) as context:
#             ls_instance.exec(['nonexistent_directory'])
#         self.assertIn("No such file or directory", str(context.exception))

#     def test_ls_not_a_directory(self):
#         ls_instance = Ls()
#         temp_file = 'temp_file.txt'
#         Path(temp_file).touch()
#         with self.assertRaises(NotADirectoryError) as context:
#             ls_instance.exec([temp_file])
#         self.assertIn("Not a directory", str(context.exception))
#         Path(temp_file).unlink()  # Clean up
    
#     def test_cat_file_not_found(self):
#         cat_instance = Cat()
#         result = cat_instance.exec(['nonexistent_file.txt'])
#         self.assertIn("Error: File 'nonexistent_file.txt' not found", result)
    
#     def test_head_wrong_number_of_arguments(self):
#         head_instance = Head()
#         with self.assertRaises(ValueError) as context:
#             head_instance.exec([])
#         self.assertEqual(str(context.exception), "wrong number of command line arguments")

#     def test_head_wrong_flags(self):
#         head_instance = Head()
#         with self.assertRaises(ValueError) as context:
#             head_instance.exec(['-x', '5', 'file.txt'])
#         self.assertEqual(str(context.exception), "wrong flags")
    
#     def test_tail_wrong_number_of_arguments(self):
#         tail_instance = Tail()
#         with self.assertRaises(ValueError) as context:
#             tail_instance.exec([])
#         self.assertEqual(str(context.exception), "wrong number of command line arguments")

#     def test_unsafe_wrapper_error(self):
#         unsafe_instance = UnsafeWrapper(Uniq()) 
#         with self.assertRaises(ValueError) as context:
#             unsafe_instance.exec([])
#         self.assertIn("Error occurred:", str(context.exception))
    
#     def test_uniq_wrong_number_of_arguments(self):
#         uniq_instance = Uniq()
#         with self.assertRaises(ValueError) as context:
#             uniq_instance.exec(['-i'])
#         self.assertEqual(str(context.exception), "wrong number of command line arguments")
    
#     def test_grep_wrong_number_of_arguments(self):
#         grep_instance = Grep()
#         with self.assertRaises(ValueError) as context:
#             grep_instance.exec(['pattern'])
#         self.assertEqual(str(context.exception), "wrong number of command line arguments")
    
#     def test_head_wrong_number_of_arguments(self):
#         head_instance = Head()
#         with self.assertRaises(ValueError) as context:
#             head_instance.exec(['-n', '5'])
#         self.assertEqual(str(context.exception), "wrong number of command line arguments")

#     def test_tail_wrong_flags(self):
#         tail_instance = Tail()
#         with self.assertRaises(ValueError) as context:
#             tail_instance.exec(['-x', '10', 'file.txt'])
#         self.assertEqual(str(context.exception), "wrong flags")
    
#     def test_cat_empty_file_error(self):
#         cat_instance = Cat()
#         # Create an empty temporary file
#         temp_file = 'temp_empty_file.txt'
#         Path(temp_file).touch()
#         result = cat_instance.exec([temp_file])
#         self.assertIn(f"Error: Empty file '{temp_file}' detected", result)
#         Path(temp_file).unlink()  # Clean up

#     def test_cat_file_not_found_error(self):
#         cat_instance = Cat()
#         result = cat_instance.exec(['nonexistent_file.txt'])
#         self.assertIn("Error: File 'nonexistent_file.txt' not found", result)

#     def test_diff_wrong_number_of_arguments(self):
#         diff_instance = Diff()
#         with self.assertRaises(ValueError) as context:
#             diff_instance.exec(['string1'])
#         self.assertEqual(str(context.exception), "Two arguments are required for diff.")
    
#     def test_touch_no_arguments(self):
#         touch_instance = Touch()
#         with self.assertRaises(ValueError) as context:
#             touch_instance.exec([])
#         self.assertEqual(str(context.exception), "At least one argument is required for touch.")

#     def test_mkdir_no_arguments(self):
#         mkdir_instance = Mkdir()
#         with self.assertRaises(ValueError) as context:
#             mkdir_instance.exec([])
#         self.assertEqual(str(context.exception), "Wrong number of command line arguments")
    
#     def test_rmdir_no_arguments(self):
#         rmdir_instance = Rmdir()
#         with self.assertRaises(ValueError) as context:
#             rmdir_instance.exec([])
#         self.assertEqual(str(context.exception), "wrong number of command line arguments")

#     def test_find_non_directory_path(self):
#         find_instance = Find()
#         with self.assertRaises(ValueError) as context:
#             find_instance.exec(['nonexistentdir', '*.txt'])
#         self.assertEqual(str(context.exception), "path is not a directory")

# class TestShell(unittest.TestCase):

#     @classmethod
#     def eval(cls, cmdline):
#         # Use your run function here, make sure it returns the output as a string
#         output_deque = run(cmdline)
#         # Convert deque to string if necessary  
#         return ''.join(output_deque)
    
#     def test_cut_with_string(self):
#         cut_instance = Cut()
#         result = cut_instance.exec(['-b', '1-3', 'abc'])
#         self.assertEqual(result, 'abc\n')

    
#     def test_cut_specific_bytes_in_string(self):
#         cut_instance = Cut()
#         result = cut_instance.exec(['-b', '1-3', 'abcdefgh'])
#         self.assertEqual(result, 'abc\n')

#     def test_uniq_duplicate_line(self):
#         uniq_instance = Uniq()
#         result = uniq_instance.exec(['aaa\naaa\nbbb\naaa'])
#         self.assertEqual(result, 'aaa\nbbb\naaa\n')



    
#     # Unit testing for, WC, TOUCH, DIFF
#     # unittesting wc
#     # words
#     # lines

#     def test_wc_line_count(self):
#         cmdline = "wc -l 'one two three'"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, '1')
    
#     # chars
#     def test_wc_char_count(self):
#         cmdline = "wc -c 'one two three'"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, '13')

#     # file
#     def test_wc_word_count(self):
#         cmdline = "wc -w unittest1.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, '4')

#     # property based testing
#     def test_wc_word_property(self):
#         input_str = 'one two three'
#         cmdline = f"wc -w '{input_str}'"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         # only count the words in the input string
#         word_count = len(input_str.split())
#         self.assertEqual(result, str(word_count))

#     # mutation testing
#     def test_wc_word_count_mutation(self):
#         cmdline = "wc -w 'one two three'"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         mutated_result = int(result) + 1
#         self.assertNotEqual(mutated_result, '3')
    
#     # integration testing

#     def test_wc_pipe_file_to_string(self):
#         cmdline = "cat unittest1.txt | wc -w"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, '4')
    
#     def test_wc_pipe_string_to_file(self):
#         cmdline = "echo foo nam > newfile.txt| wc -w newfile.txt"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         self.assertEqual(result, '2')

#     # testing touch, property based
#     def test_touch_update_access_time(self):
#         filename = 'unittest1.txt'
#         old_access_time = os.path.getatime(filename)
#         sleep(1) # Sleep for 1 second to ensure the access time is different
#         cmdline = f"touch {filename}"
#         self.eval(cmdline)  
#         new_access_time = os.path.getatime(filename)
#         self.assertGreater(
#             new_access_time, old_access_time, "The access time was not updated."
#             )
    
#     def test_touch_create_file(self):
#         filename = "testfile.txt"
#         cmdline = f"touch {filename}"
#         self.eval(cmdline)
#         self.assertTrue(Path(filename).exists(), "The file was not created.")
#         Path(filename).unlink()

#     # testing diff
#     def test_diff_files(self):
#         cmdline = "diff unittest1.txt unittest2.txt"
#         result = self.eval(cmdline).strip()

#         expected_line1 = "-aaa aaa aaa"
#         expected_line2 = "-bbb"
#         expected_line3 = "+zzz zzz"
#         expected_line4 = "+ccc"
#         expected_line5 = "+ddd"

#         self.assertIn(expected_line1, result)
#         self.assertIn(expected_line2, result)
#         self.assertIn(expected_line3, result)
#         self.assertIn(expected_line4, result)
#         self.assertIn(expected_line5, result)
    
#     def test_diff_strings(self):
#         cmdline = "diff 'hello' 'hi'"
#         stdout = self.eval(cmdline)
#         result = stdout.strip()
#         expected_line1 = "-hello"
#         expected_line2 = "+hi"
#         self.assertIn(expected_line1, result)
#         self.assertIn(expected_line2, result)

#     def test_pipe_diff_files(self):
#         cmdline = "cat unittest1.txt | diff unittest2.txt"
#         result = self.eval(cmdline).strip()

#         expected_line1 = "-zzz zzz"
#         expected_line2 = "-ccc"
#         expected_line3 = "-ddd"
#         expected_line4 = "+aaa aaa aaa"
#         expected_line5 = "+bbb"

#         self.assertIn(expected_line1, result)
#         self.assertIn(expected_line2, result)
#         self.assertIn(expected_line3, result)
#         self.assertIn(expected_line4, result)
#         self.assertIn(expected_line5, result)

#     def test_pipe_diff_strings(self):
#         cmdline = "echo hello | diff 'hi'"
#         result = self.eval(cmdline).strip()
        
#         expected_line1 = "-hi"
#         expected_line2 = "+hello"
#         self.assertIn(expected_line1,result)
#         self.assertIn(expected_line2,result)

    

# if __name__ == '__main__':
#     unittest.main()
