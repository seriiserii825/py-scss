import subprocess
from libs.buffer import addToClipBoardFile
from modules.convertToRem import convertToRem
from modules.convertVariables import convertVariables
from modules.deleteLines import deleteLines
from modules.printTemp import printTemp
from modules.removeComment import removeComment
from modules.sortLines import sortLines


def scssHandler(file_path, variables_path):
    removeComment(file_path)
    # printTemp(file_path)
    convertToRem(file_path)
    deleteLines(file_path)
    convertVariables(file_path, variables_path)
    sortLines(file_path)
    with open(file_path, 'r') as file:
        addToClipBoardFile(file_path)
        file_content = file.read()
        subprocess.Popen(['notify-send', file_content])

