import unittest
from applications import Sort, Find, Uniq, Cut

'''text.txt contains:
hello world
corgito ergo sum
i think therefore i am'''


class TestCut(unittest.TestCase):

    def test_one(self):

        # print('dir', os.getcwd(), os.listdir())
        self.assertEqual(Cut().exec(['-b', '1', 'test/text.txt']).rstrip().
                         split('\n'), ["h", "c", "i"])

    def test_range(self):

        self.assertEqual(Cut().exec(['-b', '1-2', 'test/text.txt'])
                         .rstrip().split('\n'), ["he", "co", "i"])

    # test that if length of arg is less than 3 then value error is raised
    def test_less_than_3(self):

        with self.assertRaises(ValueError):
            Cut().exec(['-b', 'test/text.txt'])

    # test that the first element of arg isnt -b then value error is raised
    def test_first_element(self):

        with self.assertRaises(ValueError):
            Cut().exec(['-a', '1-2', 'test/text.txt'])

    # test range where second element
    # begins with -3 that cut functions correctly
    def test_range4(self):

        self.assertEqual(Cut().exec(['-b', '-3', 'test/text.txt']).
                         rstrip().split('\n'), ["hel", "cor", "i t"])

    def test_range5(self):

        self.assertEqual(Cut().exec(['-b', '7-', 'test/text.txt']).
                         rstrip().split('\n'),
                         ["world", "o ergo sum", "k therefore i am"])


class testSort(unittest.TestCase):
    # test that sort sorts the file correctly
    def test_sort_file(self):

        self.assertEqual(Sort().exec(['test/text.txt']).
                         rstrip().split('\n'),
                         ["corgito ergo sum", "hello world",
                         "i think therefore i am"])

    def test_sort_array(self):

        self.assertEqual(Sort().exec(['hello\nworld\ncorgito']).
                         rstrip().split('\n'),
                         ["corgito", "hello", "world"])

    # test sort with -r flag
    def test_sort_file_r(self):

        self.assertEqual(Sort().exec(['-r', 'test/text.txt']).
                         rstrip().split('\n'),
                         ["i think therefore i am", "hello world",
                         "corgito ergo sum"])

    # test for arg length less than 2
    def test_less_than_3(self):

        with self.assertRaises(ValueError):
            Sort().exec(['test/text.txt', 'test/text.txt',
                          'test/text.txt'])


class testUniq(unittest.TestCase):
    # test that uniq removes duplicates
    def test_uniq(self):

        self.assertEqual(Uniq().exec(['test/text.txt']).rstrip().split('\n'),
                         ["hello world", "corgito ergo sum",
                          "i think therefore i am"])

    # test that uniq removes duplicates with -i flag
    def test_uniq_i(self):

        self.assertEqual(Uniq().exec(['-i', 'test/texti.txt'])
                         .rstrip().split('\n'),
                         ["Hello world", "corgito eGo sum",
                         "i think therefore i aM"])


class testFind(unittest.TestCase):
    # test that find finds the correct file
    def test_find(self):

        self.assertEqual(Find().exec(['test', '-name', 'text.txt']).
                         rstrip().split('\n'),
                         ["test/text.txt"])

    # test that find finds the correct file with -name flag
    def test_find_name(self):

        self.assertEqual(Find().exec(['-name', 'text.txt']).
                         rstrip().split('\n'),
                         ["./test/text.txt"])

    # test that find raises value error if arg length is less than 2
    def test_less_than_2(self):

        with self.assertRaises(ValueError):
            Find().exec(['test/text.txt'])


if __name__ == "__main__":
    unittest.main()
