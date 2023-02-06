#imports
import sys,Puzz8

#define functions
def ValidateString(StringToExamine):
    count = [0 for i in range(len(StringToExamine.split(",")))]
    #determine if the String is of the right size
    if StringToExamine.split(",").size != 9:
        return 1
    #determine if the string is composed of the right elements
    for item in StringToExamine.split(","):
        if item == "1":
            count[1] += 1
            if count[1]>1:
                return 1
        elif item == "2":
            count[2]+= 1
            if count[2]>1:
                return 1
        elif item == "3":
            count[3]+= 1
            if count[3]>1:
                return 1
        elif item == "4":
            count[4]+= 1
            if count[4]>1:
                return 1
        elif item == "5":
            count[5]+= 1
            if count[5]>1:
                return 1
        elif item == "6":
            count[6]+= 1
            if count[6]>1:
                return 1
        elif item == "7":
            count[7]+= 1
            if count[7]>1:
                return 1
        elif item == "8":
            count[8]+= 1
            if count[8]>1:
                return 1
        elif item == "b":
            count[0]+= 1
            if count[0]>1:
                return 1
        else:
            return 1
    return 0

#initialize variables
outputfilename="output.txt"
inputfilename="input.txt"

#import and handle comand line arguments
for arg in sys.argv:
    if arg[0:4] == "-i:'":
        inputfilename=arg[5:-2]
    elif arg[0:12] == "-inputfile:'":
        inputfilename=arg[13:-2]
    elif arg[0:4] == "-o:'":
        outputfilename=arg[5:-2]
    elif arg[0:13] == "-outputfile:'":
        outputfilename=arg[14:-2]
    elif arg[-16:] == "8PuzzleSolver.py":
        pass
    else:
        print(" command line arg "+arg+" is not understood.  Please use either -i:'filename',-inputfile:'filename',-o:'filename', or -outputfile:'filename'.")

#query user for missing data
if outputfilename=='output.txt':
    outputfilename = input("Leave blank to use default output file 'output.txt', type 'none' to not use an output file, or enter a filename to record this session's results:")
if inputfilename=='input.txt':
    inputfilename = input("Leave blank to use default input file 'input.txt', type 'file:<filename>' to use a file, or type 'none' to enter a string to examine:")

