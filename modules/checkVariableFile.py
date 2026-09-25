import os

from py_libs.Print import Print


def checkVariableFile(variables_file):
    if not os.path.isfile(variables_file):
        Print.error("File variables not found")
        # create file
        os.system("touch " + variables_file)
    # if file is empty
    if os.stat(variables_file).st_size == 0:
        Print.error("File variables is empty")
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
