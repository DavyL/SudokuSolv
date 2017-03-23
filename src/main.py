#Read a file containing a sudoku
#File shall be a python list
def readSudoku(filename):
    fd = open(filename)
    l = fd.readlines()
    fd.close()
    return eval(l[0])

#Creates a standard grid cointaining no elements and every possible candidates
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
    for numLine in range(9):
        for elem in range(9):
            grid[numLine][elem] = (grid[numLine][elem], [i for i in range(1,10)]) 
    cleanTrivialCand(grid)
    cleanSGrid(grid)
    return grid

#Takes a standard grid in parameters and returns a classic grid
def SGrid2Grid(SGrid):
    for numLine in range(9):
        for elem in range(9):
            SGrid[numLine][elem] = SGrid[numLine][elem][0]
    return SGrid

#Checks for non zero values of a standard grid
#When found their second members switch to an empty list
def cleanSGrid(SGrid): 
    SGrid = cleanBasic(SGrid)
    SGrid = rule3(SGrid)
    SGrid = rule4(SGrid) 

    return SGrid

#returns True if a candidate appears only once in candidate list of a whole line
def isAlone(SLine, cand):
    occur = 0
    for elem in SLine:
        if cand in elem[1]:
            occur += 1
            if occur > 1:
                return False
    
    if occur == 1:
        return True
    
    return False

#Regroups rule 1 and rule 2 inside a single function
#If a candidates appears only once in a line or a column or a square
#Or if it's the only candidate of the element
#Then it becomes a value
def cleanBasic(SGrid):
    SGrid = cleanLine(SGrid)
    SGrid = cleanColumns(SGrid)
    SGrid = cleanSquare(SGrid) 

    return SGrid

#Rule 3 applied in line
#If a candidate appears only once in the candidates of a line removes it
def rule3Line(SGrid):
    for cand in range(1, 10):
        for line in range(9):
            if isAlone(SGrid[line], cand):
                #print(cand, " APPEARS ONLY ONCE AT LINE ", line)
                for column in range(9):
                    if cand in SGrid[line][column][1]:
                        SGrid[line][column] = (cand, [])
                        #updateLineCand(SGrid[line])
                        cleanBasic(SGrid)
    return SGrid

#Rule 3 applied in columns
def rule3Column(SGrid):
    SGrid = retColumns(SGrid)
    SGrid= rule3Line(SGrid)
    SGrid = retColumns(SGrid)
    
    return SGrid

#Rule 3 applied to a whole grid applied in lines and in columns
def rule3(SGrid):
    SGrid = rule3Line(SGrid)
    SGrid = rule3Column(SGrid)

    return SGrid

