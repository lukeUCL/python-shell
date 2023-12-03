from collections import deque
from applications import apps

class Command:
    def execute(self, args, output):
        raise NotImplementedError("for subclasses ( not called here)")

class SeqCommand(Command):
    def execute(self, args, output):
        for command in args:
            app = command[0]
            app_args = command[1:]
            apps(app, app_args, output)

class PipeCommand(Command):
    def execute(self, args, output):
        intermediate_output = deque()  
        for i, command in enumerate(args):
            app = command[0]
            app_args = command[1:]
            if i > 0: 
                # force by prepending intermediate to args--- mabe we jsut use a diff paramete
                app_args = list(intermediate_output) + app_args
                intermediate_output.clear()

            apps(app, app_args, intermediate_output)

            if i == len(args) - 1:
                output.extend(intermediate_output)

class CallCommand(Command):
    def execute(self, args, output):
        if args:
            app = args[0]
            app_args = args[1:]
            apps(app, app_args, output)
