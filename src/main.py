def cl_readSudoku(Filename):
	l=[]
	with open(Filename) as f:
		for line in f:
			for i in range(9):
				l.append((int(line[i]),[]))
	f.close()
	return l

#Read a file containing a sudoku
#File shall be a python list
def readSudoku(filename):
    fd = open(filename)
    l = fd.readlines()
    fd.close()
    return eval(l[0])

def newEmptyGrid():
	l = []
	for i in range(9):
		l.append([])
		for j in range(9):
			l[i].append((0,[1,2,3,4,5,6,7,8,9]))
	return l

def cl_printSudoku(s):
	k = 0
	for i in s:
		k = k+1
		if k == 9:
			print(i[0])
		else:
			print(i[0], end = "")

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
        
def computeCandidates(s):
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

def m2a(x, y):
	return x*9 + y

grid =	readSudoku("../grid/grid1.gr")
printSudoku(grid)
if (checkSudoku(grid) != ([],[])):
        print("OH DEAR, WE ARE IN TROUBLE")
