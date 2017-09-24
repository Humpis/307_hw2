import sys

file = open(sys.argv[1], 'r')

position = 0,0
target = 0,0
horizon = 10
for line in file:
	line = line.strip()
	if line == '':
		continue
	print(line)
	if line[0:4] == 'room':
		print(line[8:9])
		room = [int(line[5:6])][int(line[8:9])]
		print(room)