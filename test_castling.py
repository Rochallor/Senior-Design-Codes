#==============================================================================
# File Name: 	test_castling
# Author: 	   Khira Morgan
# Project:	   Senior Design Fall 2017
# 
# Description: This script serves to test the separate code "castling" by
#              passing the inputs oldboard, new_blank_king, new_blank_rook,
#              new_occupied_king, and new_occupied_rook into the castling 
#              function, getting the output "newboard" back, and finally
#              printing the old and new boards for comparison.
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
# 	       iv.  The variable "side" is used the denote King, 'K', or Queen, 'Q',
#              side castling. Change this variable to test.
#         v.   The variable "player" is used to indicated whether White or
#              Black made the castling move. Change this variable to test.
# Assumptions:
# 	       i.   In King Side Castling, the two spaces between the King and the
#              Rook are already blank.
#        ii.   In Queen Side Castling, the three spaces between the King and
#              the Rook are already blank.
#==============================================================================

import castling

row1 = ['r', 's', 's', 's', 'k', 's', 's', 'r'];
row2 = ['p', 'p', 'p', 'q', 's', 'p', 'p', 'p'];
row3 = ['s', 's', 'n', 'b', 'b', 's', 's', 'n'];
row4 = ['s', 's', 's', 'p', 'p', 's', 's', 's'];
row5 = ['s', 'P', 's', 'P', 's', 's', 'P', 's'];
row6 = ['N', 'B', 's', 's', 's', 'N', 's', 'B'];
row7 = ['P', 's', 'P', 'Q', 'P', 'P', 's', 'P'];
row8 = ['R', 's', 's', 's', 'K', 's', 's', 'R'];

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

side = 'K'          # Change this variable to test King or Queen Side Castling
player = 'W'        # Change this variable to indicate White or Black player

def print_board(board):
    for i in range(0,len(board)):
        print(board[len(board)-i-1]);

print("Previous Board:")
print_board(oldboard);

newboard = castling.castling(oldboard, side, player);

print("");
print("Move Made: " + str(side) + " side Castling")
print("Player: " + str(player))
print("");
print("Updated Board:")    
print_board(newboard);