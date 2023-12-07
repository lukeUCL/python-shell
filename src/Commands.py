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
            redirections = command[-1] if isinstance(command[-1], dict) else None
            if redirections:
                app_args = command[1:-1]
            else:
                app_args = command[1:]
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


class PipeCommand(Command):
    def execute(self, args, output):
        app_factory = ApplicationFactory()
        intermediate_output = []

        for i, command in enumerate(args):
            # app_name = command[0]
            # app_instance = app_factory.create_application(app_name)
            app_name = command[0]
            redirections = command[-1] if isinstance(command[-1], dict) else None

            if redirections:
                app_args = command[1:-1]
            else:
                app_args = command[1:]

            app_instance = app_factory.create_application(app_name)

            if i == len(args) - 1:
                # with open(command[-1]['out'], 'w') as file:
                #     file.write(app_instance.exec([intermediate_output]))
                #['-b', '-1,2-', 'abc\n']
                app_args.extend(intermediate_output)
                if redirections:
                    if not redirections['out']==None:
                        with open(redirections['out'], 'w') as file:
                            file.write(app_instance.exec(app_args))
                    elif not redirections['in']==None:
                        app_args.append(redirections['in'])
                        output.append(app_instance.exec(app_args))
                    else:
                        output.append(app_instance.exec(app_args))

            #should be piped to next
            else:
                if redirections:
                    if not redirections['out']==None:
                        with open(redirections['out'], 'w') as file:
                            file.write(app_instance.exec(app_args))
                    elif not redirections['in']==None:
                        app_args.append(redirections['in'])
                        intermediate_output.append(app_instance.exec(app_args))
                else:
                    intermediate_output.append(app_instance.exec(app_args))

        



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