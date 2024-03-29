# Fall 2019
# HW 7
# Keep this file in the folder with the .pyc files
# Run this file, or type "from runme import *"
# You should then be able to run the code
# key.main()
# However, if you know your python version, for example 3.7,
# you can also play this game at the command line by typing
# python3 (filename).pyc
# etc

import os
import re

def findFileNames():
    L=[]
    cp=os.listdir(".")
    p=re.compile('hw[\w]*3[\d]')
    for i in range(len(cp)):
        names=p.findall(cp[i])
        if not(names in L) and len(names)>0:
            L.append(names)
    return L

L=findFileNames()
print("Trying: ", L)

for i in range(len(L)):
    try:
        exec("import "+L[i][0]+" as key")
        print(L[i][0], "worked")
    except:
        pass
