#!/usr/bin/python3.2
endornot = "n"
gridmax = [11,7] # dimensions of the grid.
gridrep=[]

def alpha_to_num(x):
	"""A function to change [a-g] into [0-6]

	This is just for the gridrep indicies"""

	if x == 'a': return 0
	if x == 'b': return 1
	if x == 'c': return 2
	if x == 'd': return 3
	if x == 'e': return 4
	if x == 'f': return 5
	if x == 'g': return 6

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
	if endornot == 'r':
		x = input("put in a letter, a to g")
		print(alpha_to_num(x))
