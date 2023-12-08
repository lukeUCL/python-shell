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
        
# class Grep(Application):   
#     def exec(self, args):
#         if len(args) < 2:
#             raise ValueError("wrong number of command line arguments")
        
#         pattern = args[0]
#         files = args[1:]
#         result = ""
    
#         for file in files:
#             with open(file) as f:
#                 lines = f.readlines()
#                 for line in lines:
#                     if re.match(pattern, line):
#                         if len(files) > 1:
#                             result += f"{file}:{line}"
#                         else:
#                             result += line

#         return result

class Grep(Application):   
    def exec(self, args):
        if len(args) < 2:
            raise ValueError("wrong number of command line arguments")
        
        pattern = args[0]
        input = args[1:]
        result = ""

        #adding check for files vs strings from pipes
        #pipe input -> [aaa,bbb,ccc] etc, files [file1,file2] etc
        #we could just do this check in the for loop
        #but i dont think theres ever mix of strings and files so shud be fine
        files = True
        for file in input:
            if not os.path.isfile(file): 
                files = False

        if files:
            for file in input:
                with open(file) as f:
                    lines = f.readlines()
                    for line in lines:
                        if re.match(pattern, line):
                            if len(input) > 1:
                                result += f"{file}:{line}"
                            else:
                                result += line
        else:
            for segment in input:
                if re.match(pattern, segment):
                    result += segment

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


    
# class Uniq(Application):
#     def exec(self, args):
#         #print('here')
#         #return 'here'
#         out = deque()
#         res = ''
#         if len(args) > 2 or len(args) < 1:
#             raise ValueError("wrong number of command line arguements")
#         ignoreCase = args[0] == '-i'
#         if ignoreCase and len(args) == 2:
#             file = args[1]
#         elif not ignoreCase and len(args) == 1:
#             file = args[0]
#         ready = False
#         temp = None
#         line = None
#         copy = None
#         count = 0
#         with open(file) as f:
#             for l in f:
#                 copy = str(l)
#                 if ignoreCase:
#                     line = l.lower()
#                 else:
#                     line = l

#                 if not ready:
#                     temp = line
#                     ready = True
#                     out.append(copy)
#                     count += 1
#                     continue
#                 else:
#                     if temp != line:
#                         out.append(copy)
#                         temp = line
#                         count += 1
#         if count == 0 and copy is not None:
#             out.append(copy)
#         if line != temp and copy is not None:
#             out.append(copy)
#         return "".join(out)

# class Uniq(Application):
#     def exec(self, args):
#         #print('here')
#         #return 'here'
#         out = deque()
#         if len(args) > 2 or len(args) < 1:
#             raise ValueError("wrong number of command line arguements")
#         ignoreCase = args[0] == '-i'
#         if ignoreCase and len(args) == 2:
#             input = args[1]
#         elif not ignoreCase and len(args) == 1:
#             input = args[0]
#         ready = False
#         temp = None
#         line = None
#         copy = None
#         count = 0
#         if os.path.isfile(input):
#             with open(input) as f:
#                 for l in f:
#                     copy = str(l)
#                     if ignoreCase:
#                         line = l.lower()
#                     else:
#                         line = l

#                     if not ready:
#                         temp = line
#                         ready = True
#                         out.append(copy)
#                         count += 1
#                         continue
#                     else:
#                         if temp != line:
#                             out.append(copy)
#                             temp = line
#                             count += 1
#             if count == 0 and copy is not None:
#                 out.append(copy)
#             if line != temp and copy is not None:
#                 out.append(copy)
#         else:
#             #if we have a string, we need to split it by newlines
#             #and then check for uniq lines
#             #this is because we are checking for uniq lines, not uniq characters
#             input = input.split('\n')
#             for l in input:
#                 copy = str(l)
#                 if ignoreCase:
#                     line = l.lower()
#                 else:
#                     line = l

