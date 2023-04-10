import os
import time

class Screen:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.grid = {}
		for i in range(x):
			for j in range(y):
				self.grid[(i,j)] = '.'

	def display(self):
		os.system('cls')
		out = ""
		for y in range(self.y):
			line = ""
			for x in range(self.x):
				line = line + self.grid[(x,y)]
			out = out + line + '\n'
		print(out)
	
	def count(self):
		count = 0
		for key in self.grid:
			if self.grid[key] == '#':
				count += 1
		return count

	def rect(self, x, y):
		for i in range(int(x)):
			for j in range(int(y)):
				self.grid[(i,j)] = '#'

	def	rotate_col(self, x, d):
		newcol = []
		for i in range(self.y):
			pos = i - d			#For d = 2 , the new position 3 is the old position 1
			while pos < 0:
				pos += self.y
			newcol.append(self.grid[(x,pos)])

		for y, val in enumerate(newcol):
			self.grid[(x,y)] = val

	def	rotate_row(self, y, d):
		newrow = []
		for i in range(self.x):
			pos = i - d
			while pos < 0:
				pos += self.x
			newrow.append(self.grid[(pos,y)])

		for x, val in enumerate(newrow):
			self.grid[(x,y)] = val



if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "8.txt"))

	s = Screen(50,6)
	f = open(path)
	for line in f:
		instruction = line.strip('\n').split()
		match instruction[0]:
			case "rect":
				data = instruction[1].split('x')
				s.rect(data[0], data[1])
			case "rotate":
				dist = instruction[4]
				pos = instruction[2].split('=')[1]
				if instruction[1] == "row":
					s.rotate_row(int(pos), int(dist))
				else:
					s.rotate_col(int(pos), int(dist))

		s.display()
		time.sleep(0.1)
	print(f"{s.count()} pixels are lit")
			