import os
import re
from abc import ABC, abstractmethod
from os import listdir
from collections import deque

class Application(ABC):  

    @abstractmethod
    def exec(self, args):
        pass

class Pwd(Application):
    def exec(self, args):
        return os.getcwd()

class Cd(Application):
    def exec(self, args):
        if len(args) != 1:
            raise ValueError("wrong number of command line arguments")
        os.chdir(args[0])
        return ""

class Echo(Application):   
    def exec(self, args):
        return " ".join(args) + "\n"
    
class Ls(Application):   
    def exec(self, args):
        if len(args) == 0:
            ls_dir = os.getcwd()
        elif len(args) == 1:
            ls_dir = args[0]
        else:
            raise ValueError("wrong number of command line arguments")
        
        files = [f for f in listdir(ls_dir) if not f.startswith(".")]
        return "\n".join(files) + "\n"
    
class Cat(Application):   
    def exec(self, args):
        result = ""
        for a in args:
            with open(a) as f:
                result += f.read()
        return result
 
class Head(Application):   
    def exec(self, args):
        if len(args) != 1 and len(args) != 3:
            raise ValueError("wrong number of command line arguments")
        
        if len(args) == 1:
            num_lines = 10
            file = args[0]
        elif len(args) == 3:
            if args[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]

        with open(file) as f:
            lines = f.readlines()
            return "".join(lines[:min(len(lines), num_lines)])
    