#validate User Queries
if inputfilename=="":
    try: inputfile = open("input.txt","rt")
    except IOError as e:
        sys.exit("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        sys.exit("Unexpected error:", sys.exc_info()[0])
    userInput=inputfile.readline()
elif inputfilename[0:5] == "file:":
    inputfilename = userInput.split(":")[1]
    try: inputfile = open(inputfilename,"rt")
    except IOError as e:
        sys.exit("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        sys.exit("Unexpected error:", sys.exc_info()[0])
    userInput=inputfile.readline()
elif inputfilename=="none":
    userInput = input("please enter a string in the for of 'SearchType:b,1,2,3,4,5,6,7,8':")
else:
    sys.exit("Invalid Input selection")

if outputfilename=="none":
    outputfilename=""
elif outputfilename=="":
    outputfilename="output.txt"
    try: outputfile = open(outputfilename,"wt")
    except IOError as e:
        sys.exit("I/O error({0}): {1}".format(e.errno, e.strerror))
    except:
        #handle other exceptions such as attribute errors
        sys.exit("Unexpected error:", sys.exc_info()[0])
else:
    try: outputfile = open(outputfilename,"wt")
    except IOError as e:
        sys.exit("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        sys.exit("Unexpected error:", sys.exc_info()[0])

#execute program

#condition UserInput into useful variables

while (userInput!=""):
    print(userInput)
    currentPuzzle=Puzz8.Puzzle8(userInput.split(":")[0],userInput.split(":")[1])
    if outputfilename!="":
        outputfile.write("current puzzle:"+str(currentPuzzle.ListOfStates[0].data)+" using searchtype "+str(currentPuzzle.SearchType)+"\n")
        if currentPuzzle.ListOfStates[0].inversionCount%2 !=0:
            outputfile.write("skipping this puzzle becasue it has an odd inversion score of:"+str(currentPuzzle.ListOfStates[0].inversionCount)+"\n")
        elif currentPuzzle.SearchType == "best-first":
            outputfile.write("manhatten distance hueristic:\n")
            currentPuzzle.perfType = "manhatten"
            if currentPuzzle.BestFirstSolve():
                outputfile.write("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                    outputfile.writelines(str(state.data)+"\n")
            else:
                outputfile.write("puzzle was not solvable!\n")
            outputfile.write("badTile hueristic:\n")
            del currentPuzzle
            currentPuzzle=Puzz8.Puzzle8(userInput.split(":")[0],userInput.split(":")[1])
            currentPuzzle.perfType = "badTile"
            if currentPuzzle.BestFirstSolve():
                outputfile.write("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                    outputfile.writelines(str(state.data)+"\n")
            else:
                outputfile.write("puzzle was not solvable!\n")
            outputfile.write("my hueristic:\n")
            del currentPuzzle
            currentPuzzle=Puzz8.Puzzle8(userInput.split(":")[0],userInput.split(":")[1])
            currentPuzzle.perfType = "myPerf"
            if currentPuzzle.BestFirstSolve():
                outputfile.write("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                    outputfile.writelines(str(state.data)+"\n")
            else:
                outputfile.write("puzzle was not solvable!\n")
        elif currentPuzzle.SearchType == "A*":
            currentPuzzle.perfType = "manhatten"
            if currentPuzzle.AStarSolve():
                outputfile.write("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                    outputfile.writelines(str(state.data)+"\n")
            else:
                outputfile.write("puzzle was not solvable!\n")
            outputfile.write("badTile hueristic:\n")
            del currentPuzzle
            currentPuzzle=Puzz8.Puzzle8(userInput.split(":")[0],userInput.split(":")[1])
            currentPuzzle.perfType = "badTile"
            if currentPuzzle.AStarSolve():
                outputfile.write("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                    outputfile.writelines(str(state.data)+"\n")
            else:
                outputfile.write("puzzle was not solvable!\n")
            outputfile.write("my hueristic:\n")
            del currentPuzzle
            currentPuzzle=Puzz8.Puzzle8(userInput.split(":")[0],userInput.split(":")[1])
            currentPuzzle.perfType = "myPerf"
            if currentPuzzle.AStarSolve():
                outputfile.write("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                    outputfile.writelines(str(state.data)+"\n")
            else:
                outputfile.write("puzzle was not solvable!\n")
        else:
            outputfile.write("skipping this puzzle becasue it has an invalid search type of:"+str(currentPuzzle.SearchType)+"\n")
    else:
        print("current puzzle:"+str(currentPuzzle.ListOfStates[0].data)+" using serachtype "+str(currentPuzzle.SearchType))
        if currentPuzzle.ListOfStates[0].inversionCount%2 !=0:
             print("skipping this puzzle becasue it has an odd inversion score of:"+str(currentPuzzle.ListOfStates[0].inversionCount)+"\n")
        elif currentPuzzle.SearchType == "best-first":
            if currentPuzzle.BestFirstSolve():
                print("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                    outputfile.writelines(str(state.data)+"\n")
            else:
                 print("puzzle was not solvable!\n")
        elif currentPuzzle.SearchType == "A*":
            if currentPuzzle.AStarSolve():
                print("puzzle was solvable in "+str(len(currentPuzzle.ListOfStates))+" steps:\n")
                for state in currentPuzzle.ListOfStates:
                     print(str(state.data)+"\n")
            else:
                 print("puzzle was not solvable!\n")
        else:
             print("skipping this puzzle becasue it has an invalid search type of:"+str(currentPuzzle.SearchType)+"\n")
    del currentPuzzle
    if inputfilename=="none":
        userInput = input("please enter a string in the for of 'SearchType:b,1,2,3,4,5,6,7,8':")
    else:
        userInput=inputfile.readline()

#quit


