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
            redirections = args[-1] if isinstance(args[-1], dict) else None
            if redirections:
                app_args = args[1:-1]
            else:
                app_args = args[1:]
            app_instance = app_factory.create_application(app_name)
            if redirections:
                if not redirections['out']==None:
                    with open(redirections['out'], 'w') as file:
                        file.write(app_instance.exec(app_args))
                elif not redirections['in']==None:
                    app_args.append(redirections['in'])
                    output.append(app_instance.exec(app_args))
            else:
                output.append(app_instance.exec(app_args))