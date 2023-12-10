import sys
sys.path.insert(0, '/Users/lukemciver/softwareEng/src')
sys.path.insert(0, '/Users/lukemciver/softwareEng/src/shell')

from collections import deque
import unittest
from shell import run

# Inside your TestShell class, you'll modify or add a new method to use your run function
class TestShell(unittest.TestCase):

    @classmethod
    def eval(cls, cmdline):
        # Use your run function here, make sure it returns the output as a string
        output_deque = run(cmdline)
        # Convert deque to string if necessary  
        return ''.join(output_deque)
    
    #new funcs testing
    def test_wc(self):
        cmdline = 'wc -w "gi gi gi"'
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, "abc")

    def test_substitution(self):
        cmdline = "echo `echo foo`"
        stdout = self.eval(cmdline)
        result = stdout.strip()
        self.assertEqual(result, "foo")

    if __name__ == "__main__":
        unittest.main()
