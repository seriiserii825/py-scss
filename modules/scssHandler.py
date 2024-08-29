from modules.convertToRem import convertToRem
from modules.deleteLines import deleteLines


def scssHandler(file_path):
    convertToRem(file_path)
    deleteLines(file_path)
