

#Read a file containing a sudoku
#File shall be a python list
def readSudoku(filename):
    fd = open(filename)
    l = fd.readlines()
    fd.close()
    return eval(l[0])

#Creates a standard grid cointaining no elements
def newEmptyGrid():
	l = []
	for i in range(9):
		l.append([])
		for j in range(9):
			l[i].append((0,[1,2,3,4,5,6,7,8,9]))
	return l

#Takes a grid containing only list containing line elements
#Returns a grid containing each elements from input and all of the possible candidates as tuple
def grid2SGrid(grid):
    for numLine in range(len(grid)):
        for elem in range(9):
            grid[numLine][elem] = (grid[numLine][elem], [i for i in range(1,9)]) 
    cleanSGrid(grid)
    return grid

#Checks for non zero values of a standard grid
#When found their second members switch to an empty list
def cleanSGrid(SGrid):
    
    cleanTrivialCand(SGrid)    
    cleanLine(SGrid)
    cleanColumns(SGrid) 
    cleanLine(SGrid)
    return SGrid

#If there is already a value removes candidates
def cleanTrivialCand(SGrid):
    for lineNum in range(9):            #Cleans trivial values
        for elem in range(9):
            if SGrid[lineNum][elem][0] != 0:
                SGrid[lineNum][elem] = (SGrid[lineNum][elem][0], [])
    return SGrid

#Removes from candidates values that are already in the same line
#Parses a grid
def cleanLine(SGrid):
    for i in range(9):                  #Cleans line
        SGrid[i] = updateLineCand(SGrid[i])
        for elemNum in range(len(SGrid[i])):
            if SGrid[i][elemNum][0] == 0:
                if len(SGrid[i][elemNum][1]) == 1:
                    SGrid[i][elemNum] = (SGrid[i][elemNum][1][0], [])
    return SGrid

#Removes from candidates values that are already in the same columns
#Parses a grid
def cleanColumns(SGrid):    
    SGrid = retColumns(SGrid)
    cleanLine(SGrid)
    SGrid = retColumns(SGrid)
   
    return SGrid

#If there's only one single candidate, then sets it as a value
#Parses the whole grid
def swapSingleCand(SGrid):
    for lineNum in range(9):
        SGrid[lineNum] = swapSingleCandLine(SGrid[lineNum])
    return SGrid


#If there's only one single candidate, then sets it as a value
#Parses only a line
def swapSingleCandLine(SLine):
    for elemNum in range(9):
        if len(SLine[elemNum][1]) == 1:
            SLine[elemNum] = (SLine[elemNum][1][0], [])

    return SLine

#Updates the candidates of a line
def updateLineCand(SLine):
    for elemNum in range(9):
        if SLine[elemNum][0] == 0:
            SLineLen = len(SLine[elemNum][1])
            for candNum in range(SLineLen):
                cand = SLine[elemNum][1][SLineLen -1 - candNum]
                if (cand, []) in SLine:
                    SLine[elemNum][1].remove(cand)
    return SLine

#Prints the Sudoku
def printSudoku(grid):
    for line in range(len(grid)):
        print(grid[line])


#Returns a list of all the columns of the sudoku
def retColumns(grid):
    columns = []
    for i in range(9):
        columns.append([])
    for line in grid:
        for i in range(9):
            columns[i].append(line[i])
    return columns


#Checks if the respects the rules
#Checks lines then columns
#return the lists containing issues inside lines then inside columns
#If the grid contains no zero value then each list are the same 
def checkSudoku(grid):
    issueL = []
    for line in grid:
        if checkLine(line) != []:
            issueL.append(checkLine(line))
    issueC = []
    for columns in retColumns(grid):
        if checkLine(columns) != []:
            issueC.append(checkLine(columns))
    return issueL, issueC

    

#Checks if each element of a line appears only once
#Returns a list containing each value that appears more than once
def checkLine(line):
    issue = []
    for j in range(1,9):
        count = 0
        for i in line:
            if i == j:
                count +=1
            if(count > 1):
                issue.append(j)

    return list(set(issue))
        
grid =	readSudoku("../grid/grid1.gr")
grid[2][2] = 0
grid[2][3] = 0 
printSudoku(grid)
if (checkSudoku(grid) != ([],[])):
        print("OH DEAR, WE ARE IN TROUBLE")
SGrid = grid2SGrid(grid)
printSudoku(SGrid)


##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################















#All of functions below have been written by teacher
#They are here just in case they might turn out to be useful
#They will probably be removed soon

def cl_computeCandidates(s):
	for i in range(9):
		for j in range(9):
			e = s[m2a(i,j)]
			if e[0] == 0:
				for k in range(9):
					ec = s[m2a(k,j)]
					el = s[m2a(i,k)]
					if ec[0]!=0 and ec[0] in e[1]:
						e[1].remove(ec[0])
					if el[0] != 0 and el[0] in e[1]:
						e[1].remove(el[0])

def cl_m2a(x, y):
	return x*9 + y

def cl_readSudoku(Filename):
	l=[]
	with open(Filename) as f:
		for line in f:
			for i in range(9):
				l.append((int(line[i]),[]))
	f.close()
	return l

def cl_printSudoku(s):
	k = 0
	for i in s:
		k = k+1
		if k == 9:
			print(i[0])
		else:
			print(i[0], end = "")

