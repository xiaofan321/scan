# coding=utf-8
import os

def set2txt(argtxt,qresults):
    if '/' in argtxt  or '\\' in argtxt:
        path = os.path.dirname(argtxt)
        if not os.path.exists(path):
            os.makedirs(path)
    with open(argtxt,'w') as f:
        while not qresults.empty():
            result = qresults.get()
            f.write(result['info'])
            f.write('\n')