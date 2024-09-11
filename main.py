import os
from termcolor import colored

import time
import pyperclip

from modules.checkVariableFile import checkVariableFile
from modules.scssHandler import scssHandler

# check if is file front-page.php
if not os.path.isfile('style.css'):
    exit(colored('File style.css not found', "red"))

current_script_directory = os.path.dirname(os.path.realpath(__file__))
projects_dir= os.path.join(current_script_directory, 'projects')
current_directory = os.getcwd()
current_directory_name = os.path.basename(current_directory)
variables_file = os.path.join(projects_dir, current_directory_name + '.txt')

checkVariableFile(variables_file)


temp_file = os.path.join(projects_dir, 'temp.txt')
os.system('echo "" > ' + temp_file)
time.sleep(1)

# Initialize the last clipboard content to an empty string
last_clipboard_content = ""

while True:
    current_clipboard_content = pyperclip.paste()
    if current_clipboard_content != last_clipboard_content:
      temp_file = os.path.join(projects_dir, 'temp.txt')
      with open(temp_file, 'w') as file:
        file.write(current_clipboard_content)
      last_clipboard_content = current_clipboard_content
      if ':' in current_clipboard_content:
        scssHandler(temp_file, variables_file)
    time.sleep(0.5)
