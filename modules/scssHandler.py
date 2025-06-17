import subprocess
from libs.buffer import addToClipBoardFile
from modules.convertToRem import convertToRem
from modules.convertVariables import convertVariables
from modules.deleteLines import deleteLines
from modules.has_convert_to_rem import has_convert_to_rem
from modules.removeComment import removeComment
from modules.removeEmptyLines import removeEmptyLines
from modules.sortLines import sortLines


def scssHandler(file_path, variables_path):
    removeComment(file_path)
    try:
        convert_to_rem = has_convert_to_rem()
        print(f"convert_to_rem: {convert_to_rem}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return
    if convert_to_rem == '1':
        convertToRem(file_path)
    deleteLines(file_path)
    convertVariables(file_path, variables_path)
    sortLines(file_path)
    removeEmptyLines(file_path)
    with open(file_path, 'r') as file:
        addToClipBoardFile(file_path)
        file_content = file.read()
        subprocess.Popen(['notify-send', file_content])
