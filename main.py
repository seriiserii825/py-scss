import os
from termcolor import colored

from libs.buffer import getFromClipBoard

import time
import pyperclip

from modules.scssHandler import scssHandler

# check if is file front-page.php
if not os.path.isfile('front-page.php'):
    exit(colored('File front-page.php not found', "red"))

current_script_directory = os.path.dirname(os.path.realpath(__file__))
projects_dir= os.path.join(current_script_directory, 'projects')
current_directory = os.getcwd()
current_directory_name = os.path.basename(current_directory)
variables_file = os.path.join(projects_dir, current_directory_name + '.txt')

if not os.path.isfile(variables_file):
    print(colored('File variables not found', "red"))
    ## create file
    os.system('touch ' + variables_file)
# if file is empty
if os.stat(variables_file).st_size == 0:
    print(colored('File variables is empty', "red"))
    exit()

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
