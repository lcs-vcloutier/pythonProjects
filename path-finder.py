import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# print maze
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    # loop over maze using enumerate (get index and value) in this case
    for i, row in enumerate(maze): # i is the row 
        for j, value in enumerate(row): # j is the column
            stdscr.addstr(i, j*2, value, BLUE) # print value at i, j x 2

# find the start (the O)
def find_start(maze, start):
     # loop over maze using enumerate (get index and value) in this case
    for i, row in enumerate(maze): # i is the row 
        for j, value in enumerate(row): # j is the column
            if value == start: 
                return i, j

# find the best path (this is the algorithm)
def find_path(maze, stdscr):
    start = "O"
    end = "X" 





# standard output screen -> will override terminal
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # initializing first color pairing
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # initializing second color pairing
    stdscr.clear() # clear the screen
    print_maze(maze, stdscr) # call above func to print maze
    stdscr.refresh() # refresh
    stdscr.getch() # get character -> input statement

wrapper(main)