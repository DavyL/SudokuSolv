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
		for j in range(9):
			l.append((0,0))
	print(l)
	return l
def printSudoku(s):
	k = 0
	for i in s:
		k = k+1
		if k == 9:
			print(i[0])
		else:
			print(i[0], end = "")
def m2a(x, y):
	return x*9 + y


newEmptyGrid()
