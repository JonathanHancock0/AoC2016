import os

if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "23.txt"))
	f = open(path)