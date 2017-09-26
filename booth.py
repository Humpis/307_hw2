import sys

file = open(sys.argv[1], 'r')
room = 0
position = 0, 0
target = 0, 0
horizon = 10
for line in file:
    line = line.strip()
    if line == '':
        continue
    print(line)
    if line[0:4] == 'room':
        # print(line[8:9])
        w = int(line[5:6])
        h = int(line[8:9])
        room = [[0 for x in range(w)] for y in range(h)]
        print(room)
    elif line[0:6] == 'booths':
        booths = [int(line[7:8]) + 1]
    elif line[0:9] == 'dimension':
        booths[int(line[10:11])] = [int(line[13:14]), int(line[16:17])]