#                 if not ready:
#                     temp = line
#                     ready = True
#                     out.append(copy)
#                     count += 1
#                     continue
#                 else:
#                     if temp != line:
#                         out.append(copy)
#                         temp = line
#                         count += 1
#             if count == 0 and copy is not None:
#                 out.append(copy)
#             if line != temp and copy is not None:
#                 out.append(copy)
#         return "".join(out)

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


# class Cut(Application):
#     def exec(self, args):
#         out = deque()
#         if len(args) < 3:
#             raise ValueError("wrong number of command line arguements")
#         options, file = args[:-1], args[-1]
#         if options[0] != '-b' or len(options) < 2:
#             raise ValueError("incorrect input")
#         options = options[1].split(',')
#         #return str(options)
#         #finish implementing by going through fn byte by byte per line
#         with open(file) as f:
#             for line in f:
#                 overlapStart = False
#                 for option in options:
#                     index = option.find('-')
#                     if index != -1:
#                         if option[0] == '-':
#                             for elem in line[:int(option[1:])]:
#                                 out.append(elem + '\n')
#                         elif option[-1] == '-' and not overlapStart:
#                             overlapStart = True
#                             for elem in line[int(option[:-1]) - 1:]:
#                                 out.append(elem)
#                         elif option[-1] != '-':#option is specifcying a range
#                             out.append(line[int(option[:index]) - 1:int(option[index + 1:])] + '\n')
#                     else:#just wants those specific bytes
#                         out.append(line[int(option)] + '\n')
#                 #out.append(toAdd)
#         return "".join(out)

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
        #return str(options)
        #finish implementing by going through fn byte by byte per line
        if os.path.isfile(input): 
            with open(input) as f:
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
        else:
            #when we split the input(string) it will be a list, i,e .split('\n') -> 'abc' -> ['abc', '']
            #this caused issues with particualar bytes, so we will just take the string at that section
            input = input.split('\n')

            overlapStart = False
            for option in options:
                index = option.find('-')
                if index != -1:
                    if option[0] == '-':
                        for elem in input[:int(option[1:])]:
                            out.append(elem + '\n')
                    elif option[-1] == '-' and not overlapStart:
                        overlapStart = True
                        for elem in input[int(option[:-1]) - 1:]:
                            out.append(elem)
                    elif option[-1] != '-':#option is specifcying a range
                        out.append(input[int(option[:index]) - 1:int(option[index + 1:])] + '\n')
                else:#just wants those specific bytes
                    #bytes vs string indexing
                    #if we pass 1 with a string we want the first index, i,e cut -b 1 'abc' -> 'a'
                    #so index by 0 
                    input = input[0]
                    ind = int(option) - 1
                    out.append(input[ind] + '\n')
            #out.append(toAdd)
            return "".join(out)



       
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
        
        #use files flag again to check if we have a file or a string
        #strings will actually be one input as well so myabe not for
        #loop??

        # files=True
        # for element in input:
        #     if not os.path.isfile(element):
        #         files = False

        if os.path.isfile(input):
            with open(input, "r") as f:
                for line in f:
                    res.append(line)
            res.sort()
            if reverse:
                res.reverse()
            for elem in res:
                out.append(elem)
            return "".join(out)
        else:
            # we would have an array [result1\n, results2\n] etc 
            #so split by new line
            lines = input.split('\n')
            for line in lines:
                res.append(line)#put new line back

            res.sort()
            if reverse:
                res.reverse()
                
            for elem in res:
                out.append(elem+'\n')#put new line back for each
            return "".join(out)

# class Sort(Application):
#     def exec(self, args):
#         res = ''
#         out = deque()
#         if len(args) > 2:
#             raise ValueError("wrong number of command line arguments")
#         reverse = (args[0] == "-r")
#         if reverse and len(args) == 2:
#             file = args[1]
#         elif not reverse and len(args) == 1:
#             file = args[0]
#         else:
#             raise ValueError("wrong number of command line arguements")
#         res = []
#         with open(file, "r") as f:
#             for line in f:
#                 res.append(line)
#         res.sort()
#         if reverse:
#             res.reverse()
#         for elem in res:
#             out.append(elem)
#         return "".join(out)



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