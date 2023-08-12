#!/usr/bin/python
#author: Mustafa SENTURK
#This script is to solve sudoku puzzles. There is one more function missing in this script. 
#For simple sudoku puzzles this script is enough as it is

# During my military service, there wasn't much for me to linger on other than the book. 
# There was plenty of time to think. When I couldn't read a book, 
# the only game I could play on the keypad phone was Sudoku. 
# After a while, when I realized that my mind was using certain algorithms while solving sudoku, 
# I decided to put it into software. After shaping it well in my head, 
# I wrote this python sketch the day after I got back from the military. 
#
# This is not perfet and much has to be done.
# Yet still it is capable of solving some of the sudoku puzzles
#
# I am going to develop new one within another language

from math import floor, ceil, sqrt
from copy import copy
import time
import json


a = \
[3, 0, 6, 5, 0, 8, 4, 0, 0,\
5, 2, 0, 0, 0, 0, 0, 0, 0,\
0, 8, 7, 0, 0, 0, 0, 3, 1,\
0, 0, 3, 0, 1, 0, 0, 8, 0,\
9, 0, 0, 8, 6, 3, 0, 0, 5,\
0, 5, 0, 0, 9, 0, 6, 0, 0,\
1, 3, 0, 0, 0, 0, 2, 5, 0,\
0, 0, 0, 0, 0, 0, 0, 7, 4,\
0, 0, 5, 2, 0, 6, 3, 0, 0]

b = \
[5, 3, 0, 0, 7, 0, 0, 0, 0,\
6, 0, 0, 1, 9, 5, 0, 0, 0,\
0, 9, 8, 0, 0, 0, 0, 6, 0,\
8, 0, 0, 0, 6, 0, 0, 0, 3,\
4, 0, 0, 8, 0, 3, 0, 0, 1,\
7, 0, 0, 0, 2, 0, 0, 0, 6,\
0, 6, 0, 0, 0, 0, 2, 8, 0,\
0, 0, 0, 4, 1, 9, 0, 0, 5,\
0, 0, 0, 0, 8, 0, 0, 7, 9]

c = \
[ 3, 0, 6, 5, 0, 8, 4, 0, 0,\
5, 2, 0, 0, 0, 0, 0, 0, 0 , \
0, 8, 7, 0, 0, 0, 0, 3, 1 , \
0, 0, 3, 0, 1, 0, 0, 8, 0 , \
9, 0, 0, 8, 6, 3, 0, 0, 5 , \
0, 5, 0, 0, 9, 0, 6, 0, 0 , \
1, 3, 0, 0, 0, 0, 2, 5, 0 , \
0, 0, 0, 0, 0, 0, 0, 7, 4 , \
0, 0, 5, 2, 0, 6, 3, 0, 0 ]

def draw_sudoku(sudoku):
	a = sudoku
	print("drawing..")
	row = int(sqrt(len(sudoku)))
	for i in range(row):
		line = ""
		for j in range(row):
			line += str(a[i*row + j ] )+ " "
		print(line)


def calc_posibility(sudoku, number):
	pos = [str(number)]
	for i in range(9):
		for j in range(9):
			present = True
			for row in range(9):
				if sudoku[row*9 + j]  == number or sudoku[i*9 + j] != 0:
					present = False
			for coloumn in range(9):
				if sudoku[i*9 + coloumn] == number or sudoku[i*9 + j] != 0 :
					present = False
			if present == False:
				pos += '0'
			else:
				pos += '1'
	pos.pop(0)
	print("calculated the posibility of number "+str(number))
	#drawSudoku(pos)
	return pos

def solve_posibleTiles(sudoku):
    posibles = [None]* 9
    for number in range(9):
        posibles[number] = calc_posibility(sudoku, number + 1)
    return posibles

def analyse_poses(posibles, number, sudoku):
    pos = posibles
    num = number
    sudoku = sudoku
    print("analaysing posibilities of "+str(num))
    draw_sudoku(pos)
    #looking for squares
    squareTile = [None]*9
    squarePosTile = [None]*9
    print("starting..")
 
    
    for sq in range (9):
        for i in range(3):
            for j in range(3):
                squareTile[i*3 + j] = copy(sudoku[floor(sq / 3) * 27 + i*9 + (sq % 3)*3 + j])
        if squareTile.count(number) == 1:
            draw_sudoku(squareTile)
            print("number in {} sq {} number ".format(sq, number))
            for i in range(3):
                for j in range(3):
                    pos[floor(sq / 3) * 27 + i*9 + (sq % 3)*3 + j] = '0'
    
        #looking at tiles for couple posibilities and deleting corresponding imposibles
        for i in range(3):
            for j in range(3):
                squarePosTile[i*3 + j] = copy(pos[floor(sq / 3) * 27 + i * 9 + (sq % 3) * 3 + j])
        if squarePosTile.count('1') == 2:
            for i in range(3):
                posSearcher = 0
                for j in range(3):
                    posSearcher += int(squarePosTile[i*3 + j])
                if posSearcher == 2:
                    tileCount = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                    print("sq {} row {} couple possib".format(sq, i))
                    tileCount.pop((sq % 3)*3)
                    tileCount.pop((sq % 3)*3)
                    tileCount.pop((sq % 3)*3)
                    for j in tileCount:
                        pos[floor(sq / 3) * 27 + i * 9 + j] = '0'
            for j in range(3):
                posSearcher = 0
                for i in range(3):
                    posSearcher += int(squarePosTile[i*3 + j])
                if posSearcher == 2:
                    tileCount = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
                    print("sq {} coloumn {} couple possib".format(sq, j))
                    tileCount.pop(floor(sq / 3)*3)
                    tileCount.pop(floor(sq / 3)*3)
                    tileCount.pop(floor(sq / 3)*3)
                    for i in tileCount:
                        pos[int(i) * 9 + (sq % 3) * 3 + j] = '0'
                
    

    print("probability tile...")               
    draw_sudoku(pos)
    return pos

