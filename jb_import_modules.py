import sys
import os

path = '\\Python\\packages' #path within main folder where modules are located.
                            #this folder has to contain empty __init__.py file

module_path = os.path.abspath(os.path.join('..')) + path

if module_path not in sys.path:
    sys.path.append(module_path)
