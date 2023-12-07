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
            redirections = command[-1] if isinstance(command[-1], dict) else {}

            if 'out' in redirections:
                with open(redirections['out'], 'w') as file:
                    apps(app, app_args, file)
            elif 'in' in redirections:
                with open(redirections['in'], 'r') as file:
                    apps(app, file, output)
            else:
                apps(app, app_args, output)


class PipeCommand(Command):
    def execute(self, args, output):
        intermediate_output = deque()
        for i, command in enumerate(args):
            app = command[0]
            app_args = command[1:]
            redirections = command[-1] if isinstance(command[-1], dict) else {}

            if i == 0 and 'in' in redirections:
                with open(redirections['in'], 'r') as file:
                    apps(app, file, intermediate_output)
            elif i == len(args) - 1 and 'out' in redirections:
                with open(redirections['out'], 'w') as file:
                    apps(app, intermediate_output, file)
            else:
                apps(app, intermediate_output, intermediate_output)

            if i < len(args) - 1: # intermediate step
                intermediate_output = deque(intermediate_output) # prepare for next command

            if i == len(args) - 1: # last command
                output.extend(intermediate_output)



class CallCommand(Command):
    def execute(self, args, output):
        if args:
            app = args[0]
            app_args = args[1:]
            redirections = args[-1] if isinstance(args[-1], dict) else {}

            if 'out' in redirections:
                with open(redirections['out'], 'w') as file:
                    apps(app, app_args, file)
            elif 'in' in redirections:
                with open(redirections['in'], 'r') as file:
                    apps(app, file, output)
            else:
                apps(app, app_args, output)
