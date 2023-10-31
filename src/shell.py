import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob


# Improved function to tokenize the command line
def tokenize(cmdline):
    # Split the command by semicolons, quotes, etc.
    raw_commands = re.findall(r"([^\"';]+|\"[^\"]*\"|'[^']+')", cmdline)
    #lets use raw string so we don't have to escape the backslash (would act as quotes)

    #first will find all the strings that are not semicolons, quotes, or apostrophes
    #second will find all the strings that are double quotes uses * because empty strings are valid
    #third will find all the strings that are single quotes uses * because empty strings are valid

    tokens = []
    for command in raw_commands:
        # Further tokenize each command
        matches = re.findall(r"[^\\s\"']+|\"([^\"]*)\"|'([^']*)'", command)
        for match in matches:
            if match[0] or match[1]:
                # If it's a quoted string, remove quotes and add
                tokens.append(match[0] or match[1])
            else:
                # Handle globbing only if necessary, e.g., not for echo
                globbed = glob(match[0])
                tokens.extend(globbed if globbed else [match[0]])
    return tokens

# Separate function for handling 'head' and 'tail' since they have a lot in common
def process_head_tail(app, args, out):
    if len(args) < 1:
        raise ValueError(f"wrong number of arguments for {app}")
    num_lines = 10  # Default number of lines
    file = args[-1]  # Last arg is the file
    if len(args) == 3:
        if args[0] != "-n":
            raise ValueError("wrong flags")
        num_lines = int(args[1])
    with open(file) as f:
        lines = f.readlines()
        # Handling the logic for 'head' and 'tail'
        display_lines = (lines[:num_lines] if app == "head" else lines[-num_lines:])
        out.extend(display_lines)

# Main evaluation function
def eval(tokens, out):
    if not tokens:
        return

    app = tokens[0]
    args = tokens[1:]

    if app == "exit" or app == "quit":
        exit(0)
    elif app == "pwd":
        out.append(os.getcwd())
    elif app == "cd":
        if len(args) != 1:
            raise ValueError("cd requires exactly one argument")
        os.chdir(args[0])
    elif app == "echo":
        out.append(" ".join(args) + "\n")
    # ... [other commands like ls, cat can remain largely the same]
    elif app == "head" or app == "tail":
        process_head_tail(app, args, out)
    elif app == "grep":
        # Using re.search instead of re.match
        pattern = re.compile(args[0])
        files = args[1:]
        for file in files:
            with open(file) as f:
                for line in f:
                    if pattern.search(line):
                        out.append(line)
    else:
        raise ValueError(f"unsupported application {app}")

if __name__ == "__main__":
    while True:
        print(f"{os.getcwd()}> ", end="")
        cmdline = input()
        tokens = tokenize(cmdline)
        out = deque()
        try:
            eval(tokens, out)
            while out:
                print(out.popleft(), end="")
        except Exception as e:
            print(f"Error: {e}")


def rawC(test):
    raw_commands = re.findall(r"([^\"';]+|\"[^\"]*\"|'[^']+')",test)
    print(raw_commands)




