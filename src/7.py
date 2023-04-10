import os

def TLStest(ip):
	hyper = False
	good = False
	for i in range(len(ip) - 3):
		seq = ip[i] + ip[i+1] + ip[i+2] + ip[i+3]
		if '[' in seq:
			hyper = True
			continue
		if seq[0] == ']':	#The next sequence is out of the []
			hyper = False
			continue
		if seq[0] != seq[1] and seq[0] == seq[3] and seq[1] == seq[2]:
			if hyper:
				return False
			else:
				good = True
	if good:
		return True
	return False

def SSLtest(ip):
	word = ""
	supernet = []		#Outside []
	hypernet = []		#Inside []
	for char in ip:
		if char == '[':
			supernet.append(word)
			word = ""
		elif char == ']':
			hypernet.append(word)
			word = ""
		else:
			word = word + char
	supernet.append(word)
	
	for s_block in supernet:
		for i in range(len(s_block) - 2):
			seq = s_block[i] + s_block[i+1] + s_block[i+2]
			if seq[0] == seq[2] and seq[0] != seq[1]:	#Valid ABA
				BAB = seq[1] + seq[0] + seq[1]
				for h_block in hypernet:
					for j in range(len(h_block)-2):
						if h_block[j:j+3] == BAB:
							return True
	return False

if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "7.txt"))
	f = open(path)

	TLS_count = 0
	SSL_count = 0
	for line in f:
		ip = line.strip('\n')
		if TLStest(ip):
			TLS_count += 1
		if SSLtest(ip):
			SSL_count += 1
	f.close()
	print(f"{TLS_count} IP addresses support TLS")
	print(f"{SSL_count} IP addresses support SSL")