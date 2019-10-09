
import ast
import sys, os

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
NORMAL = '\033[0m'

dir_path = os.path.dirname(os.path.realpath(__file__))
scripts = os.listdir(dir_path)

print(GREEN+"-"*13)

for file in scripts:
    if file[0] == ".":
        continue
    if file.endswith(".py"):
        comment = ""
        try:
            lines = [line.rstrip('\n') for line in open(os.path.join(dir_path, file))]
            for line in lines:
                if line.strip().startswith("#"):
                    comment = line.strip()[1:]
                    break
        except Exception:
            pass
        print(RED, '{0: <10}'.format(file[0:-3]), YELLOW, "\t", comment)


print(GREEN+"-"*13+NORMAL)