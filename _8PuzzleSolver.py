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
outputfilename='output.txt'
inputfilename='input.txt'

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
    inputfilename = input("Leave blank to use default input file 'input.txt', type 'file:<filename>' to use a file, or type 'none' enter a string to examine:")

#validate User Queries
if inputfilename=="":
    try: inputfile = open(inputfilename,"rt")
    except IOError as e:
        sys.exit("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        sys.exit("Unexpected error:", sys.exc_info()[0])
elif inputfilename[0:5] == "file:":
    inputfilename = UserInput.split(":")[1]
    try: inputfile = open(inputfilename,"rt")
    except IOError as e:
        sys.exit("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        sys.exit("Unexpected error:", sys.exc_info()[0])
elif inputfilename=="none":
    UserInput=""
    inputfilename=""
else:
    if len(UserInput.split(":")) != 2:
        print(UserInput+" is not an understood method for examining a string.")
        print("Please enter a string in the format method:string where the only supported methods are best-first and A*.")
        print("The strings are of the format #,#,#,#,#,#,#,# where # is some combination of 1-8 and b where each is only used once.  For instance '4,5,b,6,1,8,7,3'.")
    else:
        if UserInput.split(":")[0] != "best-first" and UserInput.split(":")[0] != "A*":
            print(UserInput.split(":")[0]+" is not an understood method for examining a string.")
            print("Please enter a string in the format method:string where the only supported methods are best-first and A*.")
        if ValidateString(UserInput.split(":")[1]):
            print(UserInput.split(":",2)+" is not a correct string to examine")
            print("The strings are of the format #,#,#,#,#,#,#,# where # is some combination of 1-8 and b where each is only used once.  For instance '4,5,b,6,1,8,7,3'.")

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

    SearchType = UserInput.split(":")[0]
    if SearchType != "best-first" and SearchType != "A*":
         sys.exit("Please enter a string in the format method:string where the only supported methods are best-first and A*.")

    Puzzle = UserInput.split(":")[1].split(",")
    if len(Puzzle) != 9 and len(Puzzle) != 16:
        sys.exit("Please enter a puzzle of size 9 or 16 (e.g. b,1,2,3,4,5,6,7,8)")
    elif len(Puzzle) == 9:
        checkCharList = ['b',1,2,3,4,5,6,7,8]
        Puzz8.Puzzle8(SearchType,Puzzle).Solve()
    elif len(Puzzle) == 16:
        checkCharList = ['b',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    else:
        sys.exit("Puzzle Size check failed?! How?!")

    fail = 0
    for checkChar in checkCharList:
        if checkChar not in checkCharList:
            print("Puzzle is missing charcater "+str(checkChar))
            fail = 1
    if fail:
        sys.exit()

#quit


