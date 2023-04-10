import os

def walk(text):
	direction = 0
	x = 0
	y = 0
	positions = [(0,0)]
	for command in text:
		if command[0] == "L":
			direction -= 1
		else:
			direction += 1
		if direction == -1:
			direction = 3
		if direction == 4:
			direction = 0
		
		distance = int(command[1:])
		match direction:
			case 0:		#North
				for _ in range(distance):
					y += 1
					if (x,y) in positions:
						return (x,y)
					positions.append((x,y))
			case 1:		#East
				for _ in range(distance):
					x += 1
					if (x,y) in positions:
						return (x,y)
					positions.append((x,y))
			case 2:		#South
				for _ in range(distance):
					y -= 1
					if (x,y) in positions:
						return (x,y)
					positions.append((x,y))
			case 3:		#West
				for _ in range(distance):
					x -= 1
					if (x,y) in positions:
						return (x,y)
					positions.append((x,y))

		print(f"Turning {command[0]}. Moving {command[1:]} spaces in direction {direction}. Moving to ({x},{y}).")

if __name__ == '__main__':
	dirname=os.path.dirname
	path = os.path.join(dirname(dirname(__file__)), os.path.join("inputs", "1.txt"))
	f = open(path)
	text = f.readline()
	f.close()
	text = text.split(", ")
	
	coords = walk(text)
	
	print(f"First position visited twice is ({coords[0]},{coords[1]}). Manhattan distance of {abs(coords[0])+abs(coords[1])}")
	