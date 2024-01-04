import unittest
from applications import Cd, Ls, Cat, Head, Tail, Grep, Diff, Touch, Mkdir, Rmdir, ApplicationFactory
from pathlib import Path

class errorTesting(unittest.TestCase):

    def test_cd_wrong_number_of_arguments(self):
        cd_instance = Cd()
        with self.assertRaises(ValueError) as context:
            cd_instance.exec([])
        self.assertEqual(str(context.exception), "wrong number of command line arguments")

    def test_ls_file_not_found(self):
        ls_instance = Ls()
        with self.assertRaises(FileNotFoundError) as context:
            ls_instance.exec(['nonexistent_directory'])
        self.assertIn("No such file or directory", str(context.exception))

    def test_ls_not_a_directory(self):
        ls_instance = Ls()
        temp_file = 'temp_file.txt'
        Path(temp_file).touch()
        with self.assertRaises(NotADirectoryError) as context:
            ls_instance.exec([temp_file])
        self.assertIn("Not a directory", str(context.exception))
        Path(temp_file).unlink()  # Clean up

    def test_cat_file_not_found(self):
        cat_instance = Cat()
        result = cat_instance.exec(['nonexistent_file.txt'])
        self.assertIn("Error: File 'nonexistent_file.txt' not found", result)

    def test_head_wrong_flags(self):
        head_instance = Head()
        with self.assertRaises(ValueError) as context:
            head_instance.exec(['-x', '5', 'file.txt'])
        self.assertEqual(str(context.exception), "wrong flags")

    def test_tail_wrong_number_of_arguments(self):
        tail_instance = Tail()
        with self.assertRaises(ValueError) as context:
            tail_instance.exec([])
        self.assertEqual(str(context.exception), "wrong number of command line arguments")

    def test_grep_wrong_number_of_arguments(self):
        grep_instance = Grep()
        with self.assertRaises(ValueError) as context:
            grep_instance.exec(['pattern'])
        self.assertEqual(str(context.exception), "wrong number of command line arguments")

    def test_head_wrong_number_of_arguments(self):
        head_instance = Head()
        with self.assertRaises(ValueError) as context:
            head_instance.exec(['-n', '5'])
        self.assertEqual(str(context.exception), "wrong number of command line arguments")

    def test_tail_wrong_flags(self):
        tail_instance = Tail()
        with self.assertRaises(ValueError) as context:
            tail_instance.exec(['-x', '10', 'file.txt'])
        self.assertEqual(str(context.exception), "wrong flags")

    def test_cat_empty_file_error(self):
        cat_instance = Cat()
        # Create an empty temporary file
        temp_file = 'temp_empty_file.txt'
        Path(temp_file).touch()
        result = cat_instance.exec([temp_file])
        self.assertIn(f"Error: Empty file '{temp_file}' detected", result)
        Path(temp_file).unlink()  # Clean up

    def test_cat_file_not_found_error(self):
        cat_instance = Cat()
        result = cat_instance.exec(['nonexistent_file.txt'])
        self.assertIn("Error: File 'nonexistent_file.txt' not found", result)

    def test_diff_wrong_number_of_arguments(self):
        diff_instance = Diff()
        with self.assertRaises(ValueError) as context:
            diff_instance.exec(['string1'])
        self.assertEqual(str(context.exception), "Two arguments are required for diff.")

    def test_touch_no_arguments(self):
        touch_instance = Touch()
        with self.assertRaises(ValueError) as context:
            touch_instance.exec([])
        self.assertEqual(str(context.exception), "At least one argument is required for touch.")

    def test_mkdir_no_arguments(self):
        mkdir_instance = Mkdir()
        with self.assertRaises(ValueError) as context:
            mkdir_instance.exec([])
        self.assertEqual(str(context.exception), "Wrong number of command line arguments")

    def test_rmdir_no_arguments(self):
        rmdir_instance = Rmdir()
        with self.assertRaises(ValueError) as context:
            rmdir_instance.exec([])
        self.assertEqual(str(context.exception), "wrong number of command line arguments")

    def test_cd_no_args(self):
        with self.assertRaises(ValueError):
            Cd().exec([])

    def test_cd_many_args(self):
        with self.assertRaises(ValueError):
            Cd().exec(["dir1", "dir2"])

    def test_ls_non_existent_directory(self):
        with self.assertRaises(FileNotFoundError):
            Ls().exec(["nonexistentdir"])

    def test_ls_file_instead_of_directory(self):
        with self.assertRaises(FileNotFoundError):
            Ls().exec(["file.txt"])

    def test_invalid_application_name(self):
        with self.assertRaises(ValueError) as context:
            ApplicationFactory.create_application("invalid_app")
        self.assertTrue("Invalid application name: invalid_app" in str(context.exception))