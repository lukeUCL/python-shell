import os
import re
from abc import ABC, abstractmethod
from collections import deque
import glob
import difflib
from pathlib import Path


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
            if not os.path.exists(ls_dir):
                raise FileNotFoundError(f"No such file or directory: '{ls_dir}'")
            if not os.path.isdir(ls_dir):
                raise NotADirectoryError(f"Not a directory: '{ls_dir}'")
        else:
            raise ValueError("wrong number of command line arguments")

        files = [f for f in os.listdir(ls_dir) if not f.startswith(".")]
        return "\n".join(files) + "\n"

class Cat(Application):
    def exec(self, args):
        result = ""
        error_messages = []
        for a in args:
            try:
                with open(a) as f:
                    file_content = f.read()
                    if not file_content.strip():  # Check if the file content is empty
                        error_messages.append(f"Error: Empty file '{a}' detected")
                    else:
                        result += file_content
            except FileNotFoundError:
                error_messages.append(f"Error: File '{a}' not found")
            except Exception as e:
                error_messages.append(f"Error reading file '{a}': {str(e)}")
        if error_messages:
            return '\n'.join(error_messages)
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
                    # check line by line
                    lines = f.readlines()
                    # only need fileName when we have multiple files
                    result += grep(lines, file=(len(input) > 1), filename=file)

        # strings, just directly process
        else:
            result = grep(input)

        return result


class Find(Application):
    def exec(self, args):

        out = deque()
        # no prefix directory
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

        # recursive checking (see func below)
        self.search(path, pattern, out)
        if cwdRoot:
            res = deque()
            while len(out) > 0:
                res.appendleft('.' + out.pop()[len(os.getcwd()):])

            out.extend(res)

        path_list = [item for item in out if item != '.']
        return '\n'.join(path_list)

    def search(self, path, pattern, out):
        if not os.path.isdir(path):
            raise ValueError("path is not a directory")

        # check for globbing
        if "*" in pattern or "?" in pattern:
            glob_check = str(os.path.join(path, pattern))
            # glob path/pattern, join by \n
            matches = glob.glob(glob_check)
            mlist = '\n'.join(matches).strip('\n')
            out.extend(mlist.split('\n'))

        # check every directory recursively
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                self.search(os.path.join(path, file), pattern, out)
            else:
                # base case, we found a match
                if file == pattern or file.endswith(pattern[1:-1]):
                    out.append(os.path.join(path, file))


class Uniq(Application):
    def exec(self, args):
        out = deque()
        if len(args) > 2 or len(args) < 1:
            raise ValueError("wrong number of command line arguments")
        if args[0] == '-i':
            ignoreCase = True
        else:
            ignoreCase = False
        input_source = args[-1]

        def process_line(line, last_line):
            normalized_line = line.lower() if ignoreCase else line
            if normalized_line != last_line:
                # split by \n in pipe strings
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


# string handling vs file handling - for file,
# byte 1 is first element, for strings,
# byte 0 is first element
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

            # for strings passed by pipe, we want to consider each
            # string as a single element, so we'll nest them
            else:
                input = [[segment] for segment in input.split('\n')]
                # remove empty string
                input = input[:-1]

            for line in input:
                overlapStart = False
                for option in options:
                    index = option.find('-')
                    if index != -1:
                        if option[0] == '-':
                            for elem in line[:int(option[1:])-1]:
                                out.append(elem)
                            out.append(line[int(option[1:])-1] + '\n')
                        elif option[-1] == '-' and not overlapStart:
                            overlapStart = True
                            for elem in line[int(option[:-1]) - 1:]:
                                out.append(elem)
                        # option is specifying a range
                        elif option[-1] != '-':
                            start_index = int(option[:index]) - 1
                            end_index = int(option[index + 1:])
                            line_slice = line[start_index:end_index] + '\n'
                            out.append(line_slice)
                    # just wants those specific bytes
                    else:
                        if not File:
                            # extract string from square brackets
                            line = line[0]
                        # adjust bytes to string index
                        option = str(int(option) - 1)
                        out.append(line[int(option)] + '\n')
            return "".join(out)

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

        # add lines, sort, reverse(?), append to out
        # add \n if we need
        def sortInput(input):
            for line in input:
                res.append(line if line.endswith('\n') else line + '\n')
            res.sort()
            if reverse:
                res.reverse()
            for elem in res:
                # newline for strings which were split by
                # newline earlier
                out.append(elem) if elem.endswith('\n') else out.append(elem+'\n')
            return "".join(out)

        if os.path.isfile(input):
            input = open(input, "r")
        else:
            input = [line for line in input.split('\n') if line.strip()]
        return sortInput(input)


class Wc(Application):

    def exec(self, args):
        if len(args) != 2:
            raise ValueError(
                "wc expects exactly one argument for file or string input"
            )

        option, input_source = args
        # lines, words, chars opts
        if option not in ['-l', '-w', '-c']:
            raise ValueError(
                "wc expects an option -l (lines),\
                    -w (words), or -c (characters)"
            )

        content = self.getContent(input_source)

        if option == '-l':
            return str(self.countLines(content))
        elif option == '-w':
            return str(self.countWords(content))
        elif option == '-c':
            return str(self.countChars(content))

    def getContent(self, source):
        if os.path.isfile(source):
            with open(source, 'r') as file:
                return file.read()  # read as single string
        else:
            return source

    def countLines(self, content):
        return content.count('\n') if\
            content.count('\n') > 0 else 1

    def countWords(self, content):
        return len(content.split())

    def countChars(self, content):
        return len(content)


class Diff:
    def exec(self, args):
        # args checking
        if len(args) != 2:
            raise ValueError("Two arguments are required for diff.")

        content1, fromfile = self.getContent(args[0])
        content2, tofile = self.getContent(args[1])

        diff = self.computeDiff(content1, content2, fromfile, tofile)
        return self.join(diff)

    def getContent(self, source):
        if os.path.isfile(source):
            with open(source, 'r') as file:
                return file.readlines(), source
        else:
            # account for piped strings passed with \n
            lines = source.split('\n')
            lines = [line + '\n' for line in lines if line]
            return lines, "string_input"

    # also printing file names now
    def computeDiff(self, content1, content2, fromfile, tofile):

        diff = difflib.unified_diff(
            content1, content2, fromfile=fromfile, tofile=tofile, lineterm=''
        )
        return list(diff)

    def join(self, diff):
        # joining diff output into single string
        return '\n'.join(diff)


class Touch:
    def exec(self, args):
        # arg checking
        if len(args) < 1:
            raise ValueError("At least one argument is required for touch.")

        for file_path in args:
            self._touch_file(file_path)

        # dont throw command line error
        return ''

    def _touch_file(self, file_path):
        path = Path(file_path)
        path.touch(exist_ok=True)


class Mkdir(Application):
    def exec(self, args):
        if len(args) != 1:
            # no arg given
            raise ValueError("Wrong number of command line arguments")

        directory_name = args[0]
        os.makedirs(directory_name)
        # dont throw command line error
        return ""


class Rmdir(Application):
    def exec(self, args):
        if len(args) != 1:
            raise ValueError("wrong number of command line arguments")

        directory_name = args[0]
        os.rmdir(directory_name)
        return ""


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
            "mkdir": Mkdir,
            "rmdir": Rmdir
        }

        actual_name = app_name[1:] if app_name.startswith("_") else app_name
        if actual_name not in app_types:
            raise ValueError(f"Invalid application name: {app_name}")

        # call unsafe for _ prefix
        app_instance = app_types[actual_name]()
        return UnsafeWrapper(app_instance)\
            if app_name.startswith("_") else app_instance