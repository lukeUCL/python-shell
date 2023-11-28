import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob

def pipe(left, right):#can just remove the directory name from current output
    pass
    #apps(right[0], )

def pwd(out, pipe= False):#pipe represents if app is on left of pipe symbol
    if pipe:
        return os.getcwd()
    out.append(os.getcwd())


def cd(args):
    if len(args) == 0 or len(args) > 1:
        raise ValueError("wrong number of command line arguments")
    os.chdir(args[0])

def echo(out, args, pipe= False):
    if pipe:
        return " ".join(args) + "\n"
    
    out.append(" ".join(args) + "\n")

def ls(out, args):
    if len(args) == 0:
        ls_dir = os.getcwd()
    elif len(args) > 1:
        raise ValueError("wrong number of command line arguments")
    else:
        ls_dir = args[0]
    for f in listdir(ls_dir):
        if not f.startswith("."):
            out.append(f + "\n")

def cat(out, args, pipe= False):
    if pipe:
        outNew = deque()
        with open(a) as f:
            outNew.append(f.read())
        return outNew
    for a in args:
        with open(a) as f:
            out.append(f.read())

def head(out, args, pipe= False):
    if len(args) != 1 and len(args) != 3:
        raise ValueError("wrong number of command line arguments")
    if len(args) == 1:
        num_lines = 10
        file = args[0]
    if len(args) == 3:
        if args[0] != "-n":
            raise ValueError("wrong flags")
        else:
            num_lines = int(args[1])
            file = args[2]
    if pipe:
        outNew = deque()
        lines = f.readlines()
        with open(file) as f:
            lines = f.readlines()
            for i in range(0, min(len(lines), num_lines)):
                outNew.append(lines[i])
        return outNew

    with open(file) as f:
        lines = f.readlines()
        for i in range(0, min(len(lines), num_lines)):
            out.append(lines[i])

def tail(out, args, pipe= False):
    if len(args) != 1 and len(args) != 3:
        raise ValueError("wrong number of command line arguments")
    if len(args) == 1:
        num_lines = 10
        file = args[0]
    if len(args) == 3:
        if args[0] != "-n":
            raise ValueError("wrong flags")
        else:
            num_lines = int(args[1])
            file = args[2]
    if pipe:
        outNew = deque()
        with open(file) as f:
            lines = f.readlines()
            display_length = min(len(lines), num_lines)
            for i in range(0, display_length):
                outNew.append(lines[len(lines) - display_length + i])
        return outNew
    with open(file) as f:
        lines = f.readlines()
        display_length = min(len(lines), num_lines)
        for i in range(0, display_length):
            out.append(lines[len(lines) - display_length + i])

def grep(out, args):
    if len(args) < 2:
        raise ValueError("wrong number of command line arguments")
    pattern = args[0]
    files = args[1:]
    for file in files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if re.match(pattern, line):
                    if len(files) > 1:
                        out.append(f"{file}:{line}")
                    else:
                        out.append(line)
#to implement find, cut, uniq, sort.
def find(out, args):#prints the path to the file 
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


    

def uniq(out, args):
    if len(args) > 2 or len(args) < 1:
        raise ValueError("wrong number of command line arguements")
    caseSensitive = args[0] == '-i'
    if caseSensitive and len(args) == 2:
        file = args[1]
    elif not caseSensitive and len(args) == 1:
        file = args[0]
    ready = False
    temp = None
    line = None
    count = 0
    with open(file) as f:
        for l in f:
            if not caseSensitive:
                line = l.lower()
            else:
                line = l

            if not ready:
                temp = line
                ready = True
                continue
            else:
                if temp != line:
                    out.append(temp)
                    temp = line
                    count += 1
    if count == 0 and temp is not None:
        out.append(temp)
    if line not in out and line is not None:
        out.append(line)

                

            

def cut(out, args):
    if len(args) < 3:
        raise ValueError("wrong number of command line arguements")
    options, file = args[:-1], args[-1]
    if options[0] != '-b' or len(options) < 2:
        raise ValueError("incorrect input")
    options = options[1].split(separator=',')
    #finish implementing by going through fn byte by byte per line
    with open(file) as f:
        for line in f:
            toAdd = ''
            index = option.find('-')
            for option in options:
                if index != -1:
                    if option[0] == '-':
                        toAdd += line[:int(option[1:])]
                    elif option[-1] == '-':
                        toAdd += line[int(option[:-1]) - 1:]
                    else:#option is specifcying a range
                        toAdd += line[int(option[:index]) - 1:int(option[index + 1:])]
                else:#just wants those specific bytes
                    toAdd += line[int(option)]
        out.append(toAdd)
        
def sort(out, args):#to implement next
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
        res.reverse
    for elem in res:
        out.append(elem)



def apps(app, args, out):
    if app == "pwd":
        pwd(out)
    elif app == "cd":
        cd(args)
    elif app == "echo":
        echo(out, args)
    elif app == "ls":
        ls(out, args)
    elif app == "cat":
        cat(out, args)
    elif app == "head":
        head(out, args)
    elif app == "tail":
        tail(out, args)
    elif app == "grep":
        grep(out, args)
    elif app == "find":
        find(out, args)
    elif app == "cut":
        cut(out, args)
    elif app == "uniq":
        uniq(out, args)
    elif app == "sort":
        sort(out, args)
    else:
        raise ValueError(f"unsupported application {app}")