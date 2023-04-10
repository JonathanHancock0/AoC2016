import os
import string

class LetterCounter:
	def __init__(self):
		alph = string.ascii_lowercase
		self.data = {}
		for letter in alph:
			self.data[letter] = 0
	
	def add(self, letter):
		old = self.data[letter]
		new = old + 1
		self.data[letter] = new

	def getMost(self):
		record = 0
		best_letter = "."
		for key in self.data:
			if self.data[key] > record:
				record = self.data[key]
				best_letter = key
		return best_letter
	
	def getLeast(self):
		record = 9999
		best_letter = "."
		for key in self.data:
			if self.data[key] < record and self.data[key] != 0:
				record = self.data[key]
				best_letter = key
		return best_letter

if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "6.txt"))
	f = open(path)

	lines = []
	modified = True
	for line in f:
		lines.append(line.strip('\n'))
	f.close()

	m_length = len(lines[0])		#They all have the same length so we can pick the first
	message = ""
	for i in range(m_length):
		counter = LetterCounter()
		for l in lines:
			counter.add(l[i])
		if modified:
			message = message + counter.getLeast()
		else:
			message = message + counter.getMost()

	print(f"The real message is {message}")
