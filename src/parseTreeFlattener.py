
from antlr4 import tree
from PARSER.ShellParser import ShellParser
from PARSER.ShellParserVisitor import ShellParserVisitor
import re


class parseTreeFlattener(ShellParserVisitor):

    # handling subsitution
    def processArg(self, text):
        from shell import run
        result = ""
        # Check for backquoted to be subbed
        pattern = r'`([^`]*)`'
        while '`' in text:
            match = re.search(pattern, text)
            if match:
                # store text before backquotes
                pre_text = text[:match.start()]
                # extract the command
                command_substitution = match.group(1)
                # echo is a unique edge case,
                # if we have echo echo we can just skip 5 indexes
                if command_substitution.startswith("echo echo"):
                    return command_substitution[5:]

                # store text after backquotes
                post_text = text[match.end():]
                # nested shell call, just process
                # the command with run from shell
                # use this output as sub
                substitution_output_deque = run(command_substitution)

                # we will never need any \n in substitution output,
                # replace with spaces
                substitution_output_str = ''.join(
                    substitution_output_deque
                    ).replace('\n', ' ').strip()

                result += pre_text + substitution_output_str
                text = post_text
            else:
                break

        return result + text

    def visitSeqPipeCommand(self, ctx: ShellParser.SeqPipeCommandContext):
        commands = []
        current_type = None
        current_group = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, tree.Tree.TerminalNodeImpl):
                if child.symbol.type == ShellParser.SEMI\
                 or child.symbol.type == ShellParser.PIPE:
                    if current_group:
                        if current_type:
                            commands.append([current_type] + current_group)
                        else:
                            commands.extend(current_group)
                        current_group = []

                    current_type = 'seq' if child.symbol.type\
                        == ShellParser.SEMI else 'pipe'
            else:
                command = self.visit(child)
                if command:
                    current_group.append(command)

        if current_group:
            if current_type:
                commands.append([current_type] + current_group)
            else:
                commands.extend(current_group)

        return commands

    def visitPipeCommand(self, ctx: ShellParser.PipeCommandContext):
        pipe_sequence = ['pipe']
        for i in range(0, ctx.getChildCount(), 2):
            command = self.visit(ctx.getChild(i))
            # ensure we only have one pipe flag, i.e ['pipe'[command, args]]
            if command:
                if command[0] != 'pipe':
                    pipe_sequence.append(command)
                else:
                    pipe_sequence.extend(command[1:])
        return pipe_sequence

    # same approach as pipe above
    def visitSeqCommand(self, ctx: ShellParser.SeqCommandContext):
        sequence = ['seq']
        for i in range(ctx.getChildCount()):
            command = self.visit(ctx.getChild(i))
            if command:
                if command[0] != 'seq':
                    sequence.append(command)
                else:
                    sequence.extend(command[1:])
        return sequence

    def visitCallCommand(self, ctx):
        command = None
        arguments = []
        redirection = {'in': None, 'out': None}
        skip_next = False  # flag to skip for redirection case

        for i in range(ctx.getChildCount()):

            child = ctx.getChild(i)
            text = child.getText()

            # if we have seen a redirection symbol, we skip the next child,
            # as we will have processed redirection, and arg
            if skip_next:
                skip_next = False
                continue

            if isinstance(child, ShellParser.RedirectionContext)\
                    or text in ['<', '>']:
                if i + 1 < ctx.getChildCount():
                    redirection_target_node = ctx.getChild(i+1)
                    redirection_target_text = redirection_target_node.getText()
                    if text == '<':
                        redirection['in'] = redirection_target_text
                    elif text == '>':
                        redirection['out'] = redirection_target_text
                    # skip next child since it's part of redirection
                    skip_next = True
                else:
                    # redirection with no target
                    raise ValueError(f"Redirection symbol\
                                    '{text}' at the end of\
                                     command without a target")

            elif command is None:
                # check for subsitituion i.e `echo a`
                command = self.processArg(text)
            else:
                if text not in ['<', '>']:
                    argument = self.visit(child)
                    arguments.append(argument)

        if command is None:
            raise ValueError("Command not found in callCommand context")

        full_command = [command] + arguments

        if redirection['in'] or redirection['out']:
            full_command.append(redirection)

        return full_command

    # Args are either quoted (double or single),
    # backquoted, or a mix, where we address splitting
    def visitArgument(self, ctx: ShellParser.ArgumentContext):

        if ctx.quoted():
            return self.visit(ctx.quoted())

        if ctx.backQuoted():
            return self.visit(ctx.backQuoted())

        arg_text = ctx.getText()

        # substitution
        text = self.processArg(arg_text)

        # splitting
        if '"' in text:
            return text.replace('"', '')
        if "'" in text:
            return text.replace("'", '')

        return text

    # just visit child- single or double quoted
    def visitQuoted(self, ctx: ShellParser.QuotedContext):
        return self.visit(ctx.getChild(0))

    # just return inner content unless we have substitution
    def visitSingleQuoted(self, ctx: ShellParser.SingleQuotedContext):
        text = ctx.getText()[1: -1]
        return self.processArg(text)

    # same as above
    def visitDoubleQuoted(self, ctx: ShellParser.DoubleQuotedContext):
        text = ctx.getText()[1: -1]
        return self.processArg(text)

    # substitution
    def visitBackQuoted(self, ctx: ShellParser.BackQuotedContext):
        backQuotedText = ctx.getText()
        return self.processArg(backQuotedText)

# del ShellParser- cant access
