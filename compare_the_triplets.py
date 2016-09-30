def read_int(line):
	line = line.split()
	for n in range(len(line)):
		line[n] = int(line[n])
	return line

line1 = read_int(input())
line2 = read_int(input())

score1, score2 = 0, 0

for i in range(len(line1)):
	if line1[i] == line2[i]:
		continue
	elif line1[i] > line2[i]:
		score1 += 1
	else:
		score2 += 1
		
print(score1, score2)