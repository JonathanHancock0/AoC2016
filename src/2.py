import os

class Buttons:
	def __init__(self, data):	#Data is a list of strings for each row (empty space is .)
		self.squares = {}
		for r, row in enumerate(data):
			for c, char in enumerate(row):
				if char != '.':
					self.squares[(r,c)] = char

	def test(self, row, col):
		return ((row, col) in self.squares)

	def getChar(self, row, col):
		return self.squares[row,col]

	def getStart(self):
		for coord in self.squares:
			if self.squares[coord] == '5':
				return coord


if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "2.txt"))
	f = open(path)

	grid1 = ["123", "456", "789"]
	grid2 = ["..1..", ".234.", "56789", ".ABC.", "..D.."]

	keypad = Buttons(grid2)
	start = keypad.getStart()

	row = start[0] 
	col = start[1]
	code = ""
	for instruction in f:
		for char in instruction:
			match char:
				case 'U':
					if keypad.test(row-1 , col):
						row -= 1
				case 'D':
					if keypad.test(row+1 , col):
						row += 1
				case 'L':
					if keypad.test(row , col-1):
						col -= 1
				case 'R':
					if keypad.test(row , col+1):
						col += 1
			#print(f"Moving {char}. Current button is {calc(row, col)}")
		code = code + keypad.getChar(row, col)
		#print(f"{calc(row, col)} added to code!")
	
	print(f"Code is {code}.")
		