class Tail(Application):   
    def exec(self, args):
        #return 'here'
        if len(args) != 1 and len(args) != 3:
            raise ValueError("wrong number of command line arguments")
        
        if len(args) == 1:
            num_lines = 10
            file = args[0]
        elif len(args) == 3:
            if args[0] != "-n":
                raise ValueError("wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]

        with open(file) as f:
            lines = f.readlines()
            display_length = min(len(lines), num_lines)
            return "".join(lines[len(lines) - display_length:])

class Grep(Application):   
    def exec(self, args):
        if len(args) < 2:
            raise ValueError("wrong number of command line arguments")
        
        pattern = args[0]
        input = args[1:]
        result = ""

        def grep(lines, file=False, filename=""):
            grep_result = ""
            for line in lines:
                if re.search(pattern, line):
                    if file:
                        grep_result += f"{filename}:{line}"
                    else:
                        grep_result += line
            return grep_result

        if all(os.path.isfile(file) for file in input):
            for file in input:
                with open(file, "r") as f:
                    #check line by line 
                    lines = f.readlines()
                    #only need fileName when we have multiple files
                    result += grep(lines, file=(len(input) > 1), filename=file)

        #strings, just directly process
        else:
            result = grep(input)

        return result


class Find(Application):
    def exec(self, args):
        out = deque()
        cwdRoot = False
        if len(args) > 3 or len(args) < 2:
            raise ValueError("wrong number of command line arguments")
        if len(args) == 2:
            cwdRoot = True
            path = os.getcwd()
            pattern = args[1]
        else:
            path = args[0]
            pattern = args[2]

        if not os.path.isdir(path):
            raise ValueError("path is not a directory")
        self.search(path, pattern, out)
        if cwdRoot:
            res = deque()
            while len(out) > 0:
                res.append('.' + out.pop()[len(os.getcwd()):])
            out = res
        return "".join(out)
    
    def search(self, path, pattern, out):
        if not os.path.isdir(path):
            raise ValueError("path is not a directory")
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                self.search(os.path.join(path, file), pattern, out)
            else:
                if file == pattern or (pattern[0:2] == "'*" and file.endswith(pattern[1:-1])):
                    out.append(os.path.join(path, file))

class Uniq(Application):
    def exec(self, args):
        out = deque()
        if len(args) > 2 or len(args) < 1:
            raise ValueError("wrong number of command line arguments")  
        if args[0] == '-i':
            ignoreCase=True
        else:
            ignoreCase=False
        input_source = args[-1]

        def process_line(line, last_line):
            normalized_line = line.lower() if ignoreCase else line
            if normalized_line != last_line:
                #split by \n in pipe strings 
                out.append(line if line.endswith('\n') else line + '\n')
                return normalized_line
            return last_line

        last_line = None
        if os.path.isfile(input_source):
            with open(input_source) as f:
                for line in f:
                    last_line = process_line(line, last_line)
        else:
            lines = input_source.split('\n')
            for line in lines:
                last_line = process_line(line, last_line)

        return ''.join(out)

#some hardcoding here..? when we have -b 1, with a string, we should return 0 index, not 1 index so code doesnt work - just changred it to 
#option-1..?

class Cut(Application):

    def exec(self, args):
        out = deque()
        if len(args) < 3:
            raise ValueError("wrong number of command line arguements")
        options, input = args[:-1], args[-1]
        if options[0] != '-b' or len(options) < 2:
            raise ValueError("incorrect input")
        options = options[1].split(',')


        def cutProcess(input, File):
            if File:
                input = open(input)
             
            #for strings passed by pipe, we want to consider each string as a single element, so we'll nest them 
            else:
                input = [[segment] for segment in input.split('\n')]
                #remove empty string
                input = input[:-1]

            for line in input:

                overlapStart = False
                for option in options:
                    index = option.find('-')
                    if index != -1:
                        if option[0] == '-':
                                for elem in line[:int(option[1:])]:
                                    out.append(elem + '\n')
                        elif option[-1] == '-' and not overlapStart:
                            overlapStart = True
                            for elem in line[int(option[:-1]) - 1:]:
                                out.append(elem)
                        elif option[-1] != '-':#option is specifcying a range
                            out.append(line[int(option[:index]) - 1:int(option[index + 1:])] + '\n')
                    else:#just wants those specific bytes
                        if not File:
                            #adjust bytes to string index
                            option = str(int(option) - 1)
                            #extract string from square brackets
                            line = line[0]
                        out.append(line[int(option)] + '\n')
                #out.append(toAdd)
            return "".join(out)

        #when we split the input(string) it will be a list, i,e .split('\n') -> 'abc' -> ['abc', '']
        #this caused issues with particualar bytes, so we will just take the string at that section

        if os.path.isfile(input): 
            return cutProcess(input, True)
        else:
            return cutProcess(input, False)
        

class Sort(Application):
    def exec(self, args):
        out = deque()
        if len(args) > 2:
            raise ValueError("wrong number of command line arguments")
        
        reverse = (args[0] == "-r")

        if reverse and len(args) == 2:
            input = args[1]
        elif not reverse and len(args) == 1:
            input = args[0]
        else:
            raise ValueError("wrong number of command line arguments")
        
        res = []
        
        def sortInput(input,File):
            for line in input:
                res.append(line)
            res.sort()
            if reverse:
                res.reverse()
            for elem in res:
                out.append(elem) if File else out.append(elem+'\n')
            return "".join(out)
            
        if os.path.isfile(input):
            input = open(input, "r")
            return sortInput(input,File=True)
        else:
            input = input.split('\n')
            return sortInput(input,File=False)

class Wc(Application):

    def exec(self, args):
        if len(args) != 2:
            raise ValueError("wc expects exactly one argument for file or string input")

        option, input_source = args
        if option not in ['-l', '-w', '-c']:
            raise ValueError("wc expects an option -l (lines), -w (words), or -c (characters)")

        if os.path.isfile(input_source):
            with open(input_source, 'r') as file:
                content = file.read()
        else:
            content = input_source

        if option == '-l':
            return str(self.countLines(content))
        elif option == '-w':
            return str(self.countWords(content))
        elif option == '-c':
            return str(self.countChars(content))

    def countLines(self, content):
        a= content.count('\n')
        print(a)

    def countWords(self, content):
        return len(content.split())

    def countChars(self, content):
        return len(content)

import difflib

class Diff:
    def exec(self, args):
        #arg checking
        if len(args) != 2:
            raise ValueError("Two arguments are required for diff.")
        
        #content to compare
        content1 = self.getContent(args[0])
        content2 = self.getContent(args[1])

        diff = self.computeDiff(content1, content2)
        return self.join(diff)

    def getContent(self, source):
        if os.path.isfile(source):
            with open(source, 'r') as file:
                return file.readlines()
        #string case
        else:
            return source.splitlines()

    def computeDiff(self, content1, content2):
        # difflib to check file diff
        diff = difflib.unified_diff(content1, content2, lineterm='')
        return list(diff)

    def join(self, diff):
        return '\n'.join(diff)
    
from pathlib import Path

class Touch:
    def exec(self, args):
        #arg checking
        if len(args) < 1:
            raise ValueError("At least one argument is required for touch.")
        
        for file_path in args:
            self._touch_file(file_path)
    
    def _touch_file(self, file_path):
        path = Path(file_path)
        path.touch(exist_ok=True)

class UnsafeWrapper(Application):
    def __init__(self, app):
        self._app = app

    def exec(self, args):
        try:
            return self._app.exec(args)
        except Exception as e:
            return f"Error occurred: {str(e)}\n"


class ApplicationFactory:
    @staticmethod
    def create_application(app_name: str) -> Application:
        app_types = {
            "pwd": Pwd,
            "cd": Cd,
            "echo": Echo,
            "ls": Ls,
            "cat": Cat,
            "head": Head,
            "tail": Tail,
            "grep": Grep,
            "find": Find,
            "uniq": Uniq,
            "sort": Sort,
            "cut": Cut,
            "wc": Wc,
            "diff": Diff,
            "touch": Touch,
        }

        actual_name = app_name[1:] if app_name.startswith("_") else app_name
        if actual_name not in app_types:
            raise ValueError(f"Invalid application name: {app_name}")
        
        app_instance = app_types[actual_name]()
        return UnsafeWrapper(app_instance) if app_name.startswith("_") else app_instance