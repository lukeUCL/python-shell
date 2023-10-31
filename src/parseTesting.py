import re

def rawC(test):
    raw_commands = re.findall(r"([^\"';]+|\"[^\"]*\"|'[^']+')",test)
    print(raw_commands)

# Test the function
rawC('echo "Hello World"; ls -l \'My Folder\'')
