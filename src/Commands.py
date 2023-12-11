from applications import ApplicationFactory


class Command:
    def execute(self, args, output):
        raise NotImplementedError("for subclasses ( not called here)")


def evalCommand(flattened, output):
    if isinstance(flattened[0], list):
        intermediate = []
        for part in flattened:
            if part[0] == 'seq':
                intermediate.extend(
                    SeqCommand().execute(part[1:], output, store=True)
                )
            elif part[0] == 'pipe':
                part[1].extend(intermediate)
                SeqCommand().execute(part[1:], output)
    elif flattened[0] == 'pipe':
        PipeCommand().execute(flattened[1:], output)
    elif flattened[0] == 'seq':
        SeqCommand().execute(flattened[1:], output)
    else:
        CallCommand().execute(flattened, output)


def getArgs(command):
    app_name = command[0]
    redirections = command[-1] if isinstance(command[-1], dict) else None
    if redirections:
        app_args = command[1:-1]
    else:
        app_args = command[1:]
    return app_name, app_args, redirections


def handleRedirections(app_instance, app_args, redirections, output):

    if redirections:
        if redirections['out']:
            with open(redirections['out'], 'w') as file:
                file.write(app_instance.exec(app_args))
        elif redirections['in']:
            app_args.append(redirections['in'])
            output.append(app_instance.exec(app_args))

    return output, app_args


def processCommand(app_instance, app_args, output):
    output.append(app_instance.exec(app_args))
    return output


class SeqCommand(Command):
    def execute(self, args, output, store=False):
        # store flag for passing seqs to pipes
        app_factory = ApplicationFactory()
        intermediate_output = [] if store else output

        for command in args:
            app_name, app_args, redirections = getArgs(command)
            app_instance = app_factory.create_application(app_name)

            if redirections:
                intermediate_output, app_args =\
                    handleRedirections(
                        app_instance, app_args,
                        redirections, intermediate_output
                    )
            else:
                intermediate_output = processCommand(
                        app_instance, app_args, intermediate_output
                    )

        # explicit return stops from writing to out
        if store:
            return intermediate_output


class PipeCommand(Command):
    def execute(self, args, output):
        app_factory = ApplicationFactory()
        intermediate_output = []

        for i, command in enumerate(args):
            app_name, app_args, redirections = getArgs(command)
            app_instance = app_factory.create_application(app_name)

            # Extend args with intermediate
            # output for all but the first command
            if i > 0:
                app_args.extend(intermediate_output)
                intermediate_output = []

            # Handle redirections and execute command
            if redirections:
                intermediate_output, app_args = handleRedirections(
                    app_instance, app_args, redirections, intermediate_output
                    )
            else:
                intermediate_output = processCommand(
                    app_instance, app_args, intermediate_output
                )

            # For the last command in the pipe,
            # append the results to the main output
            if i == len(args) - 1:
                output.extend(intermediate_output)


class CallCommand(Command):
    def execute(self, args, output):
        if args:
            app_factory = ApplicationFactory()
            app_name, app_args, redirections = getArgs(args)
            app_instance = app_factory.create_application(app_name)

            if redirections:
                handleRedirections(
                    app_instance, app_args, redirections, output
                )
            else:
                processCommand(
                    app_instance, app_args, output
                )
        else:
            raise ValueError("No command given")
