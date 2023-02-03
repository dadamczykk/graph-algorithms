from os import listdir
from os.path import isfile
from dimacs import readSolution
import time

def runtest(function, directory, to_omit = []):
    # to_omit parameter may be used to omit some long tests
    all_time = time.time()

    has_uncorrect = False

    if directory[-1] != "\\":
        directory += "\\"

    graphs = [name for name in listdir(directory) if name not in to_omit]

    print("Testing files: ",  graphs)

    for graph in graphs:
        
        test_time = time.time()
        path = directory + graph
        
        if not isfile(path):
            continue
        ans = int(readSolution(path))
        
        print("\n============================\n")
        print("Filename: " + graph)
        
        myans = function(path)

        print("Correct solution: ", ans)
        print("My solution:      ", myans)
        print("Answer is " + "correct" if myans == ans else "uncorrect")
        print(f"Time of test: {time.time() - test_time:.4f}s", )
        
        if ans != myans:
            has_uncorrect = True

    print("\n" + "Everything is OK!" if not has_uncorrect else "There are problems!")
    print(f"\nAll tests time: {time.time() - all_time:.4f}s")
    return None
