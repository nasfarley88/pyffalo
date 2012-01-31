#!/usr/bin/python3.2
import re

endornot = "n"
gridmax = [11,7] # dimensions of the grid.
gridrep=[]

class Piece:
	"""A class for the pieces on the grid"""
	x = 0
	y = 0
	type = 'p'
	def return_piece(self):
		return [self.x,self.y,self.type]
	def move(self):
		start_coord = input('Please enter the co-ordinates of the piece you wish to move')
		if test_coord(start_coord):
			finish_coord = input('Where would you like to move it?')
			if test_coord(finish_coord):
				for i in range(0,len(piece_list)):
					if piece_list[i].x == finish_coordx: break
					if piece_list[i].y == finish_coordy: break


def extract_x():
	"""This is to get the x value from a human input of coordinates

	This should only be run after test_coord()"""
	x = input('test letter please')
	y = re.search('[a-k]', x)
	if y is MatchObject type:
		print(y.pos)
	print(x)


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
	if x == 'h': return 7
	if x == 'i': return 8
	if x == 'j': return 9
	if x == 'k': return 10

def test_coord(x):
	"""This function checks whether the coord is valid"""

	test_str= re.findall('[a-z]',x)
	testx = len(test_str)
	# I should sort with the pickle module how it would change with gridmax
	# Maybe some other time
	test_str = re.findall('[0-9]',x)
	testy = len(test_str)
	if testx != 1 or testy != 1:
		print('Invalid input')
		return False
	temp = len(re.findall('[a-g]',x)) + len(re.findall('[0-7]',x))
	if temp != 2:
		print('Coordinates out of range.')
		return False
	else:
		# If the function gets this far, the coordinate should be good!
		print('Good coordinates!') #TODO delete this after board is done.
		return True


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

# put some pieces on the table.
piece_list = []
for i in range(0,gridmax[0]):
	piece_list.append(Piece())
	gridrep[6][i] = piece_list[i].type

print_grid()


string = 'test string 123'
while endornot != 'c':
	endornot = input("Enter a coordinate:\n")
	test_coord(endornot)
	if endornot == 'd':
		extract_x()

