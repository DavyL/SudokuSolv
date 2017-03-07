def readSudoku(Filename):
	l=[]
	with open(Filename) as f:
		for line in f:
			for i in range(9):
				l.append((int(line[i]),[]))
	f.close()
	return l

def newEmptyGrid():
	l = []
	for i in range(9):
		l.append([])
		for j in range(9):
			l[i].append((0,[1,2,3,4,5,6,7,8,9]))
	return l

def printSudoku(s):
	k = 0
	for i in s:
		k = k+1
		if k == 9:
			print(i[0])
		else:
			print(i[0], end = "")

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

def fillGrid(grid):	
	grid[][1] = (8, None)
	grid[][2] = (7, None)
	grid[][6] = (9, None)
	grid[][7] = (9, None)
	grid[1][2] = (9, None)
	grid[1][2] = (9, None)
	grid[1][2] = (9, None)
	grid[1][2] = (9, None)
	grid[1][2] = (9, None)
	grid[1][2] = (9, None)
grid = newEmptyGrid()
grid[1][2] = (9, None)
print(grid)