#Returns 0 if there is not two candidates in the same row of a square that are the same
def isAlign(SLine, column, cand):
    occur = 0
    for elem in SLine[(column//3)*3: (column//3)*3 + 3]:
        if cand in elem[1]:
            occur += 1
    if occur >= 2:
        return occur
    return 0

#returns true if occcur appears elsewhere in square
def isInSquare(SGrid, line, column, occur, cand):
    SSquare = square2Line(SGrid)
    for elem in SSquare[(line//3) * 3 + column // 3]:
        if cand in elem[1]:
            #print(cand, "APPEARS IN GRID")
            occur -= 1
    square2Line(SGrid)    
    if occur == 0:
        return False
    else: 
        return True
            
#Rule 4 applied to a line
#Checks if a candidates appears several times in a row, and nowhere else in their square
#If it's the case, then same candidates from the line can be removed
def rule4Line(SGrid):
    for cand in range(1,10):
        for line in range(0,9):
            for column in range(0,9):
                occur = isAlign(SGrid[line], column, cand)
                if occur != 0:
                    #print("AT LINE ", line, " AND COLUMN ", column, " THE CANDIDATE : ", cand, "APPEARS : ", isAlign(SGrid[line], column, cand))
                    if not isInSquare(SGrid, line, column, occur, cand):
                        #print("AT LINE ", line, " AND COLUMN ", column, " THE CANDIDATE : ", cand, "APPEARS : ", occur, "AND IT APPEARS NOWHERE ELSE IN THE SQUARE")                        
                        excludedColumns =  excludeColumns(column)
                        for col in range(9):
                            if cand in SGrid[line][col][1] and not col in excludedColumns  :
                                #printSudoku(SGrid)
                                SGrid[line][col][1].remove(cand)
                                #print("remove ", cand, " at column ", col, " and line ", line)
    return cleanBasic(SGrid)

#Returns a list containing column number of elements that are in the same square than column
def excludeColumns(column):
    return [ (column//3) * 3 + i for i in range(3)]

#Rule 4 applied for columns only
def rule4Columns(SGrid):
    SGrid = retColumns(SGrid)
    SGrid = rule4Line(SGrid)
    SGrid = retColumns(SGrid)
    return SGrid

#Rule 4 applied in the 2 ways, by lines and by columns
def rule4(SGrid):
    SGrid = rule4Line(SGrid)
    SGrid = rule4Columns(SGrid)

    return SGrid

#Main function for sudoku solving
def solveGrid(SGrid):
    candNum = 1
    while candNum > 0:
        candNum = 0
        for line in range(9):
            for elem in range(9):
                candNum += len(SGrid[line][elem][1])
        print("Candidates left : ", candNum, "candidates found : ", countValues(SGrid))
        printSudoku(SGrid) 
        SGrid = cleanSGrid(SGrid)
        
    return SGrid

#Counts the number of candidates left
def countCandidates(SGrid):
    candNum = 0
    for line in range(9):
        for elem in range(9):
            candNum+= len(SGrid[line][elem][1])
    print("Candidates left : ", candNum)
    return candNum
            
#If there is already a value removes candidates
#Shall only be used at init
def cleanTrivialCand(SGrid):
    for lineNum in range(9):            
        for elem in range(9):
            if SGrid[lineNum][elem][0] != 0:
                SGrid[lineNum][elem] = (SGrid[lineNum][elem][0], [])
    return SGrid

#Removes from candidates values that are already in the same line
#Parses a grid
def cleanLine(SGrid):
    for i in range(9):
        if(updateLineCand(SGrid[i])):
            cleanLine(SGrid)

        for elemNum in range(9):
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

#Removes from candidates values that are already in the same square
#Parses a grid
def cleanSquare(SGrid):
    SGrid = square2Line(SGrid)
    cleanLine(SGrid)
    SGrid = square2Line(SGrid)

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
                cand = SLine[elemNum][1][SLineLen - 1 - candNum]
                if (cand, []) in SLine:
                    SLine[elemNum][1].remove(cand)
                    return 1
    return 0

#Prints the Sudoku
def printSudoku(grid):
    for line in range(9):
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

#Returns a SGrid containing squares as lines
#line 0 : square 0,0
#line 1 : square 0,1
#line 2 : square 0,2
#...
#line 8 : square 2,2
def square2Line(SGrid):
    squareGrid = []
    for line in range(9):
        squareGrid.append([])
    count = 0
    for line in range(3):
        for i in SGrid[line][0:3] : 
            squareGrid[0].append(i)
        for j in SGrid[line][3:6]:
            squareGrid[1].append(j)
        for k in SGrid[line][6:9]:
            squareGrid[2].append(k)

    for line in range(3,6):
        for i in SGrid[line][0:3] : 
            squareGrid[3].append(i)
        for j in SGrid[line][3:6]:
            squareGrid[4].append(j)
        for k in SGrid[line][6:9]: 
            squareGrid[5].append(k)

    for line in range(6,9):
        for i in SGrid[line][0:3] : 
            squareGrid[6].append(i)
        for j in SGrid[line][3:6]:
            squareGrid[7].append(j)
        for k in SGrid[line][6:9]: 
            squareGrid[8].append(k)

    
    #squareGrid.append(SGrid[1][0:3])
    #squareGrid.append(SGrid[2][0:3])
    return squareGrid

#Checks if the sudoku respects the rules
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

def countValues(SGrid):
    count = 0
    for line in range(9):
        for column in range(9):
            if SGrid[line][column][0] != 0:
                count += 1

    return count

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

#This one is solved applying only rule 1 and 2        
#grid =	readSudoku("../grid/grid3.gr")

#This one is solved applying only rule 1, 2 and 3
#grid = readSudoku("../grid/grid4.gr")


#This one is solved applying rule 1, 2, 3 and 4
grid = readSudoku("../grid/grid5.gr")
 
printSudoku(grid)
if (checkSudoku(grid) != ([],[])):
        print("OH DEAR, WE ARE IN TROUBLE")

SGrid = grid2SGrid(grid)

SGrid = solveGrid(SGrid)

SGrid = SGrid2Grid(SGrid)

print("Solved grid : ")

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

