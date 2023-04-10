import hashlib
import os

def display(p_list):
	os.system('cls')
	word = ""
	for c in p_list:
		word = word + c
	print(word)

if __name__ == '__main__':
	door_id = "abbhdwsy"
	p_len = 8
	password = ['_'] * p_len
	i = 0
	while True:
		index = door_id + str(i)
		hash = hashlib.md5(index.encode('utf-8')).hexdigest()
		if hash[:5] == '00000':
			try:
				pos = int(hash[5])
				if pos < p_len and password[pos] == '_':
					password[pos] = hash[6]
					display(password)
					
					if '_' not in password:
						break
			except:
				pass
		i += 1
	print(f"Decryption complete!")