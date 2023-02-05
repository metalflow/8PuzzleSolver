#imports
import sys

class Puzzle:
    #initialize variables
    data = [[0,0,0],[0,0,0],[0,0,0]]
    bCoords = [-1,-1]
    performanceScore = 0
    inversionCount=0

    def ProcessList(self,listIn):
        if len(listIn)!=3:
            raise Exception("Invalid list provided: has "+str(len(listIn))+" rows when only 3 are allowed") 
        xCoord=0
        for x in listIn:
            if len(x)!=3:
                raise Exception("Invalid list provided: row "+str(xCoord)+" has "+str(len(x))+" columns when only 3 are allowed") 
            yCoord=0
            for y in x:
                self.data[xCoord][yCoord]=y
                if y=='b':
                    self.bCoords=[xCoord,yCoord]
                yCoord +=1
            xCoord +=1
        return

    def ProcessString(self,stringIn):
        xCount=0
        for x in stringIn.split(','):
            if x=='b':
                self.bCoords=[xCount//3,xCount%3]
                self.data[xCount//3][xCount%3]=x
            else:
                self.data[xCount//3][xCount%3]=int(x)
            xCount +=1
            
        return

    #constructor
    def __init__(self,puzzleIn : 'Puzzle'):
        self.data = puzzleIn.data.copy()
        self.bCoords = puzzleIn.bCoords.copy()
        self.performanceScore = puzzleIn.performanceScore

    def __init__(self,inVar):
        if type(inVar) == str:
            self.ProcessString(inVar)
        elif type(inVar) == list:
            self.ProcessList(inVar)
        else:
            raise Exception("invalid parameter type of "+str(type(inVar))+"passed.  Please only pass strings or lists")
        self.ValidatePuzzle()
        if self.inversionCount%2 != 0:
            raise Exception("this is not a solvable puzzle because it has an odd number of inversions:"+str(self.inversionCount))
        #self.MeasurePerformance()

    def Swap(self,x,y):
        if x != self.bCoords[0] + 1 or x != self.bCoords[0] - 1:
            return False
        if y != self.bCoords[1] + 1 or y != self.bCoords[1] - 1:
            return False
        charToSwap = self.data[x][y]
        self.data[self.bCoords[0]][self.bCoords[1]] = charToSwap
        self.data[x][y] = 'b'
        self.bCoords[0]=x
        self.bCoords[1]=y
        return True

    def FindBCoords(self):
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                if self.data[x][y] == 'b':
                    self.bCoords=[x,y]
                    return [x,y]
        sys.exit("no b was found in this puzzle! "+str(self.data))

    def ValidatePuzzle(self):
        lastValue=0
        listToCheck=[]
        for x in self.data:
            for y in x:
                listToCheck.append(y)
        #validate content
        if self.bCoords.count(-1) != 0:
            raise Exception("Invalid list provided: does not contain a 'b' character")
        if listToCheck.count(1) != 1:
            raise Exception("Invalid list provided: contains "+str(listToCheck.count(1))+" '1' characters when it should only have 1")
        if listToCheck.count(2) != 1:
                raise Exception("Invalid list provided: contains "+str(listToCheck.count(2))+" '2' characters when it should only have 1")
        if listToCheck.count(3) != 1:
                raise Exception("Invalid list provided: contains "+str(listToCheck.count(3))+" '3' characters when it should only have 1")
        if listToCheck.count(4) != 1:
                raise Exception("Invalid list provided: contains "+str(listToCheck.count(4))+" '4' characters when it should only have 1")
        if listToCheck.count(5) != 1:
                raise Exception("Invalid list provided: contains "+str(listToCheck.count(5))+" '5' characters when it should only have 1")
        if listToCheck.count(6) != 1:
                raise Exception("Invalid list provided: contains "+str(listToCheck.count(6))+" '6' characters when it should only have 1")
        if listToCheck.count(7) != 1:
                raise Exception("Invalid list provided: contains "+str(listToCheck.count(7))+" '7' characters when it should only have 1")
        if listToCheck.count(8) != 1:
                raise Exception("Invalid list provided: contains "+str(listToCheck.count(8))+" '8' characters when it should only have 1")
        for x in listToCheck:
            if x != 'b':
                if x < lastValue:
                    self.inversionCount+=1
                    #also check to see if there are any previous inversions
                    for y in listToCheck[0:listToCheck.index(x)-1]:
                        if y != 'b' and x < y:
                            self.inversionCount+=1
                lastValue = x 

class Puzzle8():

    

    SearchType = ""
    ListOfStates = []
    SolveState=Puzzle([[1,2,3],[4,5,6],[7,8,'b']])
    initialPuzzle=Puzzle([[1,2,3],[4,5,6],[7,8,'b']])

    def __init__(self,search,puzzleIn):
        self.SearchType = search
        self.Puzzle = puzzleIn

    def __init__(self,search,puzzleString):
        self.SearchType = search
        self.initialPuzzle=Puzzle(puzzleString)

    def Solve(self):
        #check to see if the initial configuration is the solved configuration
        #self.ListOfStates.clear()
        self.ListOfStates[1]=self.Puzzle
        print("initial list of states:")
        for existingState in self.ListOfStates:
            print(str(existingState))
        if str(self.ListOfStates[-1]) == str(self.SolveState):
            return True
        else:
            #print(self.ListOfStates[-1])
            bCoords = self.FindBCoords(self.ListOfStates[-1])
            print("BCoords are:"+str(bCoords))
        #check to see if you can move the blank down
        if bCoords[0]+1<3:
            if self.subSolve(self.Swap(self.ListOfStates[-1],bCoords[0]+1,bCoords[1])):
                return True
        #check to see if you can move the blank up
        if bCoords[0]-1>=0:
            if self.subSolve(self.Swap(self.ListOfStates[-1],bCoords[0]-1,bCoords[1])):
                return True
        #check to see if you can move the blank left
        if bCoords[1]+1<3:
            if self.subSolve(self.Swap(self.ListOfStates[-1],bCoords[0],bCoords[1]+1)):
                return True
        #check to see if you can move the blank right
        if bCoords[1]-1>=0:
            if self.subSolve(self.Swap(self.ListOfStates[-1],bCoords[0],bCoords[1]-1)):
                return True
        #no solution was found
        self.ListOfStates.clear()
        return False

    def subSolve(self,puzzleIn):
        #check to see if the initial configuration is the solved configuration
        self.ListOfStates.append(puzzleIn)
        print("current list of states:")
        for existingState in self.ListOfStates:
            print(str(existingState))
        if str(self.ListOfStates[-1]) == str(self.SolveState):
            print("solved with current state:"+str(self.ListOfStates[-1]))
            print("and solveState:"+str(self.SolveState))
            return True
        else:
            bCoords = self.FindBCoords(self.ListOfStates[-1])
            print("BCoords are:"+str(bCoords))
        #check to see if you can move the blank down
        if bCoords[0]+1<3:
            puzzleOut=self.Swap(self.ListOfStates[-1],bCoords[0]+1,bCoords[1])
            quitflag=0
            for existingState in self.ListOfStates:
                print(str(existingState) + " compares to " + str(puzzleOut))
                if str(existingState)==str(puzzleOut):
                    quitFlag=1
                    break
            if quitFlag==0:
                print("selected to move down")
                return self.subSolve(puzzleOut)
            else:
                print("rejected to move down because state "+str(puzzleOut)+" already exists")
        else:
            print("rejected to move down")
        #check to see if you can move the blank up
        if bCoords[0]-1>=0:
            puzzleOut=self.Swap(self.ListOfStates[-1],bCoords[0]-1,bCoords[1])
            if self.ListOfStates.count(puzzleOut)==0:
                print("selected to move up")
                return self.subSolve(puzzleOut)
            else:
                print("rejected to move up because state "+str(puzzleOut)+" already exists")
        else:
            print("rejected to move up")
        #check to see if you can move the blank right
        if bCoords[1]+1<3:
            puzzleOut=self.Swap(self.ListOfStates[-1],bCoords[0],bCoords[1]+1)
            if self.ListOfStates.count(puzzleOut)==0:
                print("selected to move right")
                return self.subSolve(puzzleOut)
            else:
                print("rejected to move right because state "+str(puzzleOut)+" already exists")
        else:
            print("rejected to move right")
        #check to see if you can move the blank left
        if bCoords[1]-1>=0:
            puzzleOut=self.Swap(self.ListOfStates[-1],bCoords[0],bCoords[1]-1)
            if self.ListOfStates.count(puzzleOut)==0:
                print("selected to move left")
                return self.subSolve(puzzleOut)
            else:
                print("rejected to move left because state "+str(puzzleOut)+" already exists")
        else:
            print("rejected to move left")
        #no solution was found
        self.ListOfStates.pop()
        return False

    
