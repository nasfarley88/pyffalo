#!/usr/bin/python3.2
endornot = "n"
gridmax = [11,7] # dimensions of the grid.
gridrep=[]

def print_grid():
	"""Prints the grid of play"""

	# print the header. TODO eventually make this based on gridmax[0]
	print('  a b c d e f g h i j k')
	for i in range(0,gridmax[1]):
		if i != 1 and i != gridmax[1]-1: 
			print(i, end=' ')
		else:
			for k in range(0,2*gridmax[0]+1): print('-',end='')
			print("\n",i, end=' ', sep='')
		for j in range (0,gridmax[0]):
			print(gridrep[i][j], end=' ', sep='')
		print()

# main program
# initialise grid
for i in range(0,gridmax[1]):
	gridrep.append([])
	for j in range(0,gridmax[0]):
		gridrep[i].append('.')


while endornot != 'c':
	endornot = input("(c)ontinue, (g)rid or (r)epeat\n")
	if endornot == 'g':
		print_grid()