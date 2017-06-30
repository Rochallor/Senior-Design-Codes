#==============================================================================
# Simple Move
# Written by Khira Morgan

# This function will implement a simple move and return the updated baord
# Functions: simple_move
# Input: oldboard = 2d list of old board position
# blank_square = 1d list with two elements
# diddo for occ_square
#==============================================================================

import simple_move

row1 = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'];
row2 = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'];
row3 = ['s', 's', 's', 's', 's', 's', 's', 's'];
row4 = ['s', 's', 's', 's', 's', 's', 's', 's'];
row5 = ['s', 's', 's', 's', 's', 's', 's', 's'];
row6 = ['s', 's', 's', 's', 's', 's', 's', 's'];
row7 = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'];
row8 = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'];

oldboard = [row1, row2, row3, row4, row5, row6, row7, row8];

a = 0;
b = 1;
c = 2;
d = 3;
e = 4;
f = 5;
g = 6;
h = 7;

row1 = 0;
row2 = 1;
row3 = 2;
row4 = 3;
row5 = 4;
row6 = 5;
row7 = 6;
row8 = 7;

new_blank = [1,1]
new_occupied = [2,2]

def print_board(board):
    for i in range(0,len(board)):
        print(board[len(board)-i-1]);

print_board(oldboard);

newboard = simple_move.simple_move(oldboard, new_blank, new_occupied);

print("");
print("Move Made: " + str(new_blank[0]) + str(new_blank[1]) + ' to ' + str(new_occupied[0]) + str(new_occupied[1]))
print("");    
print_board(newboard);