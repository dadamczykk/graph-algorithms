from os import listdir
from os.path import isfile
from dimacs import readSolution
import os

def runtest(function, directory, to_omit = []):
    
    has_uncorrect = False
    
    if directory[-1] != "\\":
        directory += "\\"

    graphs = [name for name in listdir(directory) if name not in to_omit]
    
    print("Testing files: ",  graphs)

    for graph in graphs:
        path = directory + graph
        if not isfile(path):
            continue
        ans = int(readSolution(path))
        print("\n============================\n")
        print("Filename: " + graph)
        myans = function(path)
        if ans != myans:
            has_uncorrect = True
        
        print("Correct solution: ", ans)
        print("My solution:      ", myans)
        print("Answer is " + "correct" if myans == ans else "uncorrect")
    
    print("\n" + "Everything is OK!" if not has_uncorrect else "There are problems!")
    return has_uncorrect
