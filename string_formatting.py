n = int(input())
width = len(str(bin(n)[2:]))
for x in range(1, n+1):
	for base in 'doXb':
		print('{0:{width}{base}}'.format(x, base=base, width=width), end=' ')
	print()