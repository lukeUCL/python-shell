import sys
sys.path.insert(0, '/Users/lukemciver/softwareEng/src')
sys.path.insert(0, '/Users/lukemciver/softwareEng/src/shell')

from shell import run
import unittest
from collections import deque

# Inside your TestShell class, you'll modify or add a new method to use your run function
class TestShell(unittest.TestCase):

    @classmethod
    def eval(cls, cmdline, shell="/comp0010/sh"):
        # Use your run function here, make sure it returns the output as a string
        output_deque = run(cmdline)
        # Convert deque to string if necessary  
        return ''.join(output_deque)
    
    # # def test_substitution(self):
    # #         cmdline = "echo `echo foo`"
    # #         stdout = self.eval(cmdline)
    # #         result = stdout.strip()
    # #         self.assertEqual(result, "foo")

    # #lets jsut make, concats as aBACKQUOTEDa- and then process backquote in args asw.
    # #make process backquotes a universal call in flattening
    # # def test_substitution_insidearg(self):
    # #     cmdline = "echo a`echo a`a"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip()
    # #     self.assertEqual(result, "aaa")

    # # def test_substitution_splitting(self):
    # #     cmdline = "echo `echo foo  bar`"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip()
    # #     self.assertEqual(result, "foo bar")

    # # # def test_substitution_wc_find(self):
    # # #     cmdline = "wc -l `find -name '*.txt'`"
    # # #     stdout = self.eval(cmdline)
    # # #     result = stdout.strip()
    # # #     self.assertEqual(result, "26")

    # # def test_substitution_sort_find(self):
    # #     cmdline = "cat `find dir2 -name '*.txt'` | sort"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip().split("\n")
    # #     self.assertEqual(result, ["AAA", "AAA", "aaa"])

    # # def test_substitution_semicolon(self):
    # #     cmdline = "echo `echo foo; echo bar`"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip()
    # #     self.assertEqual(result, "foo bar")

    # # def test_substitution_keywords(self):
    # #     cmdline = "echo `cat test.txt`"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip()
    # #     self.assertEqual(result, "''")

    # # def test_substitution_app(self):
    # #     cmdline = "`echo echo` foo"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip()
    # #     self.assertEqual(result, "foo")

    # # def test_singlequotes(self):
    # #     cmdline = "echo 'a  b'"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip()
    # #     self.assertEqual(result, "a  b")

    # # def test_quote_keyword(self):
    # #     cmdline = "echo ';'"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip()
    # #     self.assertEqual(result, ";")

    # def test_doublequotes(self):
    #     cmdline = 'echo "a  b"'
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, "a  b")

    # def test_substitution_doublequotes(self):
    #     cmdline = 'echo "`echo foo`"'
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, "foo")

    # def test_nested_doublequotes(self):
    #     cmdline = 'echo "a `echo "b"`"'
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, "a b")

    # def test_disabled_doublequotes(self):
    #     cmdline = "echo '\"\"'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, '""')

    # def test_splitting(self):
    #     cmdline = 'echo a"b"c'
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, "abc")

    
    # # def test_cat_stdin(self):
    # #     cmdline = "cat < dir1/file1.txt"
    # #     stdout = self.eval(cmdline)
    # #     result = stdout.strip().split("\n")
    # #     self.assertEqual(result, ["AAA", "BBB", "AAA"])


    # def test_cat_stdin(self):
    #     cmdline = "cat < dir1/file1.txt"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip().split("\n")
    #     self.assertEqual(result, ["AAA", "BBB", "AAA"])

    # def test_unsafe_ls(self):
    #     cmdline = "_ls dir3; echo AAA > newfile.txt"
    #     self.eval(cmdline)
    #     stdout = self.eval("cat newfile.txt", shell="/bin/bash")
    #     result = stdout.strip()
    #     self.assertEqual(result, "AAA")

    # def test_cut_union(self):
    #     cmdline = "echo abc | cut -b -1,2-"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, "abc")

    # def test_cut_stdin(self):
    #     cmdline = "echo abc | cut -b 1"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip()
    #     self.assertEqual(result, "a")

    # def test_grep_stdin(self):
    #     cmdline = "cat dir1/file1.txt dir1/file2.txt | grep '...'"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip().split("\n")
    #     self.assertEqual(result, ["AAA", "BBB", "AAA", "CCC"])

        #["AAA", "BBB", "AAA", "CCC"] this is the cat output, we know this

    def test_pipe_uniq(self):
        cmdline = (
            "uniq -i AAA\nBBB\nAAA\naaa "
        )
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ["AAA", "BBB", "AAA"])

            #["AAA", "BBB", "AAA", "aaa", "CCC"] this is the cat output 

    def test_pipe_uniq(self):
        cmdline = (
            "uniq -i "'AAA', 'BBB', 'AAA', 'aaa'""
        )
        stdout = self.eval(cmdline)
        result = stdout.strip().split("\n")
        self.assertEqual(result, ["AAA", "BBB", "AAA"])
        #['AAA', 'BBB', 'AAA', 'aaa']

    # def test_pipe_chain_sort_uniq(self):
    #     cmdline = "cat dir1/file1.txt dir1/file2.txt | sort | uniq"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip().split("\n")
    #     self.assertEqual(result, ["AAA", "BBB", "CCC"])

    # def test_sort_uniq(self):
    #     cmdline = "sort dir1/file1.txt | uniq"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip().split("\n")
    #     self.assertEqual(result, ["AAA", "BBB"])

        
    # def test_cat(self):
    #     cmdline = "cat dir1/file1.txt dir1/file2.txt"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip().split("\n")
    #     self.assertEqual(result, ["AAA", "BBB", "AAA", "CCC"])

    # def test_cat_stdin(self):
    #     cmdline = "cat < dir1/file2.txt"
    #     stdout = self.eval(cmdline)
    #     result = stdout.strip().split("\n")
    #     self.assertEqual(result, ["AAA", "BBB", "AAA"])



#file 2 ['CCC']
#file1["AAA", "BBB", "AAA"])

if __name__ == "__main__":
    unittest.main()
