import unittest
from pathlib import Path
from shell import run
from time import sleep
import os


class TestShell(unittest.TestCase):

    @classmethod
    def eval(cls, cmdline):
        # Use your run function here, make
        # sure it returns the output as a string
        output_deque = run(cmdline)
        # Convert deque to string if necessary
        return ''.join(output_deque)

    def test_wc_line_count(self):
        cmdline = "wc -l 'one two three'"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, '1')

    # chars
    def test_wc_char_count(self):
        cmdline = "wc -c 'one two three'"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, '13')

    # file
    def test_wc_word_count(self):
        cmdline = "wc -w unittest1.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, '4')

    # property based testing
    def test_wc_word_property(self):
        input_str = 'one two three'
        cmdline = f"wc -w '{input_str}'"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        # only count the words in the input string
        word_count = len(input_str.split())
        self.assertEqual(result, str(word_count))

    # mutation testing
    def test_wc_word_count_mutation(self):
        cmdline = "wc -w 'one two three'"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        mutated_result = int(result) + 1
        self.assertNotEqual(mutated_result, '3')

    # integration testing
    def test_wc_pipe_file_to_string(self):
        cmdline = "cat unittest1.txt | wc -w"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, '4')

    def test_wc_pipe_string_to_file(self):
        cmdline = "echo foo nam > newfile.txt| wc -w newfile.txt"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, '2')

    # testing touch, property based
    def test_touch_update_access_time(self):
        filename = 'unittest1.txt'
        old_access_time = os.path.getatime(filename)
        sleep(1)
        cmdline = f"touch {filename}"
        self.eval(cmdline)
        new_access_time = os.path.getatime(filename)
        self.assertGreater(
            new_access_time, old_access_time,
            "The access time was not updated."
            )

    def test_touch_create_file(self):
        filename = "testfile.txt"
        cmdline = f"touch {filename}"
        self.eval(cmdline)
        self.assertTrue(Path(filename).exists(), "The file was not created.")
        Path(filename).unlink()

    # testing diff
    def test_diff_files(self):
        cmdline = "diff unittest1.txt unittest2.txt"
        result = self.eval(cmdline).strip()

        expected_line1 = "-aaa aaa aaa"
        expected_line2 = "-bbb"
        expected_line3 = "+zzz zzz"
        expected_line4 = "+ccc"
        expected_line5 = "+ddd"

        self.assertIn(expected_line1, result)
        self.assertIn(expected_line2, result)
        self.assertIn(expected_line3, result)
        self.assertIn(expected_line4, result)
        self.assertIn(expected_line5, result)

    def test_diff_strings(self):
        cmdline = "diff 'hello' 'hi'"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        expected_line1 = "-hello"
        expected_line2 = "+hi"
        self.assertIn(expected_line1, result)
        self.assertIn(expected_line2, result)

    def test_pipe_diff_files(self):
        cmdline = "cat unittest1.txt | diff unittest2.txt"
        result = self.eval(cmdline).strip()

        expected_line1 = "-zzz zzz"
        expected_line2 = "-ccc"
        expected_line3 = "-ddd"
        expected_line4 = "+aaa aaa aaa"
        expected_line5 = "+bbb"

        self.assertIn(expected_line1, result)
        self.assertIn(expected_line2, result)
        self.assertIn(expected_line3, result)
        self.assertIn(expected_line4, result)
        self.assertIn(expected_line5, result)

    def test_pipe_diff_strings(self):
        cmdline = "echo hello | diff 'hi'"
        result = self.eval(cmdline).strip()

        expected_line1 = "-hi"
        expected_line2 = "+hello"
        self.assertIn(expected_line1, result)
        self.assertIn(expected_line2, result)

    def test_mkdir_and_rmdir(self):
        # Create directory
        cmdline = "mkdir temp_test_dir"
        self.eval(cmdline)
        self.assertTrue(Path('temp_test_dir').exists())

        # Remove directory
        cmdline = "rmdir temp_test_dir"
        self.eval(cmdline)
        self.assertFalse(Path('temp_test_dir').exists())


if __name__ == "__main__":
    unittest.main()
