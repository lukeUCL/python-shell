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
                    output.append(app_instance.exec([file] + app_args))
            else:
                output.append(app_instance.exec(app_args))



class PipeCommand(Command):
    def execute(self, args, output):
        app_factory = ApplicationFactory()
        intermediate_output = None

        for i, command in enumerate(args):
            app_name = command[0]
            app_instance = app_factory.create_application(app_name)

            if i == 0 and 'in' in command[-1]:
                with open(command[-1]['in'], 'r') as file:
                    intermediate_output = app_instance.exec([file.read()])
            elif i == len(args) - 1 and 'out' in command[-1]:
                with open(command[-1]['out'], 'w') as file:
                    file.write(app_instance.exec([intermediate_output]))
            else:
                intermediate_output = app_instance.exec([intermediate_output])

            if i == len(args) - 1:
                output.append(intermediate_output)


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
                app_args.remove(redirections['in'])
                app_args = [redirections['in']] + app_args  # Pass filename directly
                output.append(app_instance.exec(app_args))
            else:
                output.append(app_instance.exec(app_args))
