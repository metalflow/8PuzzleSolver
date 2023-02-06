#imports
import sys

class Puzzle:
    #initialize variables
    #data = [[0,0,0],[0,0,0],[0,0,0]]
    #bCoords = [-1,-1]
    #performanceScore = 0
    #inversionCount=0

    def ProcessList(self,listIn):
        self.data = [[0,0,0],[0,0,0],[0,0,0]]
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
        self.data = [[0,0,0],[0,0,0],[0,0,0]]
        xCount=0
        for x in stringIn.split(','):
            if str(x).find('b') == -1:
                self.data[xCount//3][xCount%3]=int(x)
            else:
                self.bCoords=[xCount//3,xCount%3]
                self.data[xCount//3][xCount%3]='b'
            xCount +=1
            
        return

    #constructor
    def __init__(self,puzzleIn : 'Puzzle'):
        self.data = puzzleIn.data.copy()
        self.bCoords = puzzleIn.bCoords.copy()
        self.performanceScore = puzzleIn.performanceScore
        self.parent=""

    def __init__(self,inVar):
        self.inversionCount = 0
        if type(inVar) == str:
            self.ProcessString(inVar)
        elif type(inVar) == list:
            self.ProcessList(inVar)
        else:
            raise Exception("invalid parameter type of "+str(type(inVar))+"passed.  Please only pass strings or lists")
        self.ValidatePuzzle()
        #if self.inversionCount%2 != 0:
        #    raise Exception("this is not a solvable puzzle because it has an odd number of inversions:"+str(self.inversionCount))
        self.MeasurePerformance()
        self.parent=""

    def Swap(self,x,y):
        if x > self.bCoords[0] + 1 or x < self.bCoords[0] - 1:
            return False
        if y > self.bCoords[1] + 1 or y < self.bCoords[1] - 1:
            return False
        charToSwap = self.data[x][y]
        self.data[self.bCoords[0]][self.bCoords[1]] = charToSwap
        self.data[x][y] = 'b'
        self.bCoords[0]=x
        self.bCoords[1]=y
        self.MeasurePerformance()
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
        return

    def MeasurePerformance(self):
        self.performanceScore=0
        self.badTilePerformanceScore=0
        self.myPerformanceScore=0
        xCounter=0
        tileCounter=0
        #calculate the manhatten distance
        for x in self.data:
            yCounter=0
            for y in x:
                tileCounter+=1
                if y == 'b':
                    distance = 0
                    #distance = abs(2-xCounter) + abs(2-yCounter)
                else:
                    distance = abs(((y-1)//3)-xCounter) + abs(((y-1)%3)-yCounter)
                    if y != tileCounter:
                        self.badTilePerformanceScore+=1
                self.performanceScore+=distance
                yCounter+=1
            xCounter+=1
        return

class Puzzle8():
    
    #SearchType = ""
    #ListOfStates = []
    SolveState=Puzzle([[1,2,3],[4,5,6],[7,8,'b']])
    #frontierStates = []

    #def __del__(self):
    #    self.SearchType = ""
    #    self.ListOfStates.clear()
    def GetPerformance(self,puzzle):
        if self.perfType=="manhatten":
            return puzzle.performanceScore
        elif self.perfType=="badTile":
            return puzzle.badTilePerformanceScore
        elif self.perfType=="myPerf":
            return puzzle.myPerformanceScore
        else:
            return 0

    def __init__(self,search,puzzleIn : Puzzle):
        self.ListOfStates = []
        self.SearchType = search
        self.perfType = "manhatten"
        self.ListOfStates.append(puzzleIn)
        #make list of frontier states
        self.frontierStates = []

    def __init__(self,search,puzzleString : str):
        self.ListOfStates = []
        self.SearchType = search
        self.perfType = "manhatten"
        self.ListOfStates.append(Puzzle(puzzleString))
        #make list of frontier states
        self.frontierStates = []

    def reset(self):
        #initalPuzzle = self.ListOfStates[0]
        self.ListOfStates.clear
        #self.ListOfStates.append(initalPuzzle)
        self.frontierStates.clear

    def isUsed(self,newPuzzle : Puzzle):
        for existingState in self.ListOfStates:
            if str(newPuzzle.data) == str(existingState.data):
                #check to see if newPuzzle has a lower performance score than existing puzzle
                if newPuzzle.performanceScore < existingState.performanceScore:
                    existingState = newPuzzle
                #this state has already been used
                return True
        for existingFrontier in self.frontierStates:
            if str(newPuzzle.data) == str(existingFrontier.data):
                #check to see if newPuzzle has a lower performance score than existing puzzle
                if newPuzzle.performanceScore < existingFrontier.performanceScore:
                    existingState = newPuzzle
                #this state has already been added to the frontier
                return True
        return False

    def BestFirstSolve(self):
        self.depth=0
        #check to see if the initial configuration is the solved configuration
        #print("initial list of states:")
        #for existingState in self.ListOfStates:
        #    print(existingState.data)
        if str(self.ListOfStates[-1].data) == str(self.SolveState.data):
            #we found our solution, return true
            return True
        else:
            #add frontier nodes
            if self.ListOfStates[-1].bCoords[0] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] - 1,self.ListOfStates[-1].bCoords[1])
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[0] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] + 1,self.ListOfStates[-1].bCoords[1])
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] -1)
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] +1)
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
        #sort the frontier nodes by performance score
        self.frontierStates.sort(reverse=True,key=self.GetPerformance)
        #order through the frontiers
        for nextFrontier in range(len(self.frontierStates)):
            if self.BestFirstSubSolve(self.frontierStates.pop()):
                return True
        #if none returned true, we failed
        self.ListOfStates.pop()
        return False

    def BestFirstSubSolve(self,puzzleIn):
        self.depth+=1
        if self.depth>900:
            print("hit depth 900, rejecting for safety")
            return False
        adjacentStates=[]
        self.ListOfStates.append(puzzleIn)
        #print("current list of states:")
        #for existingState in self.ListOfStates:
        #    print(existingState.data)
        if str(self.ListOfStates[-1].data) == str(self.SolveState.data):
            #we found our solution, return true
            return True
        else:
            #add frontier nodes
            if self.ListOfStates[-1].bCoords[0] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                try:
                    newPuzzle = Puzzle(self.ListOfStates[-1].data)
                    newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] - 1,self.ListOfStates[-1].bCoords[1])
                    #check to see if this puzzle already exists in ListOfStates
                    if self.isUsed(newPuzzle) == False:
                        if self.SearchType=="A*":
                            newPuzzle.performanceScore+=self.depth
                        self.frontierStates.append(newPuzzle)
                        adjacentStates.append(newPuzzle)
                    del newPuzzle
                except:
                    print("did not add invalid state:")
            if self.ListOfStates[-1].bCoords[0] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] + 1,self.ListOfStates[-1].bCoords[1])
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    if self.SearchType=="A*":
                        newPuzzle.performanceScore+=self.depth
                    self.frontierStates.append(newPuzzle)
                    adjacentStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] -1)
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    if self.SearchType=="A*":
                        newPuzzle.performanceScore+=self.depth
                    self.frontierStates.append(newPuzzle)
                    adjacentStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] +1)
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    if self.SearchType=="A*":
                        newPuzzle.performanceScore+=self.depth
                    self.frontierStates.append(newPuzzle)
                    adjacentStates.append(newPuzzle)
                del newPuzzle
        #sort the adjacent nodes by performance score
        adjacentStates.sort(reverse=True,key=self.GetPerformance)
        #sort the frontier nodes by performance score
        self.frontierStates.sort(reverse=True,key=self.GetPerformance)
        #order through the frontiers
        for nextState in range(len(adjacentStates)):
            stateToCheck=adjacentStates.pop()
            if self.BestFirstSubSolve(stateToCheck):
                return True
            else:
                self.frontierStates.pop(self.frontierStates.index(stateToCheck))
        #if none returned true, we failed
        self.ListOfStates.pop()
        self.depth-=1
        return False

    def AStarSolve(self):
        self.depth=0
        self.ListOfStates[-1].parent=""
        if str(self.ListOfStates[-1].data) == str(self.SolveState.data):
            #we found our solution, return true
            return True
        else:
            #add frontier nodes
            if self.ListOfStates[-1].bCoords[0] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] - 1,self.ListOfStates[-1].bCoords[1])
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[0] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] + 1,self.ListOfStates[-1].bCoords[1])
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] -1)
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] +1)
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
        #sort the frontier nodes by performance score
        self.frontierStates.sort(reverse=True,key=self.GetPerformance)
        #order through the frontiers
        while len(self.frontierStates)>0:
            if self.AStarSubSolve(self.frontierStates.pop()):
                reportableStates = []
                backtrackPuzzle = self.ListOfStates[-1]
                while backtrackPuzzle.parent != "":
                    reportableStates.insert(0,backtrackPuzzle)
                    backtrackPuzzle = backtrackPuzzle.parent
                self.ListOfStates = reportableStates
                return True
        #if none returned true, we failed
        return False

    def AStarSubSolve(self,puzzleIn):
        self.depth+=1
        if self.depth>900:
            print("hit depth 900, rejecting for safety")
            return False
        self.ListOfStates.append(puzzleIn)
        if str(self.ListOfStates[-1].data) == str(self.SolveState.data):
            #we found our solution, return true
            return True
        else:
            #add frontier nodes
            if self.ListOfStates[-1].bCoords[0] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] - 1,self.ListOfStates[-1].bCoords[1])
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[0] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0] + 1,self.ListOfStates[-1].bCoords[1])
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] - 1 >= 0:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] -1)
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
            if self.ListOfStates[-1].bCoords[1] + 1 < 3:
                #create a puzzle with the blank moved up one row
                newPuzzle = Puzzle(self.ListOfStates[-1].data)
                newPuzzle.Swap(self.ListOfStates[-1].bCoords[0],self.ListOfStates[-1].bCoords[1] +1)
                newPuzzle.parent = self.ListOfStates[-1]
                #newPuzzle.ValidatePuzzle()
                #check to see if this puzzle already exists in ListOfStates
                if self.isUsed(newPuzzle) == False:
                    self.frontierStates.append(newPuzzle)
                del newPuzzle
        #sort the frontier nodes by performance score
        self.frontierStates.sort(reverse=True,key=self.GetPerformance)
        #order through the frontiers
        while len(self.frontierStates) > 0:
            if self.AStarSubSolve(self.frontierStates.pop()):
                return True
        #if none returned true, we failed
        return False