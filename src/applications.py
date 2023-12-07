import os
import re
import sys
from abc import ABC, abstractmethod
from os import listdir
from collections import deque
from typing import List


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
        files = args[1:]
        result = ""

        for file in files:
            with open(file) as f:
                lines = f.readlines()
                for line in lines:
                    if re.match(pattern, line):
                        if len(files) > 1:
                            result += f"{file}:{line}"
                        else:
                            result += line

        return result

class Find(Application):
    def exec(self, args):#prints the path to the file 
        out = deque()
        res = ''
        #expects input directory "-name" filename.type
        initial_dir = os.getcwd()
        subdirectories = deque()
        path = args[0]
        if len(path) == 1:
            if path == '~': #all files in home of type
                os.chdir(os.path.expanduser("~"))
            else:
                raise ValueError('wrong command')
        else:
            if path[0:2] == './' or path[0] == '/': #all files in current directory
                os.chdir(path[2:])
            else:
                raise ValueError('wrong command')
        #now we are in the correct start directory, begin searching
        for f in listdir(os.getcwd()):
            if not f.startswith("."):
                if '.' in f:
                    if f[-len(args[2]):] == args[2]:
                        out.append(f)
                else: #is a subdirectory
                    subdirectories.append(os.getcwd + f)
        while len(subdirectories) > 0:
            os.chdir(subdirectories.pop())
            for f in listdir(os.getcwd()):
                if not f.startswith("."):
                    if '.' in f:
                        if f[-len(args[2]):] == args[2]:
                            out.append(f)
                    else: #is a subdirectory
                        subdirectories.append(os.getcwd + f)       
        os.chdir(initial_dir)
        return "".join(out)


    
class Uniq(Application):
    def exec(self, args):
        #print('here')
        #return 'here'
        out = deque()
        res = ''
        if len(args) > 2 or len(args) < 1:
            raise ValueError("wrong number of command line arguements")
        ignoreCase = args[0] == '-i'
        if ignoreCase and len(args) == 2:
            file = args[1]
        elif not ignoreCase and len(args) == 1:
            file = args[0]
        ready = False
        temp = None
        line = None
        copy = None
        count = 0
        with open(file) as f:
            for l in f:
                copy = str(l)
                if ignoreCase:
                    line = l.lower()
                else:
                    line = l

                if not ready:
                    temp = line
                    ready = True
                    out.append(copy)
                    count += 1
                    continue
                else:
                    if temp != line:
                        out.append(copy)
                        temp = line
                        count += 1
        if count == 0 and copy is not None:
            out.append(copy)
        if line != temp and copy is not None:
            out.append(copy)
        return "".join(out)

                    

            
class Cut(Application):
    def exec(self, args):
        out = deque()
        if len(args) < 3:
            raise ValueError("wrong number of command line arguements")
        options, file = args[:-1], args[-1]
        if options[0] != '-b' or len(options) < 2:
            raise ValueError("incorrect input")
        options = options[1].split(',')
        #return str(options)
        #finish implementing by going through fn byte by byte per line
        with open(file) as f:
            for line in f:
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
                        out.append(line[int(option)] + '\n')
                #out.append(toAdd)
        return "".join(out)
       
class Sort(Application):
    def exec(self, args):
        res = ''
        out = deque()
        if len(args) > 2:
            raise ValueError("wrong number of command line arguments")
        reverse = (args[0] == "-r")
        if reverse and len(args) == 2:
            file = args[1]
        elif not reverse and len(args) == 1:
            file = args[0]
        else:
            raise ValueError("wrong number of command line arguements")
        res = []
        with open(file, "r") as f:
            for line in f:
                res.append(line)
        res.sort()
        if reverse:
            res.reverse()
        for elem in res:
            out.append(elem)
        return "".join(out)



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
        }

        actual_name = app_name[1:] if app_name.startswith("_") else app_name
        if actual_name not in app_types:
            raise ValueError(f"Invalid application name: {app_name}")
        
        app_instance = app_types[actual_name]()
        return UnsafeWrapper(app_instance) if app_name.startswith("_") else app_instance