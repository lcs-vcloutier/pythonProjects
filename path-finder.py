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
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED) # print value at i, j x 2
            else:
                stdscr.addstr(i, j*2, value, BLUE) # print value at i, j x 2

# find the start (the O)
def find_start(maze, start):
     # loop over maze using enumerate (get index and value) in this case
    for i, row in enumerate(maze): # i is the row 
        for j, value in enumerate(row): # j is the column
            if value == start: 
                return i, j
    return None

# find the best path (this is the algorithm)
def find_path(maze, stdscr):
    start = "O"
    end = "X" 
    start_pos = find_start(maze, start)

    q = queue.Queue() # first in first out data structure
    q.put((start_pos, [start_pos])) # keep track of current position as well as path to get to that node !
    visited = set() # all of the positions we've visited

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos # break current pos down

        stdscr.clear() # clear the screen
        print_maze(maze, stdscr, path) # draw the path
        time.sleep(0.2)
        stdscr.refresh() # refresh

        if maze[row][col] == end:
            return path
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] == "#":
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
        
def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0: # CHECK UP 
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): # CHECK DOWN
        neighbors.append((row + 1, col))
    if col > 0: # CHECK LEFT 
        neighbors.append((row, col -1))
    if col + 1 < len(maze[0]): # CHECK RIGHT
        neighbors.append((row, col + 1))

    return neighbors




# standard output screen -> will override terminal
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) # initializing first color pairing
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # initializing second color pairing
    
    find_path(maze, stdscr)
    stdscr.getch() # get character -> input statement

wrapper(main)