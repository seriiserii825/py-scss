import os

from termcolor import colored


def checkVariableFile(variables_file):
    if not os.path.isfile(variables_file):
        print(colored("File variables not found", "red"))
        # create file
        os.system("touch " + variables_file)
    # if file is empty
    if os.stat(variables_file).st_size == 0:
        print(colored("File variables is empty", "red"))
        exit()
    else:
        # remove empty lines
        with open(variables_file, "r") as file:
            data = file.readlines()
        for i in range(len(data)):
            if data[i] == "\n":
                data[i] = ""
        with open(variables_file, "w") as file:
            file.writelines(data)