def single_possiblity_inCell():
    pass

def update_sudoku(posibles, number, sudoku):
    sudoku = sudoku
    line = ['0']*9
    pos = posibles
    number = number
    global updated
    
    #looking at rows
    for i in range(9):
        for j in range(9):
            line[j] = copy(pos[i*9 + j])
        if line.count('1') == 1:
            print("Updated {} row {} number".format(i, number))
            updated = True
            for j in range(9):
                if pos[i*9 + j] == '1':
                    sudoku[i*9 + j] = number
                    pos[i*9 + j] = '0'
                    

    #looking at coloumns
    for j in range(9):
        for i in range(9):
            line[i] = copy(pos[i*9 + j])
        if line.count('1') == 1:
            print("Updated {} coloumn {} number".format(j, number))
            updated = True
            for i in range(9):
                if pos[i*9 + j] == '1':
                    sudoku[i*9 + j] = number
                    pos[i*9 + j] = '0'
                    
            
    #looking for squares
    squareTile = [None]*9
    for sq in range (9):
        for i in range(3):
            for j in range(3):
                squareTile[i*3 + j] = copy(pos[floor(sq / 3) * 27 + i*9 + (sq % 3)*3 + j])
                
        if squareTile.count('1') == 1:
            print("Updated {} sq {} number ".format(sq, number))
            updated = True
            for i in range(3):
                for j in range(3):
                    if pos[floor(sq / 3) * 27 + i*9 + (sq % 3)*3 + j] == '1':
                        sudoku[floor(sq / 3) * 27 + i*9 + (sq % 3)*3 + j] = number
                        
    return sudoku
#5325777031 ali usta

def look_singleCell_possib(posMatrix, sud, print_res=False):
    sud = sud
    possMat = posMatrix
    for n in range(81):
        poss_in_cell = ['0']*9
        for i in range(9):
            poss_in_cell[i] = possMat[i][n]
            if poss_in_cell[i] == '1':
                num = i+1
        if print_res == True:
            print(str(n)," ")
            print(poss_in_cell)
            print(poss_in_cell.count('1'))
        if poss_in_cell.count('1') == 1:
            sud[n] = num
            print("SINGLE CELL RESOLEVED")
            global updated
            updated = True
    return sud
                    

def solve_sudoku(sudoku):
    posibles = [['0']*81]*9
    draw_sudoku(sudoku)
    sudokuSolved = False
    posibles = solve_posibleTiles(sudoku)
    global updated
    updated = True
    start_time = time.time()
        

    while not sudokuSolved and updated :
        updated = False
        print("/n NewLoop /n")
        posibles = solve_posibleTiles(sudoku)
        for number in range(9):
            posibles[number] = analyse_poses(posibles[number], number+1, sudoku)
        for number in range(9):
            sudoku = update_sudoku(posibles[number], number + 1, sudoku)
        print("latest answers of Sudoku Tile")
        #drawSudoku(sudoku)

        print("/n NewLoop /n")
        posibles = solve_posibleTiles(sudoku)
        for number in range(9):
            posibles[number] = analyse_poses(posibles[number], number+1, sudoku)
        for number in range(9):
            sudoku = update_sudoku(posibles[number], number + 1, sudoku)
        print("latest answers of Sudoku Tile")

        sudoku = look_singleCell_possib(posibles, sudoku)
        draw_sudoku(sudoku)
        print("updated " + str(updated))
        sudokuSolved = True
        for num in range(9):
            if posibles[num].count('1') != 0:
                sudokuSolved = False
    time_elapsed = time.time() - start_time
    print("time required to solve  " + str(time_elapsed))


def check_input(sudoku):
    if type(sudoku) != list:
        return False
    if len(sudoku) != 81:
        return False
    return True

def main():
    print("this program solves sudoku puzzles.")
    print("enter sudoku puzle as a json array")
    sudoku_string = input()
    sudoku = json.loads(sudoku_string)
    is_input_ok = check_input(sudoku)
    if not is_input_ok:
        PromptImproperInput()
        return
    solve_sudoku(sudoku)
    input()


def main(sudoku):
    is_input_ok = check_input(sudoku)
    if not is_input_ok:
        PromptImproperInput()
        return
    solve_sudoku(sudoku)
    input()

def PromptImproperInput():
    print("input you entered is not in a correct format.")

if __name__ == "__main__":
    main(c)

