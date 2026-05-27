import shutil
from shutil import copy2
import os

def movefileold(source, destination):
    shutil.move(source, destination,  copy_function=copy2)

