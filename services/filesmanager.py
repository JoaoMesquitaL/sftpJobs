import shutil
import os

def movefileold(source, destination):
    shutil.copy2(source, destination,  follow_symlinks=True)

