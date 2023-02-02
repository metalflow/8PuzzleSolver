#imports

import sys

class __Puzzle():
    #initialize variables
    data = [[0,0,0],[0,0,0],[0,0,0]]
    bCoords = [-1,-1]
    performanceScore = 0

    #constructor
    def __init__(self,puzzleIn : __Puzzle):
        self.data = puzzleIn.data.copy()
        self.bCoords = puzzleIn.bCoords.copy()
        self.performanceScore = puzzleIn.performanceScore

    def __init__(self,listIn):
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
        #validate content
        if self.bCoords.count(-1) != 0:
             raise Exception("Invalid list provided: does not contain a 'b' character")
        if self.data.count(1) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(1))+" '1' characters when it should only have 1")
        if self.data.count(2) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(2))+" '2' characters when it should only have 1")
        if self.data.count(3) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(3))+" '3' characters when it should only have 1")
        if self.data.count(4) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(4))+" '4' characters when it should only have 1")
        if self.data.count(5) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(5))+" '5' characters when it should only have 1")
        if self.data.count(6) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(6))+" '6' characters when it should only have 1")
        if self.data.count(7) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(7))+" '7' characters when it should only have 1")
        if self.data.count(8) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(8))+" '8' characters when it should only have 1")

        self.MeasurePerformance()

    def __init__(self,stringIn):
        stringElements=stringIn.split(",")
        if len(stringElements)!=9:
            raise Exception("Invalid string provided, must be of length 9") 
        if stringElements.count(1) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(1))+" '1' characters when it should only have 1")
        if stringElements.count(2) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(2))+" '2' characters when it should only have 1")
        if stringElements.count(3) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(3))+" '3' characters when it should only have 1")
        if stringElements.count(4) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(4))+" '4' characters when it should only have 1")
        if stringElements.count(5) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(5))+" '5' characters when it should only have 1")
        if stringElements.count(6) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(6))+" '6' characters when it should only have 1")
        if stringElements.count(7) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(7))+" '7' characters when it should only have 1")
        if stringElements.count(8) != 1:
             raise Exception("Invalid list provided: contains "+str(self.data.count(8))+" '8' characters when it should only have 1")
        xCount=0
        for x in stringIn:
            self.data[xCount//3][xCount%3]=x
            xCount +=1
        self.MeasurePerformance()

    def Swap(self,x,y):
        if x != self.bCoords[0] + 1 or x != self.bCoords[0] - 1:
            return False
        if y != self.bCoords[1] + 1 or y != self.bCoords[1] - 1:
            return False
        charToSwap = self.data[x][y]
        self.data[bCoords[0]][bCoords[1]] = charToSwap
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
        sys.exit("no b was found in this puzzle! "+str(puzzleIn))

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
        #counter = 0
        #for thisChar in puzzleString.split(","):
        #    #print("position:"+str(counter)+" is "+str(thisChar)+" and the x is "+str(counter//3)+" and the y is "+str(counter%3))
        #    self.Puzzle[counter//3][counter%3]=thisChar
        #    #print(self.Puzzle)
        #    counter+=1
        #if counter!=9:
        #    sys.exit("improper puzzle string of "+str(puzzleString)+" exiting.")
        #print(self.Puzzle)

    

    def Solve(self):
        #check to see if the initial configuration is the solved configuration
        #self.ListOfStates.clear()
        self.ListOfStates[1]=self.Puzzle
        print("initial list of states:")
        for existingState in self.ListOfStates:
            print(str(existingState))
        if self.ListOfStates[-1].__str__ == self.SolveState.__str__:
            return TRUE
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

    
