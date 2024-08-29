from modules.convertToRem import convertToRem
from modules.convertVariables import convertVariables
from modules.deleteLines import deleteLines


def scssHandler(file_path, variables_path):
    convertToRem(file_path)
    deleteLines(file_path)
    convertVariables(file_path, variables_path)
