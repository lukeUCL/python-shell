import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob

def pwd(out):
    out.append(os.getcwd())
    out.append('hello world')

def cd(args):
    if len(args) == 0 or len(args) > 1:
        raise ValueError("wrong number of command line arguments")
    os.chdir(args[0])

def echo(out, args):
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

def cat(out, args):
    for a in args:
        with open(a) as f:
            out.append(f.read())

def head(out, args):
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
    with open(file) as f:
        lines = f.readlines()
        for i in range(0, min(len(lines), num_lines)):
            out.append(lines[i])

def tail(out, args):
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
def find(out, args):
    options = ["-exec", "-ok", "-inium", "-links", "-name", "-newer", "-perm",
                "-print", "empty", "-size", "-user", "\(expr\)", "/;"]
    commands = []
    if len(args) < 2 or args[i][:2] != "./":
        raise ValueError("wrong number of command line arguments")
    for i in range(1, len(args), 2):
        if args[i] not in options:
            raise ValueError("syntax error")
        else:
            try:
                commands.append([args[i], args[i+1]])
            except:
                raise ValueError("syntax error")
    #implement the functionality
    directory = args[0][2:]



    

def cut(out, args):
    pass

def uniq(out, args):
    pass

def sort(out, args):
    pass

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