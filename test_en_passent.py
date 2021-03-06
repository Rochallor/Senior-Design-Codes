#==============================================================================
# File Name: 	test_en_passent
# Author: 	   Khira Morgan
# Project:	   Senior Design Fall 2017
# 
# Description: This script serves to test the separate code "en_passent" by
#              passing the inputs oldboard, new_blank, new_occupied, and
#              pawn_taken into the simple move function, getting the output 
#              "newboard" back, and finally printing the old and new boards
#              for comparison.
# Definitions: 
# 	       i.   row1, row2, row3, row4, row5, row6, row7, and row8 are defined
#              as each row in a standard chess board complete with piece/space
#              designations.
# 	       ii.  Uppercase Letters are the Black Pieces
#              Lowercase Letters are the White Pieces
# 	       iii. r & R = Rook        k & K = King
#              n & N = Knight      p & P = Pawn
#              b & B - Bishop      s = Space
#              q & Q = Queen
#==============================================================================

import en_passent

row1 = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'];
row2 = ['p', 'p', 'p', 'p', 's', 'p', 'p', 'p'];
row3 = ['s', 's', 's', 's', 's', 's', 's', 's'];
row4 = ['s', 's', 's', 'P', 'p', 's', 's', 's'];
row5 = ['s', 's', 's', 's', 's', 's', 's', 's'];
row6 = ['s', 's', 's', 's', 's', 's', 's', 's'];
row7 = ['P', 'P', 'P', 's', 'P', 'P', 'P', 'P'];
row8 = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'];

oldboard = [row1, row2, row3, row4, row5, row6, row7, row8];

row1 = 0;
row2 = 1;
row3 = 2;
row4 = 3;
row5 = 4;
row6 = 5;
row7 = 6;
row8 = 7;

a = 0;
b = 1;
c = 2;
d = 3;
e = 4;
f = 5;
g = 6;
h = 7;

new_blank = [3,3]
new_occupied = [4,4]
pawn_taken = [3,4]

def print_board(board):
    for i in range(0,len(board)):
        print(board[len(board)-i-1]);

print("Previous Board:")
print_board(oldboard);

newboard = en_passent.en_passent(oldboard, new_blank, new_occupied, pawn_taken);

print("");
print("Move Made: row " + str(new_blank[0]) + " column " + str(new_blank[1]) + " to row " + str(new_occupied[0]) + " column " + str(new_occupied[1]))
print("Pawn Taken: row " + str(pawn_taken[0]) + " column " + str(pawn_taken[1]))
print("");
print("Updated Board:")    
print_board(newboard);