#!/usr/bin/python3.2
endornot = "n"
gridmax = [11,7]
gridrep=[]

def print_grid():
	for i in range(0,gridmax[1]):
		for j in range (0,gridmax[0]):
			print(gridrep[i][j], end=' ', sep='')
		print()

#initialise grid
for i in range(0,gridmax[1]):
	gridrep.append([])
	for j in range(0,gridmax[0]):
		gridrep[i].append(i)


while endornot != 'c':
	endornot = input("(c)ontinue, (g)rid or (r)epeat\n")
	if endornot == 'g':
		print_grid()
