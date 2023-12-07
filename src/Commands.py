from collections import deque
from applications import ApplicationFactory

class Command:
    def execute(self, args, output):
        raise NotImplementedError("for subclasses ( not called here)")

class SeqCommand(Command):
    def execute(self, args, output):
        app_factory = ApplicationFactory()
        for command in args:
            app_name = command[0]
            app_args = command[1:]
            redirections = command[-1] if isinstance(command[-1], dict) else {}
            app_instance = app_factory.create_application(app_name)

            if 'out' in redirections:
                with open(redirections['out'], 'w') as file:
                    file.write(app_instance.exec(app_args))
            elif 'in' in redirections:
                with open(redirections['in'], 'r') as file:
                    output.append(app_instance.exec([file.read()] + app_args))
            else:
                output.append(app_instance.exec(app_args))

class PipeCommand(Command):
    def execute(self, args, output):
        app_factory = ApplicationFactory()
        intermediate_output = deque()

        for i, command in enumerate(args):
            app_name = command[0]
            app_args = command[1:]
            redirections = command[-1] if isinstance(command[-1], dict) else {}
            app_instance = app_factory.create_application(app_name)

            if i == 0 and 'in' in redirections:
                with open(redirections['in'], 'r') as file:
                    intermediate_output.append(app_instance.exec([file.read()] + app_args))
            elif i == len(args) - 1 and 'out' in redirections:
                final_output = ''.join(intermediate_output)
                with open(redirections['out'], 'w') as file:
                    file.write(app_instance.exec([final_output] + app_args))
            else:
                intermediate_output.append(app_instance.exec(app_args))

            if i < len(args) - 1: 
                intermediate_output = deque(intermediate_output)

            if i == len(args) - 1:
                output.extend(intermediate_output)



class CallCommand(Command):
    def execute(self, args, output):
        if args:
            app_factory = ApplicationFactory()
            app_name = args[0]
            app_args = args[1:]
            redirections = args[-1] if isinstance(args[-1], dict) else {}
            app_instance = app_factory.create_application(app_name)

            if 'out' in redirections:
                with open(redirections['out'], 'w') as file:
                    file.write(app_instance.exec(app_args))
            elif 'in' in redirections:
                with open(redirections['in'], 'r') as file:
                    output.append(app_instance.exec([file.read()] + app_args))
            else:
                output.append(app_instance.exec(app_args))
