#imports

import sys


class Puzzle8():
    SearchType = ""
    Puzzle = [[0,0,0],[0,0,0],[0,0,0]]
    ListOfStates = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
    SolveState=[[1,2,3],[4,5,6],[7,8,'b']]

    def __init__(self,search,puzzleIn):
        self.SearchType = search
        self.Puzzle = puzzleIn

    def __init__(self,search,puzzleString):
        self.SearchType = search
        counter = 0
        for thisChar in puzzleString.split(","):
            #print("position:"+str(counter)+" is "+str(thisChar)+" and the x is "+str(counter//3)+" and the y is "+str(counter%3))
            self.Puzzle[counter//3][counter%3]=thisChar
            #print(self.Puzzle)
            counter+=1
        if counter!=9:
            sys.exit("improper puzzle string of "+str(puzzleString)+" exiting.")
        #print(self.Puzzle)

    def Swap(self,puzzleIn,x,y):
        bCoords = self.FindBCoords(puzzleIn)
        puzzleOut = puzzleIn.copy()
        charToSwap = puzzleIn[x][y]
        puzzleOut[bCoords[0]][bCoords[1]] = charToSwap
        puzzleOut[x][y] = 'b'
        return puzzleOut

    def FindBCoords(self,puzzleIn):
        for x in range(len(puzzleIn)):
            for y in range(len(puzzleIn[x])):
                if puzzleIn[x][y] == 'b':
                    return [x,y]
        sys.exit("no b was found in this puzzle! "+str(puzzleIn))

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

    
