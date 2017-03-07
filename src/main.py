def readSudoku(Filename):
	l=[]
	with open(Filename) as f:
		for line in f:
			for i in range(9):
				l.append((int(line[i],[])))
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
