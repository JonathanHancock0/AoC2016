import os

def check(sides):
	print(f"Looking at a trongle with sides {sides[0]} {sides[1]} {sides[2]}")
	s = [int(side) for side in sides]
	if s[0] + s[1] <= s[2]:
		print(1)
		return False
	if s[0] + s[2] <= s[1]:
		print(2)
		return False
	if s[1] + s[2] <= s[0]:
		print(3)
		return False
	return True

def blockcount(block):
	total = 0
	if check([block[0][0] , block[1][0] , block[2][0]]):
		total += 1
	if check([block[0][1] , block[1][1] , block[2][1]]):
		total += 1
	if check([block[0][2] , block[1][2] , block[2][2]]):
		total += 1
	return total

if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "3.txt"))
	f = open(path)

	row = False
	good = 0
	if row:
		for line in f:
			sides = line.split()
			if check(sides):
				good += 1
	else:
		i = 0
		block = []
		for line in f:
			block.append(line.split())
			i += 1
			if i == 3:
				good += blockcount(block)
				block.clear()
				i = 0

	print(f"{good} good triangles found!")