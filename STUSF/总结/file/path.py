import sys
import os

def inpath(file:str):
    sys.path.append(os.path.dirname(file))
