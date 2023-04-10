import os
import string

class Ranking:
	def __init__(self):
		self.scores = {}
		for char in string.ascii_lowercase:				#This is the alphabet
			self.scores[char] = 0						#Starts each score as 0

	def __str__(self):
		return str(self.scores)

	def increment(self, letter):
		if letter != '-':
			self.scores[letter] += 1

	def winners(self):
		out = ""
		for _ in range(5):
			best = max(self.scores, key = lambda k: self.scores[k])		#key with biggest value
			out = out + best
			self.scores[best] = -1										#We will never pick this again!
		return out

def decrypt(data):		#data is a tuple of a string then a shift
	text = data[0]
	shift = data[1]
	new_text = ""
	for char in text:
		if char == '-':
			new_text = new_text + ' '
		else:
			c_val = ord(char) + (shift % 26)
			if c_val > 122:		#This is z
				c_val -= 26
			new_text = new_text + chr(c_val)
	return new_text



if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "4.txt"))
	f = open(path)

	real = []
	sum = 0
	for line in f:
		r = Ranking()
		words = line.strip('\n').split('-')
		
		info  = words[-1]
		s_info = info.split('[')
		id = s_info[0]
		checksum = s_info[1][:-1]	#Cuts off the final ]
		room = "-".join(words[:-1])
		
		for char in room:
			r.increment(char)
		target = r.winners()
		if target == checksum:
			sum += int(id)
			real.append((room , int(id)))
	
	print(f"Sum of all valid ids is {sum}.")
	for r in real:
		decrypted = decrypt(r)
		if "north" in decrypted:
			print(f"{decrypted} has room id {r[1]}")
			break

		