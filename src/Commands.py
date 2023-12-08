from collections import deque
from applications import ApplicationFactory

class Command:
    def execute(self, args, output):
        raise NotImplementedError("for subclasses ( not called here)")

class SeqCommand(Command):
    def execute(self, args, output,store=False):
        app_factory = ApplicationFactory()
        #in case of pipeSeq
        if store:
            intermediate_output = []
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
                    if store:
                        intermediate_output.append(app_instance.exec(app_args))
                        return intermediate_output
                    else:
                        output.append(app_instance.exec(app_args))
            else:
                if store:
                        intermediate_output.append(app_instance.exec(app_args))
                        return intermediate_output
                else:
                    output.append(app_instance.exec(app_args))


class PipeCommand(Command):
    def execute(self, args, output, store=False):
        app_factory = ApplicationFactory()
        intermediate_output = []

        for i, command in enumerate(args):
            # app_name = command[0]
            # app_instance = app_factory.create_application(app_name)
            # if command[0]=='seq':
            #     SeqCommand().execute(command[1:], output)

            app_name = command[0]
            redirections = command[-1] if isinstance(command[-1], dict) else None

            if redirections:
                app_args = command[1:-1]
            else:
                app_args = command[1:]

            if intermediate_output:
                app_args.extend(intermediate_output)

            app_instance = app_factory.create_application(app_name)

            if i == len(args) - 1:
                # with open(command[-1]['out'], 'w') as file:
                #     file.write(app_instance.exec([intermediate_output]))
                #['-b', '-1,2-', 'abc\n']
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
                        intermediate_output=[(app_instance.exec(app_args))]
                else:
                    intermediate_output=[(app_instance.exec(app_args))]

        



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